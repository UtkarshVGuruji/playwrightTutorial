from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://ui.eude1.ccloud.octobus.tools.sap/login?next=%2Fs%2Fgcs-all%2Fapp%2Fhome#/
    page.goto("https://ui.eude1.ccloud.octobus.tools.sap/login?next=%2Fs%2Fgcs-all%2Fapp%2Fhome#/")
    # Go to https://ajobbwdvt.accounts.ondemand.com/saml2/idp/sso/ajobbwdvt.accounts.ondemand.com?SAMLRequest=jVLLbtswEPwVgneRomqrCmE5cGMENZC2Rqzk0EtBkauGhUSqXNJp%2Fj6qH0V6aJorOTszO7OLy19DT%2FYQ0HpXU8FySsBpb6z7XtO75jqr6OVygWroi1GuUnxwt%2FAzAUYyDTqUx5%2BapuCkV2hROjUAyqjlbvXpRhYsl2Pw0WvfU7JChBAnqSvvMA0QdhD2VsPd7U1NH2IcUXKeLINkQDCte58M8zr6NiGL3vfIUI1cjZYj6BRsfOJ7wX%2BboGQ9ubJOxcMmZzL1w7fto9lHprT2yUVk3hkYlDNM%2B%2BEwWnBrRo7o%2F4emZLOu6beuUrpTnS5NW5Ug5uUMCtV2XdHO53P1HlrVzUpjqgmOmGDjMCoXa1rkhciEyN7lTV7KmZD5BZtdVF8p2Z4S%2BmDdMfnX4myPIJQfm2abbb%2FsGkruzw1OAHrqSx7Uw8uiXidW53bo8s1dLPhLrT%2BX8nki36y3vrf6iaz63j9eBVARatqpHoGSax8GFf%2FtRzBxeLEm6w5QmRyOoG1nwVC%2BPOn%2BfZPLZw%3D%3D
    page.goto("https://ajobbwdvt.accounts.ondemand.com/saml2/idp/sso/ajobbwdvt.accounts.ondemand.com?SAMLRequest=jVLLbtswEPwVgneRomqrCmE5cGMENZC2Rqzk0EtBkauGhUSqXNJp%2Fj6qH0V6aJorOTszO7OLy19DT%2FYQ0HpXU8FySsBpb6z7XtO75jqr6OVygWroi1GuUnxwt%2FAzAUYyDTqUx5%2BapuCkV2hROjUAyqjlbvXpRhYsl2Pw0WvfU7JChBAnqSvvMA0QdhD2VsPd7U1NH2IcUXKeLINkQDCte58M8zr6NiGL3vfIUI1cjZYj6BRsfOJ7wX%2BboGQ9ubJOxcMmZzL1w7fto9lHprT2yUVk3hkYlDNM%2B%2BEwWnBrRo7o%2F4emZLOu6beuUrpTnS5NW5Ug5uUMCtV2XdHO53P1HlrVzUpjqgmOmGDjMCoXa1rkhciEyN7lTV7KmZD5BZtdVF8p2Z4S%2BmDdMfnX4myPIJQfm2abbb%2FsGkruzw1OAHrqSx7Uw8uiXidW53bo8s1dLPhLrT%2BX8nki36y3vrf6iaz63j9eBVARatqpHoGSax8GFf%2FtRzBxeLEm6w5QmRyOoG1nwVC%2BPOn%2BfZPLZw%3D%3D")
    # Go to https://ui.eude1.ccloud.octobus.tools.sap/s/gcs-all/app/home#/
    page.goto("https://ui.eude1.ccloud.octobus.tools.sap/s/gcs-all/app/home#/")
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
