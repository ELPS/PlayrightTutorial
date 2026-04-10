import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(playwright: Playwright):
    # Access - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
