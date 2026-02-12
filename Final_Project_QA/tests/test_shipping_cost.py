from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from utils.constants import Urls


def test_shipping_cost_is_5_when_total_below_20(driver):
    print("STEP 1: opening store")
    driver.get(Urls.STORE)
    print("STEP 2: store opened, passing age gate if present")
    AgeGatePage(driver).pass_age_gate_if_present()
    print("STEP 3: age gate done, adding first product to cart")

    store = StorePage(driver)
    store.add_first_product_to_cart_with_quantity(1)
    print("STEP 4: product added, opening checkout/cart page")

    cart = CartPage(driver)
    cart.open_cart()  # direct URL open (stable)
    print("STEP 5: checkout opened, reading totals")

    total_text = cart.get_total_text()
    shipping_text = cart.get_shipping_cost_text()
    print("DEBUG Total:", total_text)
    print("DEBUG Shipping:", shipping_text)

    assert shipping_text == "5€", f"Expected shipping 5€ when below threshold, got: {shipping_text}"