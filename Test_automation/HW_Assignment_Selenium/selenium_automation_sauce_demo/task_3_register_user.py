from lib2to3.fixes.fix_asserts import NAMES
from select import select

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
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
    #verify title section is visible
    assert driver.find_element(By.ID, "id_gender1").is_displayed()
    assert driver.find_element(By.ID, "id_gender2").is_displayed()

    #Title select Mr or Mrs
    driver.find_element(By.CSS_SELECTOR, "label[for='id_gender1']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='id_gender2']").click()

    #Name box
    name_on_form = driver.find_element(By.CSS_SELECTOR, "input[data-qa='name']")
    assert name_on_form.get_attribute("value") == name
    #email box
    email_on_form = driver.find_element(By.CSS_SELECTOR, "input[data-qa='email']")
    assert email_on_form.get_attribute("value") == email
    #password
    password_input = driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']")
    assert password_input.is_displayed() and password_input.is_enabled(), \
        "Password input is not ready for typing"

    password_input.click()
    password_input.send_keys("TestPassword123")
    assert password_input.get_attribute("value") == "TestPassword123"

    time.sleep(4)

    # Verify Day, Month, Year dropdowns are visible
    assert driver.find_element(By.CSS_SELECTOR, "select[data-qa='days']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "select[data-qa='years']").is_displayed()

    # 10. Select checkbox 'Sign up for our newsletter!'
    driver.find_element(By.ID, "newsletter").click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.ID, "option").click()

    # 12. Fill address details
    driver.find_element(By.ID, "first_name").send_keys("gretchen")
    driver.find_element(By.ID, "last_name").send_keys("Schadebrodt")
    driver.find_element(By.ID, "company").send_keys("N/A")
    driver.find_element(By.ID, "address1").send_keys("Schwedter Str. 14")
    driver.find_element(By.ID, "address2").send_keys("4")

    Select(driver.find_element(By.ID, "country")).select_by_value("germany")
    driver.find_element(By.ID, "state").send_keys("Berlin")
    driver.find_element(By.ID, "city").send_keys("Berlin")
    driver.find_element(By.ID, "zipcode").send_keys("10119")
    driver.find_element(By.ID, "mobile_number").send_keys("015167195071")

    # 13. Click 'Create Account' button
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'ACCOUNT CREATED!')")
    ))

    # 15. Click 'Continue' button
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()

    time.sleep(2)

    # 16. Verify that 'Logged in as username' is visible
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, f"//a[contains(text(),'Logged in as {NAMES}')]")
    ))

    # 17. Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, "Delete Account").click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'ACCOUNT DELETED!')")
    ))
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()

    #close browser at the end.
    driver.quit()



