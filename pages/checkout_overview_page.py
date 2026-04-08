from playwright.sync_api import Page, expect


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page

    def should_be_open(self):
        expect(self.page.locator('[data-test="finish"]')).to_be_visible()

    def finish_checkout(self):
        self.page.locator('[data-test="finish"]').click()