import pytest

from config import PASSWORD, STANDARD_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage



@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def logged_in(login_page, inventory_page) -> InventoryPage:
    """Log in as standard_user through the UI (own session per test, no shared state)."""
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    return inventory_page