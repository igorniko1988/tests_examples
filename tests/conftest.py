import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    # Set default timeouts
    context.set_default_timeout(60000)  # 30 seconds for actions
    context.set_default_navigation_timeout(60000)  # 30 seconds for navigation
    page = context.new_page()
    yield page
    context.close()
