import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import conftest

"""
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
"""

def test_web_form(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(2)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    time.sleep(2)

    text_box.send_keys("Data Entered")

    submit_button.click()

    time.sleep(2)

    form_submitted_heading= driver.find_element(by=By.CLASS_NAME,value="display-6")

    assert form_submitted_heading.text.lower() == "form submitted"



