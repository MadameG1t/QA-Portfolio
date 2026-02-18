from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from utils.helpers import parse_eur

class CartPage:
    CART_ICON = (
        By.XPATH,
        "//a[.//svg] | //button[.//svg]"
    )

    CHECKOUT_CARD = (By.CSS_SELECTOR, "div.checkout-card-body")
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

    def open_cart_via_icon(self):
        icon = self.wait.until(EC.visibility_of_element_located(self.CART_ICON))
        ActionChains(self.driver).move_to_element(icon).pause(0.2).click(icon).perform()
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_CARD))

    def get_total(self) -> float:
        return parse_eur(self.wait.until(EC.visibility_of_element_located(self.TOTAL_VALUE)).text)

    def get_product_total(self) -> float:
        return parse_eur(self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TOTAL_VALUE)).text)

    def get_shipment(self) -> float:
        return parse_eur(self.wait.until(EC.visibility_of_element_located(self.SHIPMENT_VALUE)).text)

    def remove_first_item(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_FIRST_ITEM_BTN)).click()
        print("DEBUG checkout url:", self.driver.current_url)
