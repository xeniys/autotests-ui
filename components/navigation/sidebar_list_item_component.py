from components.base_components import BaseComponent
from playwright.sync_api import Page, expect


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, id: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{id}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{id}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{id}-drawer-list-item-button')

    def check_visible(self, title):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url):
        self.button.click()
        self.check_current_url(expected_url)
