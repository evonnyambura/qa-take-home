# Task 5: UI automation (Playwright + Python + pytest)

Target: https://www.saucedemo.com (public practice shop).

## Run (one command after setup)
```bash
cd 05-automation
python -m venv .venv && source .venv/bin/activate    
pip install -r requirements.txt
playwright install chromium
pytest
```
Useful options: `pytest --headed` (watch the browser), `pytest -k checkout` (one test).
Run it from inside `05-automation/` so `pytest.ini` (base URL and options) is found.
On failure a screenshot and trace are saved in `test-results/`.

## The 4 tests
| No | Test | What it checks (what the user sees) |
|---|------|--------------------------------------|
| 1 | `test_standard_user_logs_in_and_sees_product_list` | URL, "Products" title, 6 products visible |
| 2 | `test_locked_out_user_sees_error_message` | Exact error text, user stays on login page |
| 3 | `test_adding_two_products_shows_cart_badge_2` | Badge shows "2", both buttons read "Remove" |
| 4 | `test_standard_user_completes_checkout` | Cart contents, then "Thank you for your order!" and an empty cart |

## Structure
```
05-automation/
├── pages/        page objects: login, inventory, cart, checkout (locators + actions only)
├── tests/        the 4 tests (all assertions live here)
├── conftest.py   fixtures: page objects and a logged-in standard_user
├── config.py     users and password
└── pytest.ini    base URL and options
```

## Design choices
- **Locators:** only `data-test` attributes (stable, not tied to layout or text).
- **No fixed waits:** Playwright `expect()` retries until the condition is met or times out.
- **Independence:** every test gets a fresh browser context and logs in itself; no test relies on another. They can run in any order.
- **Assertions:** visible text, counts, button labels and URLs, not just "the click worked".
- **Credentials:** `standard_user` / `secret_sauce` are shown on the public login page, so they are not secrets. They live in `config.py` and can be overridden with environment variables.

## CI (bonus)
`.github/workflows/e2e-tests.yml` (at the repo root) runs the tests on every push.
Passing run: 

