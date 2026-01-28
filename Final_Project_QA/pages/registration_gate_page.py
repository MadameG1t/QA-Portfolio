from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls


class RegistrationGatePage:

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='confirmPassword']")  # if present
    REGISTER_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error, .alert-danger")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success, .alert-success")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(Urls.REGISTER)

    def register(self, email: str, password: str, confirm_password: str | None = None) -> None:
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)


        if confirm_password is not None:
            self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
            self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)

        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BTN)).click()

    def get_error_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    def get_success_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
