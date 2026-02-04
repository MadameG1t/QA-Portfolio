
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    BUY_NOW = (By.CSS_SELECTOR, "button.btn-buy-now")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_buy_now(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.BUY_NOW)).click()
