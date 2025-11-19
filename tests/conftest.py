import allure
from playwright.sync_api import Page

from pages.directory_page import DirectoryPage
from pages.search_result_page import SearchResultPage
import pytest
from playwright.sync_api import sync_playwright

from pages.streamer_page import StreamerPage


@pytest.fixture(scope="session")
def playwright():
    p = sync_playwright().start()
    yield p
    p.stop()


@pytest.fixture(scope="session")
def browser_context(playwright, request):
    mobile_device = request.config.getoption("--mobile-device") or request.config.getini("mobile_device")
    browser_name = request.config.getoption("--browser-name") or request.config.getini("browser")
    headless = request.config.getoption("--headless") or request.config.getini("headless")

    if mobile_device not in playwright.devices:
        raise RuntimeError(f"Device '{mobile_device}' not found. Available:\n{list(playwright.devices.keys())}")

    device = playwright.devices[mobile_device]
    print("Loaded device:", device)

    browser = playwright.chromium.launch(
        channel=browser_name,
        headless=str(headless).lower() == "true",
        args=["--disable-gpu", "--use-angle=metal"]
    )

    context = browser.new_context(
        # **device,
        viewport=device["viewport"],
        user_agent=device["user_agent"],
        device_scale_factor=device["device_scale_factor"],
        is_mobile=device["is_mobile"],
        has_touch=device["has_touch"],
    )
    # page = context.new_page()

    yield context

    context.close()
    browser.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


def pytest_addoption(parser):
    parser.addini("browser", "Browser to use for tests", default="chrome")
    parser.addini("headless", "Run in headless mode", default="false")
    parser.addini("mobile_device", "Device name for mobile emulation", default="Pixel 5")

    parser.addoption("--browser-name", action="store", help="Override browser from CLI")
    parser.addoption("--headless", action="store", help="Override headless mode true/false")
    parser.addoption("--mobile-device", action="store", help="Override device from CLI")


@pytest.fixture
def directory_page(page: Page):
    return DirectoryPage(page)


@pytest.fixture
def search_result_page(page: Page):
    return SearchResultPage(page)

@ pytest.fixture
def streamer_page(page: Page):
    return StreamerPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            allure.attach(
                page.screenshot(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                page.content(),
                name="page_html",
                attachment_type=allure.attachment_type.HTML
            )
