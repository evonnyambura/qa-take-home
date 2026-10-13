import os
import uuid
from datetime import date, timedelta
from pathlib import Path
import pytest
import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")


def _require(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} is not set. Copy .env.example to .env.")
    return value


BASE_URL = _require("BASE_URL").rstrip("/")
API_USERNAME = _require("API_USERNAME")
API_PASSWORD = _require("API_PASSWORD")
NON_EXISTENT_ID = 999999999

SESSION = requests.Session()


def call(method, path, expected_status, **kwargs):
    """Send a request; assert status code and response time (< 2 s)."""
    SESSION.cookies.clear()  
    headers = {"Accept": "application/json", **kwargs.pop("headers", {})}
    response = SESSION.request(
        method, f"{BASE_URL}{path}", headers=headers, timeout=10, **kwargs
    )
    assert response.status_code == expected_status, (
        f"{method} {path}: expected {expected_status}, got "
        f"{response.status_code}. Body: {response.text[:200]!r}"
    )
    elapsed = response.elapsed.total_seconds()
    assert elapsed < 2, f"{method} {path} took {elapsed:.3f}s (limit 2s)"
    return response


def make_payload(**overrides):
    """Valid booking. Relative dates never go stale; unique last name avoids
    clashes with other users on this shared practice site."""
    payload = {
        "firstname": "Jane",
        "lastname": f"Tester{uuid.uuid4().hex[:8]}",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": (date.today() + timedelta(days=30)).isoformat(),
            "checkout": (date.today() + timedelta(days=34)).isoformat(),
        },
        "additionalneeds": "Breakfast",
    }
    payload.update(overrides)
    return payload


def assert_booking_matches(actual, expected):
    for field in ("firstname", "lastname", "totalprice", "depositpaid", "additionalneeds"):
        assert actual[field] == expected[field], (
            f"{field}: expected {expected[field]!r}, got {actual[field]!r}"
        )
    assert actual["bookingdates"] == expected["bookingdates"]


def assert_error_body(response):
    """Error responses must carry a message and must not look like a success."""
    body = response.text.strip()
    assert body, "Error response has an empty body"
    assert "bookingid" not in body, f"Error response contains a booking: {body[:200]!r}"


@pytest.fixture(scope="session", autouse=True)
def warm_up():
    """Wake the shared server and open the connection before anything is timed.
    This is setup, not a test, so its time is not asserted."""
    try:
        SESSION.get(f"{BASE_URL}/ping", timeout=30)
    except requests.RequestException:
        pass


@pytest.fixture(scope="session")
def auth_token():
    """One token per run, kept in a variable (never pasted into requests)."""
    response = call(
        "POST", "/auth", 200,
        json={"username": API_USERNAME, "password": API_PASSWORD},
    )
    token = response.json().get("token")
    assert isinstance(token, str) and token
    return token


@pytest.fixture
def auth_headers(auth_token):
    return {"Cookie": f"token={auth_token}"}


@pytest.fixture
def booking(auth_headers):
    """Create a booking and pass its ID + payload to the test automatically;
    delete it afterwards so the shared site stays clean."""
    payload = make_payload()
    response = call("POST", "/booking", 200, json=payload)
    data = response.json()
    booking_id = data["bookingid"]
    assert isinstance(booking_id, int)
    assert_booking_matches(data["booking"], payload)

    yield {"id": booking_id, "payload": payload}

    try:
        SESSION.delete(f"{BASE_URL}/booking/{booking_id}", headers=auth_headers, timeout=10)
    except requests.RequestException:
        pass


def test_01_auth_returns_token():
    response = call(
        "POST", "/auth", 200,
        json={"username": API_USERNAME, "password": API_PASSWORD},
    )
    token = response.json().get("token")
    assert isinstance(token, str) and token


def test_02_create_booking(auth_headers):
    payload = make_payload()
    response = call("POST", "/booking", 200, json=payload)
    data = response.json()
    assert isinstance(data["bookingid"], int)
    assert_booking_matches(data["booking"], payload)

    cleanup = call("DELETE", f"/booking/{data['bookingid']}", 201, headers=auth_headers)
    assert cleanup.text == "Created"


def test_03_get_booking_by_id(booking):
    response = call("GET", f"/booking/{booking['id']}", 200)
    assert_booking_matches(response.json(), booking["payload"])


def test_04_put_updates_booking(booking, auth_headers):
    updated = make_payload(
        firstname="Janet", lastname="Updated", totalprice=200,
        depositpaid=False, additionalneeds="Lunch",
    )
    response = call(
        "PUT", f"/booking/{booking['id']}", 200, headers=auth_headers, json=updated
    )
    assert_booking_matches(response.json(), updated)

    stored = call("GET", f"/booking/{booking['id']}", 200).json()  
    assert_booking_matches(stored, updated)


def test_05_patch_updates_only_sent_field(booking, auth_headers):
    response = call(
        "PATCH", f"/booking/{booking['id']}", 200,
        headers=auth_headers, json={"firstname": "Patched"},
    )
    expected = {**booking["payload"], "firstname": "Patched"}
    assert_booking_matches(response.json(), expected)

    stored = call("GET", f"/booking/{booking['id']}", 200).json()  
    assert_booking_matches(stored, expected)


def test_06_delete_booking(booking, auth_headers):
    response = call("DELETE", f"/booking/{booking['id']}", 201, headers=auth_headers)
    assert response.text == "Created"

    gone = call("GET", f"/booking/{booking['id']}", 404)
    assert gone.text == "Not Found"


@pytest.mark.xfail(reason="F-01: missing fields return 500 instead of 400", strict=False)
def test_07_create_with_missing_fields_returns_400():
    response = call("POST", "/booking", 400, json={"firstname": "Jane"})
    assert_error_body(response)


@pytest.mark.xfail(reason="F-02: wrong data type (totalprice as text) not rejected with 400", strict=False)
def test_08_create_with_wrong_data_type_returns_400():
    response = call("POST", "/booking", 400, json=make_payload(totalprice="abc"))
    assert_error_body(response)


def test_09_get_nonexistent_booking_returns_404():
    response = call("GET", f"/booking/{NON_EXISTENT_ID}", 404)
    assert response.text == "Not Found"


@pytest.mark.xfail(reason="F-03: PUT on a non-existent booking returns 405 instead of 404", strict=False)
def test_10_put_nonexistent_booking_returns_404(auth_headers):
    response = call(
        "PUT", f"/booking/{NON_EXISTENT_ID}", 404,
        headers=auth_headers, json=make_payload(),
    )
    assert response.text == "Not Found"


def test_11_put_without_token_is_forbidden(booking):
    response = call(
        "PUT", f"/booking/{booking['id']}", 403,
        json=make_payload(firstname="Hacker"),
    )
    assert response.text == "Forbidden"

    stored = call("GET", f"/booking/{booking['id']}", 200).json()  
    assert_booking_matches(stored, booking["payload"])


def test_12_delete_with_wrong_token_is_forbidden(booking):
    response = call(
        "DELETE", f"/booking/{booking['id']}", 403,
        headers={"Cookie": "token=invalid_token"},
    )
    assert response.text == "Forbidden"

    stored = call("GET", f"/booking/{booking['id']}", 200).json()  
    assert_booking_matches(stored, booking["payload"])