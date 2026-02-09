from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    STREET = (By.CSS_SELECTOR, 'input[name="street"]')
    CITY = (By.CSS_SELECTOR, 'input[name="city"]')
    POSTAL = (By.CSS_SELECTOR, 'input[name="postalCode"]')
    CARD_NUMBER = (By.CSS_SELECTOR, 'input[name="cardNumber"]')
    CARD_NAME = (By.CSS_SELECTOR, 'input[name="nameOnCard"]')
    EXPIRATION = (By.CSS_SELECTOR, 'input[name="expiration"]')
    CVV = (By.CSS_SELECTOR, 'input[name="cvv"]')
    BUY_NOW = (By.CSS_SELECTOR, "button.btn-buy-now")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def complete_checkout(self, street, city, postal, number, name, exp, cvv):
        print("Checkout URL:", self.driver.current_url)
        print("Checkout title:", self.driver.title)

        self.wait.until(EC.visibility_of_element_located(self.STREET)).send_keys(street)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.driver.find_element(*self.CARD_NUMBER).send_keys(number)
        self.driver.find_element(*self.CARD_NAME).send_keys(name)
        self.driver.find_element(*self.EXPIRATION).send_keys(exp)
        self.driver.find_element(*self.CVV).send_keys(cvv)
        self.wait.until(EC.element_to_be_clickable(self.BUY_NOW)).click()
