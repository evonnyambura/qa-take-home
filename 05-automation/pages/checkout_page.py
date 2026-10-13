from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = self.by_test_id("firstName")
        self.last_name_input = self.by_test_id("lastName")
        self.postal_code_input = self.by_test_id("postalCode")
        self.continue_button = self.by_test_id("continue")
        self.finish_button = self.by_test_id("finish")
        self.complete_header = self.by_test_id("complete-header")
        self.complete_text = self.by_test_id("complete-text")

    def fill_customer_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()