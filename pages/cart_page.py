from playwright.sync_api import expect


class CartPage:

    def __init__(self, page):
        self.page = page

        self.checkout_button = "#checkout"
        self.cart_item = ".inventory_item_name"

    def verify_product_present(self):
        expect(self.page.locator(self.cart_item)).to_be_visible()

    def click_checkout(self):
        self.page.click(self.checkout_button)

        