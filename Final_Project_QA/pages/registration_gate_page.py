from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.constants import Urls, AgeRules
from utils.helpers import date_of_birth_for_age_years, date_of_birth_entry_format
from pages.age_gate_page import AgeGatePage
from pages.store_page import StorePage



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
    SIGN_UP_BTN = (By.XPATH, "//button[contains(@class,'submit-btn') and normalize-space()='Sign Up']")


    AUTH_MODAL = (By.CSS_SELECTOR, ".auth-modal, .modal-content")
    ERROR_TEXT = (By.CSS_SELECTOR, ".error, .alert-danger")

    AGE_MODAL = (By.CSS_SELECTOR, ".ageVerification, .age-gate")
    AGE_DOB_INPUT = (By.CSS_SELECTOR, "input[placeholder*='DD'], input[placeholder*='YYYY'], input[type='text']")
    AGE_CONFIRM_BTN = (By.XPATH, "//button[normalize-space()='Enter' or normalize-space()='Confirm' or normalize-space()='Yes']")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(Urls.STORE)
        AgeGatePage(self.driver).pass_age_gate_if_present()

    def open_registration_via_add_to_cart(self) -> None:

        StorePage(self.driver).add_first_product_to_cart()

        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        self.ensure_signup_form()

    def go_to_registration_form(self) -> None:
        self.open_registration_via_add_to_cart()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_LINK)).click()
        self.wait.until(EC.visibility_of_element_located(self.FULL_NAME_INPUT))

    def ensure_signup_form(self) -> None:

        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.FULL_NAME_INPUT))
            return
        except TimeoutException:
            pass

        link = self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_LINK))
        self.driver.execute_script("arguments[0].click();", link)


        self.wait.until(EC.visibility_of_element_located(self.FULL_NAME_INPUT))

    def register(self, full_name: str, email: str, password: str) -> None:

        self.ensure_signup_form()

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

    def pass_age_gate_if_present(self) -> None:
        try:
            quick_wait = WebDriverWait(self.driver, 3)
            quick_wait.until(EC.visibility_of_element_located(self.AGE_MODAL))

            dob = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
            dob_str = date_of_birth_entry_format(dob, AgeRules.DOB_FORMAT_HINT)

            dob_el = quick_wait.until(EC.visibility_of_element_located(self.AGE_DOB_INPUT))
            dob_el.clear()
            dob_el.send_keys(dob_str)

            quick_wait.until(EC.element_to_be_clickable(self.AGE_CONFIRM_BTN)).click()

            self.wait.until(EC.invisibility_of_element_located(self.AGE_MODAL))

        except TimeoutException:
            return
