import json

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import USERNAME, PASSWORD


class TestCheckout:

    def test_complete_checkout(self, page):

        with open("config/test_data.json") as file:
            data = json.load(file)

        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)

        home_page.add_product_to_cart()
        home_page.open_cart()

        cart_page.click_checkout()

        checkout_page.enter_checkout_details(
            data["first_name"],
            data["last_name"],
            data["postal_code"]
        )

        checkout_page.finish_order()
        checkout_page.verify_order_success()

        