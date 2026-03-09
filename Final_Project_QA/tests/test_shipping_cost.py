import pytest

from utils.constants import Urls
from pages.cart_page import CartPage

@pytest.fixture
def cart_on_checkout(purchased_product):
    driver = purchased_product
    driver.get(Urls.CHECKOUT)

    cart = CartPage(driver)
    cart.wait_until_loaded(timeout=15)
    return driver

@pytest.fixture
def cart_page(cart_on_checkout):
    page = CartPage(cart_on_checkout)
    page.open_cart()
    return page


def test_shipping_is_5_when_product_total_below_20(cart_page):
    cart_page.decrease_first_item_until_product_total_below(20.0)
    assert cart_page.get_product_total() < 20.0
    assert cart_page.get_shipment() == 5.0


def test_shipping_is_free_when_product_total_equals_20(cart_page):
    cart_page.increase_first_item_until_product_total_at_least(20.0)
    cart_page.decrease_first_item_until_product_total_below(21.0)

    total = cart_page.get_product_total()
    assert 20.0 <= total < 21.0
    assert cart_page.get_shipment() == 0.0


def test_shipping_is_free_when_product_total_above_20(cart_page):
    cart_page.increase_first_item_until_product_total_at_least(21.0)
    assert cart_page.get_product_total() >= 21.0
    assert cart_page.get_shipment() == 0.0


@pytest.mark.xfail(reason="BUG: Shipping cost does not recalculate when deleting items from the cart")
def test_removing_item_recalculates_shipping(cart_page):
    cart_page.increase_first_item_until_product_total_at_least(21.0)
    assert cart_page.get_shipment() == 0.0

    cart_page.remove_first_item()

    cart_page.wait_product_total_to_change(old_value=21.0, timeout=10)

    assert cart_page.get_product_total() < 20.0
    assert cart_page.get_shipment() == 5.0


@pytest.mark.xfail(reason="BUG: Shipping cost does not recalculate when total drops below 20€")
def test_shipping_recalculates_when_total_drops_below_20(cart_page):
    cart_page.increase_first_item_until_product_total_at_least(21.0)
    cart_page.wait_shipment_to_be(0.0)

    cart_page.decrease_first_item_until_product_total_below(20.0)
    cart_page.wait_product_total_below(20.0)

    actual_total = cart_page.get_product_total()
    actual_shipment = cart_page.get_shipment()

    assert actual_shipment == 5.0, (
        "Product quantity reduced value under 20€, shipment cost not readjusted.\n"
        f"Product Total: {actual_total}€ (expected < 20€)\n"
        f"Shipment: {actual_shipment}€ (expected 5.0€)"
    )
