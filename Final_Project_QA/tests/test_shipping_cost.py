import math

from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from utils.constants import Urls


FREE_KEYWORD = "free"
NOT_FREE_KEYWORD = "above $20 get free shipping"


def qty_to_reach(target_total: float, unit_price: float) -> int:
    return max(1, math.ceil(target_total / unit_price))


def open_store_and_pass_age(driver) -> StorePage:
    driver.get(Urls.STORE)
    AgeGatePage(driver).pass_age_gate_if_present()
    return StorePage(driver)


def test_free_shipping_above_21(driver):
    store = open_store_and_pass_age(driver)

    unit_price = store.get_first_product_unit_price()
    qty = qty_to_reach(21.01, unit_price)  # strictly above 21
    store.add_first_product_to_cart_with_quantity(qty)

    cart = CartPage(driver)
    cart.open_cart()

    shipping_msg = cart.get_shipping_message().lower()
    assert FREE_KEYWORD in shipping_msg, f"Expected free shipping message, got: {shipping_msg}"


def test_shipping_not_free_at_19(driver):
    store = open_store_and_pass_age(driver)

    unit_price = store.get_first_product_unit_price()
    qty = qty_to_reach(19.00, unit_price)
    store.add_first_product_to_cart_with_quantity(qty)

    cart = CartPage(driver)
    cart.open_cart()

    shipping_msg = cart.get_shipping_message().lower()
    assert NOT_FREE_KEYWORD in shipping_msg, f"Expected paid-shipping message, got: {shipping_msg}"


def test_shipping_not_free_at_20(driver):
    store = open_store_and_pass_age(driver)

    unit_price = store.get_first_product_unit_price()
    qty = qty_to_reach(20.00, unit_price)
    store.add_first_product_to_cart_with_quantity(qty)

    cart = CartPage(driver)
    cart.open_cart()

    shipping_msg = cart.get_shipping_message().lower()
    assert NOT_FREE_KEYWORD in shipping_msg, f"Expected paid-shipping message, got: {shipping_msg}"


def test_removing_item_recalculates_shipping(driver):
    store = open_store_and_pass_age(driver)

    unit_price = store.get_first_product_unit_price()
    qty = qty_to_reach(21.01, unit_price)
    store.add_first_product_to_cart_with_quantity(qty)

    cart = CartPage(driver)
    cart.open_cart()

    before = cart.get_shipping_message().lower()
    assert FREE_KEYWORD in before, f"Expected free shipping before removal, got: {before}"

    cart.remove_first_item()

    after = cart.get_shipping_message().lower()
    assert after != "", "Shipping message disappeared after removing item."