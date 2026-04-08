from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def should_be_open(self):
        expect(self.page.locator('[data-test="shopping-cart-link"]')).to_be_visible()

    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def add_bike_light_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    def should_have_cart_badge(self, value):
        expect(self.page.locator('[data-test="shopping-cart-badge"]')).to_have_text(value)

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def logout(self):
        self.page.locator('#react-burger-menu-btn').click()
        self.page.locator('#logout_sidebar_link').click()