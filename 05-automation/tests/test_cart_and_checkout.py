import re

from playwright.sync_api import expect

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


def test_adding_two_products_shows_cart_badge_2(logged_in):
    inventory = logged_in

    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)

    expect(inventory.cart_badge).to_have_text("2")
    expect(inventory.remove_button(BACKPACK)).to_have_text("Remove")
    expect(inventory.remove_button(BIKE_LIGHT)).to_have_text("Remove")


def test_standard_user_completes_checkout(
    page, logged_in, cart_page, checkout_page
):
    inventory = logged_in
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()
    expect(cart_page.item_names).to_have_text(["Sauce Labs Backpack"])

    cart_page.start_checkout()
    checkout_page.fill_customer_information("Jane", "Tester", "12345")
    checkout_page.finish()

    expect(page).to_have_url(re.compile(r"/checkout-complete\.html$"))
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
    expect(checkout_page.complete_text).to_contain_text("Your order has been dispatched")
    expect(inventory.cart_badge).to_have_count(0)  