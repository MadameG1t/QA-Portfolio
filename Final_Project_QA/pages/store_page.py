import re
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StorePage:
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div.product-grid div.product-card")
    ADD_TO_CART_IN_CARD = (By.CSS_SELECTOR, "button.btn-cart")
    QUANTITY_INPUT_IN_CARD = (By.CSS_SELECTOR, "input.quantity")
    PRICE_IN_CARD = (By.CSS_SELECTOR, "h5.discount-price")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def parse_price(self, text: str) -> float:
        cleaned = (
            text.replace("€", "")
                .replace("$", "")
                .replace("EUR", "")
                .replace(",", ".")
                .strip()
        )
        try:
            return float(cleaned)
        except ValueError:
            raise AssertionError(f"Could not parse price from: '{text}'")

    def get_first_product_unit_price(self) -> float:
        first_card = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_CARDS)
        )[0]
        price_text = first_card.find_element(*self.PRICE_IN_CARD).text.strip()
        return self.parse_price(price_text)

    def open_first_product(self) -> None:
        cards = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_CARDS))
        first_card = cards[0]
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", first_card)
        self.wait.until(EC.element_to_be_clickable(first_card))
        self.driver.execute_script("arguments[0].click();", first_card)

    def add_first_product_to_cart(self) -> None:
        cards = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_CARDS))
        first_card = cards[0]

        add_btn = self.wait.until(
            EC.element_to_be_clickable(first_card.find_element(*self.ADD_TO_CART_IN_CARD))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_btn)
        self.driver.execute_script("arguments[0].click();", add_btn)

    def add_first_product_to_cart_with_quantity(self, qty: int) -> None:
        cards = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_CARDS))
        first_card = cards[0]

        qty_input = self.wait.until(
            EC.visibility_of(first_card.find_element(*self.QUANTITY_INPUT_IN_CARD))
        )
        qty_input.clear()
        qty_input.send_keys(str(qty))

        add_btn = self.wait.until(
            EC.element_to_be_clickable(first_card.find_element(*self.ADD_TO_CART_IN_CARD))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_btn)
        self.driver.execute_script("arguments[0].click();", add_btn)
