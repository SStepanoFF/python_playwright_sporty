import configparser

from playwright.async_api import Page
from playwright.sync_api import Locator


class BasePage:

    def __init__(self, page: Page, url_extension: str):
        self.page = page
        self.url_extension = url_extension

        self.search_field: Locator = page.locator("//input[@placeholder='Search']")
        self.search_button: Locator = page.locator("//button[@aria-label='Search Button']")
        self.accept_banner_button: Locator = page.locator("//button[@data-a-target='consent-banner-accept']")


    def open(self):
        config= configparser.ConfigParser()
        config.read('pytest.ini')
        base_url =  config["pytest"]["ui_base_url"]
        self.page.goto(base_url + self.url_extension)
        self.accept_banner_button.wait_for(state="visible")
        self.accept_banner_button.click()

    def scroll_down(self, times=2):
        self.wait_for_page_load()
        for _ in range(times):
            self.page.mouse.wheel(0, 1000)

    def search(self, criteria: str):
        self.search_field.fill(criteria)
        self.page.keyboard.press("Enter")


    def wait_and_screenshot(self, path="streamer_page.png"):
        self.wait_for_page_load()
        self.page.screenshot(path=path)

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")