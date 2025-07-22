from playwright.sync_api import sync_playwright, expect, Playwright
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state, playwright):
    page = chromium_page_with_state

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
