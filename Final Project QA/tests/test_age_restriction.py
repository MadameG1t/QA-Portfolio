from datetime import date
import time

from pages.age_gate_page import AgeGatePage
from utils.constants import Urls, AgeRules
from utils.helpers import date_of_birth_for_age_years, date_of_birth_entry_format, add_days


def test_user_exactly_18_can_pass_age_gate(driver):
    page = AgeGatePage(driver)
    page.open(Urls.HOME)
    time.sleep(3)
    page.go_to_store()
    time.sleep(3)
    dob_date = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
    dob_str = date_of_birth_entry_format(dob_date, AgeRules.DOB_FORMAT_HINT)
    page.enter_dob(dob_str)
    time.sleep(3)
    page.submit()
    time.sleep(0)

    assert page.age_gate_closed(),\
    "Expected age verification popup to close after entering valid DOB,but stayed open"


def test_user_just_below_18_cannot_pass_age_gate(driver):
    page = AgeGatePage(driver)
    page.open(Urls.HOME)
    time.sleep(3)
    page.go_to_store()
    time.sleep(3)
    dob_exact = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
    dob_under = add_days(dob_exact,1)
    dob_str = date_of_birth_entry_format(dob_under, AgeRules.DOB_FORMAT_HINT)
    page.enter_dob(dob_str)
    time.sleep(3)
    page.submit()
    time.sleep(3)

    assert page.age_gate_still_open(), "Expected underage user to be blocked (age gate stays open), but it closed."


def test_user_below_17_cannot_pass_age_gate(driver):
    pass

def test_user_above_18_can_pass_age_gate(driver):
    pass

def test_user_dob_not_entered_cannot_pass_age_gate(driver):
    pass

def test_user_invalid_dob_cannot_pass_age_gate(driver):
    pass
