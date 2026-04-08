from playwright.sync_api import Page, expect
from config import BASE_URL, USERNAME, PASSWORD


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)

    def should_be_open(self):
        expect(self.page.locator('[data-test="username"]')).to_be_visible()
        expect(self.page.locator('[data-test="password"]')).to_be_visible()
        expect(self.page.locator('[data-test="login-button"]')).to_be_visible()

    def login_as_standard_user(self):
        self.page.locator('[data-test="username"]').fill(USERNAME)
        self.page.locator('[data-test="password"]').fill(PASSWORD)
        self.page.locator('[data-test="login-button"]').click()