from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AgeGatePage:
    DOB_INPUT = (By.CSS_SELECTOR, "input[placeholder='DD-MM-YYYY']")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='confirm']")

def __init__(self, driver, timeout=10):
    self.driver = driver
    self.wait = WebDriverWait(driver, timeout)

def open(self, url: str):
    self.driver.get(url)
