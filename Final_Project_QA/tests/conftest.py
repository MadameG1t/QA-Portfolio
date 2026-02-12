import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.age_gate_page import AgeGatePage
from pages.registration_gate_page import RegistrationGatePage
from pages.store_page import StorePage
from pages.star_rating_system_gate_page import StarRatingSystemGate
from pages.Checkout_page import CheckoutPage

from utils.constants import Urls, TestUsers, CheckoutData
from utils.helpers import unique_email


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(2)
    yield drv
    drv.quit()


@pytest.fixture
def purchased_product(driver):
    driver.get(Urls.STORE)
    AgeGatePage(driver).pass_age_gate_if_present()

    reg = RegistrationGatePage(driver)
    reg.open_registration_via_add_to_cart()

    full_name = "Test User"
    password = TestUsers.DEFAULT_PASSWORD

    # Retry registration with a truly unique email to avoid "already exists".
    for _ in range(3):
        email = unique_email("grocerymate")
        reg.register(full_name=full_name, email=email, password=password)
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located(RegistrationGatePage.AUTH_MODAL)
            )
            break
        except TimeoutException:
            error = reg.get_error_text().lower()
            if "already" in error and "exist" in error:
                continue
            raise
    else:
        raise AssertionError("Unable to register a unique user for the test.")

    driver.get(Urls.STORE)
    StorePage(driver).add_first_product_to_cart()
    driver.get(Urls.CHECKOUT)
    if "/auth" in driver.current_url:
        # If not logged in after registration, log in with the same credentials.
        reg.login(email=email, password=password)
        try:
            WebDriverWait(driver, 5).until(lambda d: "/auth" not in d.current_url)
        except TimeoutException:
            raise AssertionError("Login failed; still on /auth after login.")
        driver.get(Urls.CHECKOUT)
    CheckoutPage(driver).complete_checkout(
        street=CheckoutData.STREET,
        city=CheckoutData.CITY,
        postal=CheckoutData.POSTAL_CODE,
        number=CheckoutData.CARD_NUMBER,
        name=CheckoutData.CARD_NAME,
        exp=CheckoutData.CARD_EXPIRY,
        cvv=CheckoutData.CARD_CVV,
    )

    driver.get(Urls.PRODUCT_ORANGES)
    return True



@pytest.fixture
def star_page(driver, purchased_product):
    return StarRatingSystemGate(driver)
