from playwright.sync_api import Page

from config import FIRST_NAME, LAST_NAME, POSTAL_CODE
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_login_page_opens(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.should_be_open()


def test_standard_user_can_login(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.should_be_open()


def test_add_one_product_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.should_have_cart_badge("1")


def test_add_two_products_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.should_have_cart_badge("2")


def test_cart_contains_selected_product(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.should_be_open()
    cart_page.should_contain_product("Sauce Labs Backpack")


def test_user_can_open_checkout_step_one(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    checkout_page.should_be_open()


def test_user_can_open_checkout_overview(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = CheckoutOverviewPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.continue_checkout()

    overview_page.should_be_open()


def test_user_can_finish_order(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = CheckoutOverviewPage(page)
    complete_page = CheckoutCompletePage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.continue_checkout()
    overview_page.finish_checkout()

    complete_page.should_be_open()


def test_standard_user_can_logout(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.logout()

    login_page.should_be_open()

def test_cart_contains_two_selected_products(page: Page):
    login_page =  LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login_as_standard_user()
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.open_cart()

    cart_page.should_be_open()
    cart_page.should_contain_products([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])
