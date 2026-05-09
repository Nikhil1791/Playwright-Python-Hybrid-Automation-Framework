from pages.login_page import LoginPage
from config.config import USERNAME, PASSWORD, INVALID_PASSWORD


class TestLogin:

    def test_valid_login(self, page):

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)
        login_page.verify_successful_login()

    def test_invalid_login(self, page):

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(USERNAME, INVALID_PASSWORD)
        login_page.verify_invalid_login()

        