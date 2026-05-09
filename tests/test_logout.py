from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.config import USERNAME, PASSWORD


class TestLogout:

    def test_logout(self, page):

        login_page = LoginPage(page)
        home_page = HomePage(page)

        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)

        home_page.logout()
        home_page.verify_logout()

        