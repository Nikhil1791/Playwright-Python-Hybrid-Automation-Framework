from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.config import USERNAME, PASSWORD


class TestSortProducts:

    def test_sort_products_low_to_high(self, page):

        login_page = LoginPage(page)
        home_page = HomePage(page)

        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)

        home_page.sort_low_to_high()


        