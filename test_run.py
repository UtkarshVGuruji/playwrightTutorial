from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.facebook.com/
    page.goto("https://www.facebook.com/")
    page.set_default_timeout(3000)
    # Click [data-testid="royal_email"]
    page.click("[data-testid=\"royal_email\"]")
    # Fill [data-testid="royal_email"]
    page.fill("[data-testid=\"royal_email\"]", "utkarsh.guruji@gmail.com")
    # Press Tab
    page.press("[data-testid=\"royal_email\"]", "Tab")
    # Fill [data-testid="royal_pass"]
    page.fill("[data-testid=\"royal_pass\"]", "Bangalore@123")
    # Click [data-testid="royal_login_button"]
    # with page.expect_navigation(url="https://www.facebook.com/"):
    with page.expect_navigation():
        page.click("[data-testid=\"royal_login_button\"]")
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
