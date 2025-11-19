from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class StreamerPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, "/{name}")

        self.welcome_chat_label: Locator = page.locator("//span[text()='Welcome to the chat room!']")


