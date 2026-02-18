from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls
from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage
from pages.cart_page import CartPage


def test_can_open_cart_checkout_page(driver):
    driver.get(Urls.STORE)
    AgeGatePage(driver).pass_age_gate_if_present()

    StorePage(driver).add_first_product_to_cart_with_quantity(1)

    driver.get(Urls.CHECKOUT)

    assert "/checkout" in driver.current_url

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(CartPage.CHECKOUT_CARD)
    )