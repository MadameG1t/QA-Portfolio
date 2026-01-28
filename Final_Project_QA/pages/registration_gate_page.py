from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.constants import Urls


class RegistrationGatePage:
    ACCOUNT_ICON = (
        By.XPATH,
        "//svg[contains(@class,'headerIcon-size')][.//path[contains(@d,'M12 2a5 5')]]"
    )

    CREATE_ACCOUNT_LINK = (
        By.XPATH,
        "//a[contains(@class,'switch-link') and normalize-space()='Create a new account']"
    )

    FULL_NAME_INPUT = (By.XPATH, "//input[@placeholder='Full Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email address']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    SIGN_UP_BTN = (By.CSS_SELECTOR, "button.submit-btn")

    AUTH_MODAL = (By.CSS_SELECTOR, ".auth-modal, .modal-content")
    ERROR_TEXT = (By.CSS_SELECTOR, ".error, .alert-danger")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(Urls.STORE)

    def open_auth_modal(self) -> None:
        icon = self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_ICON))
        self.driver.execute_script("arguments[0].click();", icon)
        self.wait.until(EC.visibility_of_element_located(self.AUTH_MODAL))

    def go_to_registration_form(self) -> None:
        self.open_auth_modal()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_LINK)).click()
        self.wait.until(EC.visibility_of_element_located(self.FULL_NAME_INPUT))

    def register(self, full_name: str, email: str, password: str) -> None:
        full_name_el = self.wait.until(EC.visibility_of_element_located(self.FULL_NAME_INPUT))
        full_name_el.clear()
        full_name_el.send_keys(full_name)

        email_el = self.driver.find_element(*self.EMAIL_INPUT)
        email_el.clear()
        email_el.send_keys(email)

        pw_el = self.driver.find_element(*self.PASSWORD_INPUT)
        pw_el.clear()
        pw_el.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_BTN)).click()

    def is_error_visible(self) -> bool:
        try:
            el = self.driver.find_element(*self.ERROR_TEXT)
            return el.is_displayed() and el.text.strip() != ""
        except Exception:
            return False

    def get_error_text(self) -> str:

        try:
            return self.wait.until(EC.visibility_of_element_located(self.ERROR_TEXT)).text
        except TimeoutException:
            return ""

    def is_signup_button_visible(self) -> bool:
        try:
            return self.driver.find_element(*self.SIGN_UP_BTN).is_displayed()
        except Exception:
            return False
