from datetime import date
import time
import pytest

from pages.age_gate_page import AgeGatePage
from utils.constants import Urls, AgeRules, DEBUG_SLEEP
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
    time.sleep(DEBUG_SLEEP)

    page.go_to_store()
    time.sleep(DEBUG_SLEEP)

    assert page.wait_for_age_gate(), "Age gate did not appear on store page."

    if offset_days is not None:
        dob_exact = date_of_birth_for_age_years(date.today(), AgeRules.MIN_AGE)
        dob_variant = add_days(dob_exact, offset_days)
        dob_str = date_of_birth_entry_format(dob_variant, AgeRules.DOB_FORMAT_HINT)
    else:
        dob_str = custom_dob

    if dob_str:
        page.enter_dob(dob_str)

    page.submit()
    time.sleep(DEBUG_SLEEP)

    underage_text = page.get_underage_message_text()
    error_text = page.get_error_text()

    print("Underage msg:", underage_text)
    print("Error msg:", error_text)
    print("underage_message_visible():", page.underage_message_visible())

    if expected == "allowed":
        assert not underage_text, f"{case_name}: expected allowed but underage message shown"
    elif expected == "underage":
        assert underage_text, f"{case_name}: expected underage message"


    elif expected == "required":
        if error_text:
            assert True
        elif underage_text:
            pytest.xfail("BUG: Empty DOB is treated as underage instead of showing 'DOB is required'.")
        else:
            assert False, f"{case_name}: expected required DOB error, but no error/underage message was shown."

    elif expected == "invalid":
        if error_text:
            assert True
        elif underage_text:
            pytest.xfail("BUG: Invalid DOB format is treated as underage instead of showing 'invalid format' error.")
        else:
            assert False, f"{case_name}: expected invalid DOB error, but no error/underage message was shown."
