from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def should_be_open(self):
        expect(self.page.locator('[data-test="checkout"]')).to_be_visible()

    def should_contain_product(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def click_checkout(self):
        self.page.locator('[data-test="checkout"]').click()