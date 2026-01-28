from pages.registration_gate_page import RegistrationGatePage
from utils.helpers import unique_email
from utils.constants import TestUsers


def test_user_can_register_successfully(driver):
    page = RegistrationGatePage(driver)

    page.open()
    page.open_registration_via_add_to_cart()

    full_name = "Test User"
    email = unique_email("grocerymate")
    password = TestUsers.DEFAULT_PASSWORD
    page.register(full_name, email, password)

    assert not page.is_error_visible(), f"Registration failed: {page.get_error_text()}"



