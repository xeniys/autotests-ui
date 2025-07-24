from components.base_components import BaseComponent
from playwright.sync_api import Page, expect


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    def check_visible(self, username):
        expect(self.app_title).to_be_visible()
        expect(self.app_title).to_have_text("UI Course")

        expect(self.welcome_title).to_be_visible()
        expect(self.welcome_title).to_have_text(f"Welcome, {username}!")

