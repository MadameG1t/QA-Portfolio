from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls
from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage
from pages.cart_page import CartPage



def test_can_open_cart_checkout_page(driver, purchased_product):
    driver.get(Urls.CHECKOUT)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(CartPage.CHECKOUT_CARD)
    )
    assert "/checkout" in driver.current_url
