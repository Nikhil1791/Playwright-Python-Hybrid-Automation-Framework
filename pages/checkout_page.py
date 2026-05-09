from playwright.sync_api import expect


class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.success_message = ".complete-header"

    def enter_checkout_details(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.postal_code, postal_code)
        self.page.click(self.continue_button)

    def finish_order(self):
        self.page.click(self.finish_button)

    def verify_order_success(self):
        expect(self.page.locator(self.success_message)).to_have_text(
            "Thank you for your order!"
        )

        