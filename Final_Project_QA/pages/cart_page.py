from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls


class CartPage:
    CART_ICON = (By.CSS_SELECTOR, "div.headerIcon")  # cart icon in header

    TOTAL_TEXT = (By.CSS_SELECTOR, "div.total-container h5:last-child")
    SHIPPING_COST = (By.CSS_SELECTOR, "div.shipment-container h5:last-child")

    REMOVE_FIRST_ITEM_BTN = (By.CSS_SELECTOR, "button.minus")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_cart(self) -> None:

        self.driver.get(Urls.CHECKOUT)

        if "/checkout" not in self.driver.current_url:
            self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

        self.wait.until(EC.visibility_of_element_located(self.TOTAL_TEXT))

    def get_total_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.TOTAL_TEXT)).text.strip()

    def get_shipping_cost_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.SHIPPING_COST)).text.strip()

    def remove_first_item(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_FIRST_ITEM_BTN)).click()
