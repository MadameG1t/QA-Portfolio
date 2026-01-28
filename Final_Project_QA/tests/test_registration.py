from pages.registration_gate_page import RegistrationGatePage
from utils.helpers import unique_email
from utils.constants import Urls, TestUsers


def test_user_can_register_successfully(driver):
    page = RegistrationGatePage(driver)

    page.open()
    page.go_to_registration_form()

    email = unique_email("grocerymate")
    password = TestUsers.DEFAULT_PASSWORD
    full_name = "Test User"

    page.register(full_name=full_name, email=email, password=password)

    assert not page.is_error_visible(), f"Registration failed: {page.get_error_text()}"
    assert not page.is_signup_button_visible(), "Sign Up form still visible; registration may not have completed."


