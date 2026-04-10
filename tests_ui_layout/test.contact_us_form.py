from playwright.sync_api import Playwright, sync_playwright
#import pytest
from pom.contact_us_page import ContactUsPage

def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Symon", "123 Main Street", "test@email.com", "123-432-5434", "test subject", "test message blah")


with sync_playwright() as playwright:
    test_submit_form(playwright)
