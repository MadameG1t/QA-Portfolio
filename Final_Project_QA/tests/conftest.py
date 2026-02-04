import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.age_gate_page import AgeGatePage
from pages.registration_gate_page import RegistrationGatePage
from pages.store_page import StorePage
from pages.star_rating_system_gate_page import StarRatingSystemGate
from pages.Checkout_page import CheckoutPage

from utils.constants import Urls, TestUsers, CheckoutData


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

    email = "gschadebrodtz@gmail.com"
    password = "899b5185a70d"
    reg.switch_to_login()
    reg.login(email=email, password=password)

    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(RegistrationGatePage.AUTH_MODAL)
    )

    driver.get(Urls.STORE)
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
