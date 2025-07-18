from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_disabled()

    page.get_by_test_id('registration-form-email-input').locator('input').fill('user.name@gmail.com')

    page.get_by_test_id('registration-form-username-input').locator('input').fill('username')

    page.get_by_test_id('registration-form-password-input').locator('input').fill('password')

    expect(reg_button).to_be_enabled()

    page.wait_for_timeout(500)

