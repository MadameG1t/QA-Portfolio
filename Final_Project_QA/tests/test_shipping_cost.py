import pytest

from pages.cart_page import CartPage


@pytest.fixture
def cart_page(cart_ready):
    return CartPage(cart_ready)

def test_shipping_cost_is_5_when_total_below_20(cart_page):
    assert cart_page.get_shipment() == 5.0