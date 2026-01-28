from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls


class RegistrationGatePage:

    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a.switch-link")

    FULL_NAME_INPUT = (By.XPATH, "//input[@placeholder='Full Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email address']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    SIGN_UP_BTN = (By.CSS_SELECTOR, "button.submit-btn")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(Urls.HOME)

    def switch_to_registration(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_LINK)).click()

    def register(self, full_name: str, email: str, password: str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.FULL_NAME_INPUT)).clear()
        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(full_name)

        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_BTN)).click()
