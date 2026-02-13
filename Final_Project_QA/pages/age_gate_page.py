from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from datetime import date

from utils.constants import AgeRules
from utils.helpers import date_of_birth_for_age_years, date_of_birth_entry_format

class AgeGatePage:

    DOB_INPUT = (By.CSS_SELECTOR, "input[placeholder='DD-MM-YYYY']")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Confirm']")
    SHOP_LINK = (By.CSS_SELECTOR, "a[href='/store']")
    UNDERAGE_MESSAGE = (
        By.XPATH,
        "//*[normalize-space()='You are underage. You can still browse the site, but you will not be able to view alcohol products.']"
    )
    ERROR_TEXT = (By.CSS_SELECTOR, "[role='alert'], .error, .alert, .text-red-500")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def go_to_store(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SHOP_LINK)).click()

    def enter_dob(self, dob_str: str) -> None:
        field = self.wait.until(EC.element_to_be_clickable(self.DOB_INPUT))
        field.click()
        field.clear()
        field.send_keys(dob_str)

    def submit(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()

    def age_gate_closed(self) -> bool:
        try:
            self.wait.until(EC.invisibility_of_element_located(self.DOB_INPUT))
            return True
        except TimeoutException:
            return False

    def age_gate_still_open(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.DOB_INPUT))
            return True
        except TimeoutException:
            return False

    def underage_message_visible(self) -> bool:
        return self.get_underage_message_text() != ""

    def get_underage_message_text(self) -> str:
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.UNDERAGE_MESSAGE))
            return el.text.strip()
        except TimeoutException:
            return ""

    def get_error_text(self) -> str:
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_TEXT))
            return el.text.strip()
        except TimeoutException:
            return ""

    def wait_for_age_gate(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.DOB_INPUT))
            return True
        except TimeoutException:
            return False

    def pass_age_gate_if_present(self) -> None:

        if not self.wait_for_age_gate():
            return

        dob = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
        dob_str = date_of_birth_entry_format(dob, AgeRules.DOB_FORMAT_HINT)

        self.enter_dob(dob_str)
        self.submit()

        if not self.age_gate_closed():
            err = self.get_error_text()
            raise AssertionError(f"Age gate did not close. Error: {err}")