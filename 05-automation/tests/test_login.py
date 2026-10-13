import re

from playwright.sync_api import expect

from config import LOCKED_OUT_USER, PASSWORD, STANDARD_USER

LOCKED_OUT_MESSAGE = "Epic sadface: Sorry, this user has been locked out."


def test_standard_user_logs_in_and_sees_product_list(page, login_page, inventory_page):
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items).to_have_count(6)
    expect(inventory_page.items.first).to_be_visible()


def test_locked_out_user_sees_error_message(page, login_page, inventory_page):
    login_page.open()
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(LOCKED_OUT_MESSAGE)
    expect(page).not_to_have_url(re.compile(r"/inventory\.html"))
    expect(inventory_page.items).to_have_count(0)