from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from config.config import USERNAME, PASSWORD


class TestAddToCart:

    def test_add_product_to_cart(self, page):

        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)

        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)

        home_page.add_product_to_cart()
        home_page.open_cart()

        cart_page.verify_product_present()

        