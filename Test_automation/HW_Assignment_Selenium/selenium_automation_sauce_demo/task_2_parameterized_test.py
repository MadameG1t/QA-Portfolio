import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Note: The required fixtures and parameters (browser_driver, test_user, expected_success)
# are imported automatically by PyTest from the conftest.py file.

def test_login_parametrized(browser_driver, test_user, expected_success):
    """
    Tests login functionality with parameterized users.

    Args:
        browser_driver (fixture): The Selenium WebDriver instance from conftest.py.
        test_user (str): The username for the current test iteration.
        expected_success (bool): The expected outcome (True for success, False for failure).
    """
    driver = browser_driver
    password = "secret_sauce"
    url = "https://www.saucedemo.com/"

    print(f"\n--- Running Test ---")
    print(f"User: {test_user} | Expected Outcome: {'Success' if expected_success else 'Failure'}")

    # 1. Navigate and Login
    driver.get(url)
    driver.find_element(By.ID, "user-name").send_keys(test_user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # 2. Assertions based on Expected Outcome
    if expected_success:
        # PATH A: EXPECTED SUCCESS (standard_user, problem_user, performance_glitch_user)
        try:
            # Check for success: The "Products" title should be visible
            products_title = driver.find_element(By.CLASS_NAME, "title")
            assert products_title.text == "Products", f"TEST FAILED: Login failed unexpectedly for {test_user}"
            print(f"Result: PASS. Logged in successfully.")

            # CRITICAL: Clean up state (log out) before the next parameterized test runs.
            driver.delete_all_cookies()
            driver.get(url)

        except NoSuchElementException:
            # If the success element is missing, but no explicit error message is found, fail the test
            error_message = "No Products title found. Check if an error message is present."
            try:
                error_message_element = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
                error_message = error_message_element.text
            except NoSuchElementException:
                pass

            pytest.fail(f"TEST FAILED: Login failed for {test_user}. Error: {error_message}")

    else:
        # PATH B: EXPECTED FAILURE (locked_out_user)
        try:
            # Check for failure: An error message should be visible
            error_message_container = driver.find_element(By.CSS_SELECTOR, ".error-message-container")

            # Assert that the specific failure message for being locked out is displayed
            expected_fail_msg = "Epic sadface: Sorry, this user has been locked out."
            assert expected_fail_msg in error_message_container.text, f"Failure message incorrect for {test_user}"

            print(f"Result: PASS. Login failed as expected.")

        except NoSuchElementException:
            pytest.fail(
                f"TEST FAILED: Login succeeded unexpectedly for user {test_user} (should have been locked out).")