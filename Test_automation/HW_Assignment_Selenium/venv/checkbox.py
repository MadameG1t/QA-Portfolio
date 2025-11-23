import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import conftest


def test_checkbox(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(2)

    #find elements in checkboxes
    checkboxes = driver.find_elements(By.NAME, "my-check")

    print(len(checkboxes))

