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
    context = browser.new_context(timeout=60000)
    page = context.new_page()
    yield page
    context.close()
