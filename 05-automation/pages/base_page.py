from playwright.sync_api import Locator, Page


class BasePage:
    """Shared helpers for all page objects."""

    def __init__(self, page: Page):
        self.page = page

    def by_test_id(self, value: str) -> Locator:
        """Sauce Demo marks elements with data-test attributes, the most stable locator."""
        return self.page.locator(f'[data-test="{value}"]')