from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright


def test_about_us_section_verbiage(playwright: Playwright) -> None:
    # Access - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    assert page.is_visible()(HomePage.celebrating_beauty_header)
    # Click text=playwright-ptactice was found by a group of like-minded fashion devotes, dete
    assert page.is_visible(HomePage.celebrating_beauty_body)

    context.close()
    browser.close()


