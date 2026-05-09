from playwright.sync_api import expect


class HomePage:

    def __init__(self, page):
        self.page = page

        self.add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_icon = ".shopping_cart_link"
        self.sort_dropdown = ".product_sort_container"
        self.menu_button = "#react-burger-menu-btn"
        self.logout_button = "#logout_sidebar_link"

    def add_product_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def open_cart(self):
        self.page.click(self.cart_icon)

    def sort_low_to_high(self):
        self.page.select_option(self.sort_dropdown, "lohi")

    def logout(self):
        self.page.click(self.menu_button)
        self.page.wait_for_timeout(1000)
        self.page.click(self.logout_button)

    def verify_logout(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/")

        