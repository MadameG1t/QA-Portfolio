
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

@pytest.mark.parametrize("name, email",
                         [
                             ("standard user","salmon.de@gmail.com" ),
                             ("locked_out_user", "secret_sauce"),
                             ("problem user", "secret_sauce@web.de")
])


def test_register_user_part_1(name,email):
    # 1. Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10) # Set implicit wait time
    wait = WebDriverWait(driver, 10)

    # 2. Navigate the URL
    url = 'http://automationexercise.com'
    print(f"Navigating to: {url}")
    # Command to navigate the browser to the specified URL
    driver.get(url)
    # Maximize the window for full view
    driver.maximize_window()

    # 3. verify home page is visible successfully
    assert "Automation Exercise" in driver.title, "Home page not loaded correctly"


    # 4. Click on 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()


    #remove cookie/consent overlay (NO try/except)
    driver.execute_script(
        """
        const overlays = document.querySelectorAll('div.fc-dialog-overlay, div.fc-dialog-container');
        overlays.forEach(o => {
            if (o && o.parentNode) {
                o.parentNode.removeChild(o);
            }
        });
        """
    )
    #4. Click on 'Signup / Login' button
    signup_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))
    )
    signup_link.click()

    # 5. Verify 'New User Signup!' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='New User Signup!']"))
    )

    # 6. Enter name and mail address
    driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-name'] ").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
    time.sleep(1)

    #check for correct name and email input
    name_pattern = r"^.{1,50}$"
    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
    assert re.match(name_pattern, name), f"Invalid name: {name}"
    assert re.match(email_pattern, email), f"Invalid email address: {email}"

    time.sleep(2)

    # 7. Click 'Signup' button
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(., 'Enter Account Information')]")
    ))

    #9. Fill details : Title, Name, Email, Password, Date of birth
    driver.find_element(By.CLASS_NAME, "clearfix" ).click()
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']").click()

    #date of birth by day, month, year
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='day']").click()
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='months']").click()
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='years']").click()


    #close browser at the end.
    driver.quit()
"""

    # 10. Select checkbox 'Sign up for our newsletter!'
    driver.find_element(By.ID, "newsletter").click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.ID, "optin").click()

    # 12. Fill address details
    driver.find_element(By.ID, "first_name").send_keys(FIRST_NAME)
    driver.find_element(By.ID, "last_name").send_keys(LAST_NAME)
    driver.find_element(By.ID, "company").send_keys(COMPANY)
    driver.find_element(By.ID, "address1").send_keys(ADDRESS1)
    driver.find_element(By.ID, "address2").send_keys(ADDRESS2)

    Select(driver.find_element(By.ID, "country")).select_by_visible_text(COUNTRY)
    driver.find_element(By.ID, "state").send_keys(STATE)
    driver.find_element(By.ID, "city").send_keys(CITY)
    driver.find_element(By.ID, "zipcode").send_keys(ZIPCODE)
    driver.find_element(By.ID, "mobile_number").send_keys(MOBILE)

    # 13. Click 'Create Account' button
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'ACCOUNT CREATED!') or contains(text(),'Account Created!')]")
    ))

    # 15. Click 'Continue' button
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()

    # Sometimes there can be a small delay/overlay – tiny pause helps
    time.sleep(2)

    # 16. Verify that 'Logged in as username' is visible
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, f"//a[contains(text(),'Logged in as {NAME}')]")
    ))

    # 17. Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, "Delete Account").click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'ACCOUNT DELETED!') or contains(text(),'Account Deleted!')]")
    ))
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
"""


