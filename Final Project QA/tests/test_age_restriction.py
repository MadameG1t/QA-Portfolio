from datetime import date
import time
import pytest

from pages.age_gate_page import AgeGatePage
from utils.constants import Urls, AgeRules
from utils.helpers import date_of_birth_for_age_years, date_of_birth_entry_format, add_days

AGE_CASES = [
    ("exactly_18",     0,    None, "allowed"),
    ("just_under_18",  1,    None, "underage"),
    ("below_17",       400,  None, "underage"),
    ("above_18",       -1,   None, "allowed"),
    ("empty_dob",      None, "",   "required"),
    ("invalid_dob",    None, "13/25/2008", "invalid"),
]

@pytest.mark.parametrize("case_name, offset_days, custom_dob, expected",
                         AGE_CASES,
                         ids=[c[0] for c in AGE_CASES],
                         )
def test_age_gate_cases(driver, case_name, offset_days, custom_dob, expected):
    page = AgeGatePage(driver)
    page.open(Urls.HOME)
    time.sleep(3)
    page.go_to_store()
    time.sleep(3)

    if offset_days is not None:
        dob_exact = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
        dob_variant = add_days(dob_exact, offset_days)
        dob_str = date_of_birth_entry_format(dob_variant, AgeRules.DOB_FORMAT_HINT)
    else:
        dob_str = custom_dob

    if dob_str:
        page.enter_dob(dob_str)

    page.submit()
    time.sleep(3)

    if expected == "allowed":
        assert not page.underage_message_visible(), f"{case_name}: expected allowed but underage message shown"

    elif expected == "underage":
        assert page.underage_message_visible(), f"{case_name}: expected underage message"

    elif expected == "required":
        assert page.get_error_text(), f"{case_name}: expected required DOB error"

    elif expected == "invalid":
        assert page.get_error_text(), f"{case_name}: expected invalid DOB error"
"""
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

    assert page.underage_message_visible(), "Expected an underage warning message, but it was not shown."



def test_user_below_17_cannot_pass_age_gate(driver):
    pass

def test_user_above_18_can_pass_age_gate(driver):
    pass

def test_user_dob_not_entered_cannot_pass_age_gate(driver):
    pass

def test_user_invalid_dob_cannot_pass_age_gate(driver):
    pass
"""