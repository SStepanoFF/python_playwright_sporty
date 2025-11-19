from playwright.sync_api import Page, expect, Locator

from pages.base_page import BasePage
from pages.search_result_streamer_widget import SearchResultStreamerWidget


class DirectoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, "/directory")


