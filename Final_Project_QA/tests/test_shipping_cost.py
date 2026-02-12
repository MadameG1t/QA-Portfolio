from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from utils.constants import Urls


def test_shipping_cost_is_5_when_total_below_20(driver):
    driver.get(Urls.STORE)
    AgeGatePage(driver).pass_age_gate_if_present()

    store = StorePage(driver)
    store.add_first_product_to_cart_with_quantity(1)  # small total, should be below 20

    cart = CartPage(driver)
    cart.open_cart()

    total_text = cart.get_total_text()
    shipping_text = cart.get_shipping_cost_text()

    print("Total:", total_text)
    print("Shipping:", shipping_text)

    assert shipping_text == "5€", f"Expected shipping 5€ when below threshold, got: {shipping_text}"