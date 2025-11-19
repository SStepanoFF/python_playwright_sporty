from playwright.async_api import Locator
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.search_result_streamer_widget import SearchResultStreamerWidget


class SearchResultPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, "/search")

        self.search_result_streamer: SearchResultStreamerWidget = SearchResultStreamerWidget(
            page.locator("//section//button/div"))

    def select_first_streamer(self):
        first_streamer = self.search_result_streamer.streamer_name.filter(visible=True).first
        first_streamer.click()

