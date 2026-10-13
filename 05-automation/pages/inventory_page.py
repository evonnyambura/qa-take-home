from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = self.by_test_id("title")
        self.items = self.by_test_id("inventory-item")
        self.cart_badge = self.by_test_id("shopping-cart-badge")
        self.cart_link = self.by_test_id("shopping-cart-link")

    def add_button(self, product_slug: str):
        return self.by_test_id(f"add-to-cart-{product_slug}")

    def remove_button(self, product_slug: str):
        return self.by_test_id(f"remove-{product_slug}")

    def add_to_cart(self, product_slug: str):
        self.add_button(product_slug).click()

    def open_cart(self):
        self.cart_link.click()