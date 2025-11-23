#core selenium components
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of all test credentials provided by the website (username, expected_success)
SAUCE_USERNAMES = [
    ("standard_user", True),            # Expected Success
    ("locked_out_user", False),         # Expected Failure
    ("problem_user", True),             # Expected Success (UI glitch expected)
    ("performance_glitch_user", True)
]


# --- 2. THE DRIVER FIXTURE ---
@pytest.fixture(scope="session")
def browser_driver():
    """
    PyTest Fixture: Initializes the Chrome WebDriver once per session.
    This handles the setup (launch) and teardown (quit) automatically.
    """
    print("\n--- Setting up WebDriver Fixture ---")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
    driver.maximize_window()

    # 'yield' passes control to the test function that requests this fixture.
    yield driver

    # Teardown: This code runs after ALL tests that used this fixture are done.
    print("\n--- Tearing down WebDriver Fixture ---")
    driver.quit()


# --- 3. PARAMETERIZATION HOOK ---
def pytest_generate_tests(metafunc):
    """
    PyTest Hook: Automatically feeds the data from SAUCE_USERNAMES into the
    test function defined in task_2_parameterized_test.py.
    """
    if "test_user" in metafunc.fixturenames:
        # Map the list of tuples to the test function parameters
        metafunc.parametrize("test_user, expected_success", SAUCE_USERNAMES)