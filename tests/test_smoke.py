import re
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def open_login_page(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)


def login(page: Page) -> None:
    open_login_page(page)
    page.locator('[data-test="username"]').fill(USERNAME)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()


def test_login_page_opens(page: Page):
    open_login_page(page)

    expect(page).to_have_url(re.compile(r"saucedemo\.com/?"))
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_standard_user_can_login(page: Page):
    login(page)

    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()


def test_add_product_to_cart(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")


def test_cart_contains_selected_product(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()

    expect(page).to_have_url(re.compile(r".*/cart\.html"))
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text("Sauce Labs Backpack")


def test_checkout_step_one_opens(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()

    expect(page).to_have_url(re.compile(r".*/checkout-step-one\.html"))
    expect(page.locator('[data-test="firstName"]')).to_be_visible()