from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def should_be_open(self):
        expect(self.page.locator('[data-test="firstName"]')).to_be_visible()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="postalCode"]').fill(postal_code)

    def continue_checkout(self):
        self.page.locator('[data-test="continue"]').click()