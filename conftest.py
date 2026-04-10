import pytest
from playwright.sync_api import Playwright
import time
# import utils.secret_config
import os

from utils.secret_config import PASSWORD

try:
    PASSWORD = os.environ["PASSWORD"]
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture(scope="session")
def set_up(browser):
    # Access - Given
    #browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture(scope="session")
def login_set_up(set_up):

    page = set_up

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)


    page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)

    # page.click("'Log In'", timeout=2000)
    # page.click("[data-testid=\"signUp.switchToSignUp\"]")
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembersContainer'] input[type='email']")
    # page.click("[data-testid='siteMembersContainer'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    #page.fill("input[type='password']", utils.secret_config.PASSWORD)
    page.fill("input[type='password']", PASSWORD)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    # page.click("[aria-label='symon.storozhenko account menu']")

    yield page


@pytest.fixture
def go_to_new_collection_page(page):
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page

