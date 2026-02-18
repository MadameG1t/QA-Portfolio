import pytest
from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from utils.constants import Urls

def test_can_open_cart_checkout_page(driver):
    driver.get(Urls.STORE)
    AgeGatePage(driver).pass_age_gate_if_present()

    StorePage(driver).add_first_product_to_cart_with_quantity(1)

    cart = CartPage(driver)
    cart.open_cart()

    assert cart.is_cart_loaded(), "Cart page did not load (checkout card not visible)."