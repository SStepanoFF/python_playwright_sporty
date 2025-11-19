from playwright.sync_api import Page, expect, Locator

from ui.pages.base_page import BasePage


class DirectoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, "/directory")


