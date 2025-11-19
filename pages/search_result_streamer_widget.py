from playwright.sync_api import Locator


class SearchResultStreamerWidget:
    def __init__(self, locator: Locator):
        self.locator = locator

        self.streamer_name = self.locator.locator("//h2[@title]")
