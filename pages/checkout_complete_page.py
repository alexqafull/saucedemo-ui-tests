from playwright.sync_api import Page, expect


class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page

    def should_be_open(self):
        expect(self.page.locator('[data-test="complete-header"]')).to_be_visible()