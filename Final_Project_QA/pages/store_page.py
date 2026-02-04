from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StorePage:
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div.product-grid div.product-card")
    ADD_TO_CART_IN_CARD = (By.CSS_SELECTOR, "button.btn-cart")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_first_product(self) -> None:
        cards = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", cards[0])
        self.driver.execute_script("arguments[0].click();", cards[0])

    def add_first_product_to_cart(self) -> None:
        cards = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))
        first_card = cards[0]

        add_btn = first_card.find_element(*self.ADD_TO_CART_IN_CARD)

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_btn)
        self.driver.execute_script("arguments[0].click();", add_btn)

