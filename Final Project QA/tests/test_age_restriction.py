from datetime import date

from pages.age_gate_page import AgeGatePage
from utils.constants import Urls, AgeRules
from utils.helpers import date_of_birth_for_age_years, date_of_birth_entry_format


def test_user_exactly_18_can_pass_age_gate(driver):
    page = AgeGatePage(driver)
    page.open(Urls.SHOP)
    dob_date = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
    dob_str = date_of_birth_entry_format(dob_date, AgeRules.DOB_FORMAT_HINT)
    page.enter_dob(dob_str)
    page.submit()

    assert page.driver.current_url != Urls.HOME


def test_user_just_below_18_cannot_pass_age_gate(driver):
    pass

def test_user_below_17_cannot_pass_age_gate(driver):
    pass

def test_user_above_18_can_pass_age_gate(driver):
    pass

def test_user_dob_not_entered_cannot_pass_age_gate(driver):
    pass

def test_user_invalid_dob_cannot_pass_age_gate(driver):
    pass
