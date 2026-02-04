import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.age_gate_page import AgeGatePage
from pages.registration_gate_page import RegistrationGatePage
from pages.store_page import StorePage
from pages.star_rating_system_gate_page import StarRatingSystemGate
from pages.cart_page import CartPage
from pages.Checkout_page import CheckoutPage


from utils.constants import Urls, TestUsers
from utils.helpers import unique_email
from utils.constants import Urls, CheckoutData


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
    email = unique_email("grocerymate")
    password = TestUsers.DEFAULT_PASSWORD
    reg.register(full_name=full_name, email=email, password=password)

    driver.get(Urls.CART)
    CartPage(driver).click_buy_now()

    CheckoutPage(driver).complete_checkout(
        street=CheckoutData.STREET,
        city=CheckoutData.CITY,
        postal=CheckoutData.POSTAL_CODE,
        number=CheckoutData.CARD_NUMBER,
        name=CheckoutData.CARD_NAME,
        exp=CheckoutData.CARD_EXPIRY,
        cvv=CheckoutData.CARD_CVV,
    )

    driver.get(Urls.STORE)
    StorePage(driver).open_first_product()  # we’ll add this method


@pytest.fixture
def star_page(driver, purchased_product):
    return StarRatingSystemGate(driver)
