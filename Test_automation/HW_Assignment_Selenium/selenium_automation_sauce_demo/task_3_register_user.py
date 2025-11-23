from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

def register_user_part_1():
    # 1. Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10) # Set implicit wait time

    # Define the URL
    url = 'http://automationexercise.com'
    print(f"Navigating to: {url}")

    # Command to navigate the browser to the specified URL
    driver.get(url)

    # Maximize the window for full view
    driver.maximize_window()



