

class Urls:
    BASE = "https://grocerymate.masterschool.com"
    HOME = f"{BASE}/"
    STORE = f"{BASE}/store"
    REGISTER = f"{BASE}/register"
    LOGIN = f"{BASE}/login"
    CART = f"{BASE}/cart"
    CHECKOUT = f"{BASE}/checkout"


class AgeRules:
    MIN_AGE = 18
    DOB_FORMAT_HINT = "DD-MM-YYYY"

class Products:
    DEFAULT_NAME = "Banana"
    DEFAULT_QTY = 1

class CheckoutData:
    STREET = "Test Street 1"
    CITY = "Berlin"
    POSTAL_CODE = "10115"

    CARD_NUMBER = "4242424242424242"
    CARD_NAME = "Test User"
    CARD_EXPIRY = "12.2030"
    CARD_CVV = "123"


class TestUsers:
    DEFAULT_PASSWORD = "TestPass!12345"

DEBUG_SLEEP = 0
