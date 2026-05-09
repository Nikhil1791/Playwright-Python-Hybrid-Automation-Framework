from playwright.sync_api import expect


class WaitUtil:

    @staticmethod
    def wait_for_element_visible(locator):
        expect(locator).to_be_visible()

    @staticmethod
    def wait_for_page_load(page):
        page.wait_for_load_state("networkidle")

    @staticmethod
    def hard_wait(page, seconds):
        page.wait_for_timeout(seconds * 1000)

        