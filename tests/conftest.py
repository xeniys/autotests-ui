import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    yield page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email = page.get_by_test_id('registration-form-email-input').locator('input')
    email.fill('user.name@gmail.com')

    username = page.get_by_test_id('registration-form-username-input').locator('input')
    username.fill('username')

    password = page.get_by_test_id('registration-form-password-input').locator('input')
    password.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    context.storage_state(path='browser-state.json')


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    yield page

