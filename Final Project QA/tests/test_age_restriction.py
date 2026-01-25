from datetime import date

from pages.age_gate_page import AgeGatePage
from utils.constants import Urls, AgeRules
from utils.helpers import date_of_birth_for_age_years, date_of_birth_entry_format


def test_user_exactly_18_can_pass_age_gate(driver):
    page = AgeGatePage(driver)


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
