import pytest
from pages.cart_page import CartPage


@pytest.fixture
def cart_page(driver, purchased_product):
    return CartPage(driver)


def test_shipping_cost_is_5_when_total_below_20(cart_page):
    shipment = cart_page.get_shipment()
    assert shipment == 5.0, f"Expected shipment to be 5€, but got {shipment}"