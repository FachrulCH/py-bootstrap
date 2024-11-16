import pytest
from playwright.sync_api import Page

from tests.web.pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)

    def test_login_with_valid_credentials(self):
        self.login_page.login("admin", "admin")
        self.login_page.error_message.to_be_hidden()