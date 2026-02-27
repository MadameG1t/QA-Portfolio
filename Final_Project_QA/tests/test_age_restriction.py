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

FAIL_KNOWN_BUGS = True

KNOWN_BUGS = {
    "empty_dob": "BUG: Empty DOB is treated as underage instead of showing 'DOB is required'.",
    "invalid_dob": "BUG: Invalid DOB format is treated as underage instead of showing 'invalid format' error.",
}


def _bug_outcome(case_name: str, *, dob: str, underage_text: str, error_text: str) -> None:

    msg = (
        f"{KNOWN_BUGS.get(case_name, 'Known bug')}\n"
        f"Case: {case_name}\n"
        f"DOB entered: {repr(dob)}\n"
        f"Underage message: {repr(underage_text)}\n"
        f"Error message: {repr(error_text)}"
    )
    if FAIL_KNOWN_BUGS:
        pytest.fail(msg)
    else:
        pytest.xfail(msg)


@pytest.mark.parametrize(
    "case_name, offset_days, custom_dob, expected",
    AGE_CASES,
    ids=[c[0] for c in AGE_CASES],
)
def test_age_gate_cases(driver, case_name, offset_days, custom_dob, expected):
    page = AgeGatePage(driver)

    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")

    page.open(Urls.HOME)
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

    if expected == "allowed":
        assert not underage_text, f"{case_name}: expected allowed but underage message shown: {underage_text!r}"

    elif expected == "underage":
        assert underage_text, f"{case_name}: expected underage message"

    elif expected == "required":

        if error_text:
            assert True
        elif underage_text:
            _bug_outcome(case_name, dob=dob_str, underage_text=underage_text, error_text=error_text)
        else:
            pytest.fail(
                f"{case_name}: expected required DOB error, but no error/underage message was shown.\n"
                f"DOB entered: {repr(dob_str)}"
            )

    elif expected == "invalid":

        if error_text:
            assert True
        elif underage_text:
            _bug_outcome(case_name, dob=dob_str, underage_text=underage_text, error_text=error_text)
        else:
            pytest.fail(
                f"{case_name}: expected invalid DOB error, but no error/underage message was shown.\n"
                f"DOB entered: {repr(dob_str)}"
            )

    else:
        pytest.fail(f"Unknown expected outcome '{expected}' for case '{case_name}'.")