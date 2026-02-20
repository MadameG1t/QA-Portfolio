from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utils.constants import Urls
from utils.helpers import parse_eur


class CartPage:
    CART_ICON = (
        By.XPATH,
        "//div[contains(@class,'social-icon-cont')]"
        "//div[contains(@class,'headerIcon')][3]"
    )

    CHECKOUT_CARD = (By.CSS_SELECTOR, "div.checkout-card-body")

    def wait_until_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.CHECKOUT_CARD)
        )

    PLUS_FIRST = (By.CSS_SELECTOR, ".checkout-card-item-container:first-child button.plus")
    MINUS_FIRST = (By.CSS_SELECTOR, ".checkout-card-item-container:first-child button.minus")
    QTY_FIRST = (By.CSS_SELECTOR, ".checkout-card-item-container:first-child input.quantity-input")

    TOTAL_VALUE = (By.XPATH, "//div[contains(@class,'total-container')]/h5[2]")
    SHIPMENT_VALUE = (By.XPATH, "//div[contains(@class,'shipment-container')]/h5[2]")
    PRODUCT_TOTAL_VALUE = (By.XPATH, "//div[contains(@class,'product-total-container')]/h5[2]")

    REMOVE_FIRST_ITEM_BTN = (
        By.CSS_SELECTOR,
        ".basket-items-container .checkout-card-item-container:first-child a.remove-icon"
    )

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_cart(self):
        self.driver.get(Urls.CHECKOUT)
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_CARD))

    def is_cart_loaded(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_CARD))
            return True
        except TimeoutException:
            return False

    def open_cart_via_icon(self):
        icon = self.wait.until(EC.visibility_of_element_located(self.CART_ICON))
        ActionChains(self.driver).move_to_element(icon).pause(0.2).click(icon).perform()
        print("DEBUG open_cart_via_icon URL:", self.driver.current_url)
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_CARD))

    def get_first_item_quantity(self) -> int:
        el = self.wait.until(EC.visibility_of_element_located(self.QTY_FIRST))
        return int(el.get_attribute("value"))

    def set_first_item_quantity(self, target_qty: int, max_clicks: int = 50) -> None:
        current = self.get_first_item_quantity()
        clicks = 0

        while current != target_qty and clicks < max_clicks:
            if current < target_qty:
                self.wait.until(EC.element_to_be_clickable(self.PLUS_FIRST)).click()
            else:
                self.wait.until(EC.element_to_be_clickable(self.MINUS_FIRST)).click()

            current = self.get_first_item_quantity()
            clicks += 1

        if current != target_qty:
            raise AssertionError(f"Could not set quantity to {target_qty}. Current={current}")

    def wait_product_total_to_change(self, old_value: float, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(lambda d: self.get_product_total() != old_value)

    def get_total(self) -> float:
        return parse_eur(self.wait.until(EC.visibility_of_element_located(self.TOTAL_VALUE)).text)

    def get_product_total(self) -> float:
        return parse_eur(self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TOTAL_VALUE)).text)

    def get_shipment(self) -> float:
        return parse_eur(self.wait.until(EC.visibility_of_element_located(self.SHIPMENT_VALUE)).text)

    def remove_first_item(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_FIRST_ITEM_BTN)).click()

    def increase_first_item_until_product_total_at_least(self, target: float, max_clicks: int = 80) -> None:
        clicks = 0
        while self.get_product_total() < target and clicks < max_clicks:
            self.wait.until(EC.element_to_be_clickable(self.PLUS_FIRST)).click()
            clicks += 1

        if self.get_product_total() < target:
            raise AssertionError(f"Could not reach product total >= {target}. Current={self.get_product_total()}")

    def decrease_first_item_until_product_total_below(self, target: float, max_clicks: int = 80) -> None:
        clicks = 0
        while self.get_product_total() >= target and clicks < max_clicks:
            self.wait.until(EC.element_to_be_clickable(self.MINUS_FIRST)).click()
            clicks += 1

        if self.get_product_total() >= target:
            raise AssertionError(f"Could not get product total < {target}. Current={self.get_product_total()}")

    def wait_shipment_to_be(self, expected: float, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(lambda d: self.get_shipment() == expected)

    def wait_product_total_below(self, threshold: float, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(lambda d: self.get_product_total() < threshold)

    def wait_product_total_at_least(self, threshold: float, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(lambda d: self.get_product_total() >= threshold)