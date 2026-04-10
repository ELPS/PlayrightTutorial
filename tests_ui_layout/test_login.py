import time
from idlelib import browser

from playwright.sync_api import Playwright, sync_playwright
import pytest


def test_login(set_up) -> None:
    # Access - Given
    page = set_up



    # Act - When/Amd
    # page.click("button:has-text('Log In')", timeout=2000)
    # page.click("text=Log In")
    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)

    page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)

    #page.click("'Log In'", timeout=2000)
    #page.click("[data-testid=\"signUp.switchToSignUp\"]")
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembersContainer'] input[type='email']")
    # page.click("[data-testid='siteMembersContainer'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", "test123")
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")

    # -----------------------




