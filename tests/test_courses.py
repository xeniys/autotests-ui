from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
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

        context.storage_state(path='browser-state-courses.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        header_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(header_courses).to_be_visible()
        expect(header_courses).to_have_text('Courses')

        icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()

        courses_info = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_info).to_be_visible()
        expect(courses_info).to_have_text('There is no results')

        description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description).to_be_visible()
        expect(description).to_have_text('Results from the load test pipeline will be displayed here')
