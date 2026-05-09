from playwright.sync_api import expect
from config.config import BASE_URL


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def navigate(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def verify_successful_login(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def verify_invalid_login(self):
        expect(self.page.locator(self.error_message)).to_be_visible()

        