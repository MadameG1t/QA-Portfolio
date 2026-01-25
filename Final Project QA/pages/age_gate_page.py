from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AgeGatePage:

    DOB_INPUT = (By.CSS_SELECTOR, "input[placeholder='DD-MM-YYYY']")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Confirm']")
    SHOP_LINK = (By.CSS_SELECTOR, "a[href='/store']")
    UNDERAGE_MESSAGE = (
    By.XPATH, "//*[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'underage')]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def go_to_store(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOP_LINK)).click()

    def enter_dob(self, dob_str: str):
        field = self.wait.until(EC.element_to_be_clickable(self.DOB_INPUT))
        field.click()
        field.clear()
        field.send_keys(dob_str)

    def submit(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN))
        btn.click()

    def age_gate_closed(self) -> bool:
        try:
            self.wait.until(EC.invisibility_of_element_located(self.DOB_INPUT))
            return True
        except TimeoutException:
            return False

    def age_gate_still_open(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DOB_INPUT))
            return True
        except TimeoutException:
            return False

    def underage_message_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.UNDERAGE_MESSAGE))
            return True
        except Exception:
            return False


