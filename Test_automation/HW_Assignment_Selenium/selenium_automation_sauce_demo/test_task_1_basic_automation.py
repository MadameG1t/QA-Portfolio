from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

#initialize and navigate
def test_run_basic_automation():
     # 1. Initialize the Webdriver (Chrome)
    print("Launching Chrome browser...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 2.Navigate to the URL
    url = "https://www.saucedemo.com/"
    print(f"Navigating to: {url}")
    driver.get(url)

    driver.maximize_window()

    # 3. LOGIN AUTOMATION: Locate and interact with the login form
    print("Entering credentials...")

    # Enter Username: Located by ID
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Enter Password: Located by ID
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click the Login button: Located by ID
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)  # Wait for page transition

    # 4. LOGIN VERIFICATION (Page Title)
    print("Verifying successful login...")

    # Locate the title element using its class name 'title'
    products_title = driver.find_element(By.CLASS_NAME, "title")

    # ASSERTION 1: Check if the text matches "Products"
    assert products_title.text == "Products", "Login failed: Products page title not found or incorrect."
    print("SUCCESS: Logged in and verified Products page title.")

    # 5. PRODUCT VERIFICATION (Specific Item)
    product_name = "Sauce Labs Backpack"
    print(f"Verifying presence of product: '{product_name}'...")

    # Locate the product element using XPath to search by the exact visible text
    #backpack_product = driver.find_element(By.XPATH, f"//div[text()='{product_name}']")
    backpack_product = driver.find_element(By.ID, "item_4_title_link")
    time.sleep(2)

    # ASSERTION 2: Check if the element is displayed on the page
    assert backpack_product.is_displayed(), f"Product verification failed: '{product_name}' is not displayed."
    print(f"SUCCESS: Verified '{product_name}' is displayed on the page.")

    driver.quit()



