import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.age_gate_page import AgeGatePage
from pages.registration_gate_page import RegistrationGatePage
from pages.store_page import StorePage
from pages.star_rating_system_gate_page import StarRatingSystemGate
from pages.Checkout_page import CheckoutPage

from utils.constants import Urls, TestUsers, CheckoutData
from utils.helpers import unique_email, unique_full_name


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(0)
    yield drv
    drv.quit()


def go_to_shop_and_pass_age_gate(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/store']"))
    ).click()
    AgeGatePage(driver).pass_age_gate_if_present()


@pytest.fixture
def purchased_product(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(Urls.STORE)
    AgeGatePage(driver).pass_age_gate_if_present()

    reg = RegistrationGatePage(driver)

    reg.open_registration_via_add_to_cart()

    password = TestUsers.DEFAULT_PASSWORD

    registered_email = None

    for _ in range(3):
        full_name = unique_full_name("Test User")
        email = unique_email("grocerymate")

        reg.register(full_name=full_name, email=email, password=password)

        try:
            wait_short = WebDriverWait(driver, 5)
            wait_short.until(
                lambda d: reg.is_error_visible() or reg.is_login_form_visible() or (reg.get_success_text().strip() != "")
            )
        except TimeoutException:
            continue

        if reg.is_error_visible():
            error = reg.get_error_text().lower()
            if "already" in error and "exist" in error:
                continue
            raise AssertionError(f"Registration failed: {reg.get_error_text()}")

        success = reg.get_success_text().lower()
        if "successful" in success or "please log in" in success or reg.is_login_form_visible():
            registered_email = email
            break

    if registered_email is None:
        raise AssertionError("Unable to register a unique user for the test.")

    driver.get(Urls.CHECKOUT)

    if "/auth" in driver.current_url:

        reg.login(email=registered_email, password=password)

        try:
            WebDriverWait(driver, 10).until_not(EC.url_contains("/auth"))
        except TimeoutException:
            print("DEBUG still on /auth, error text:", reg.get_error_text())
            raise AssertionError("Login failed; still on /auth after login.")


    go_to_shop_and_pass_age_gate(driver)


    StorePage(driver).add_first_product_to_cart()
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