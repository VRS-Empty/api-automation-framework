import pytest
from playwright.sync_api import Page, expect

def test_saucedemo_login(page: Page):
    
    """
    Test case: Verify
    """

    print("\n[Step] Navigating to the login page...")
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")

    print("[Step] Entering username...")
    page.fill("#user-name", "standard_user")

    print("[Step] Entering password...")
    page.fill("#password", "secret_sauce")

    print("[Step] Clicking login button...")
    page.click("#login-button")

    print("[Step] Verifying login success...")

    expect(page.locator(".title")).to_have_text("Products", timeout=10000)

    expect(page.locator(".shopping_cart_link")).to_be_visible