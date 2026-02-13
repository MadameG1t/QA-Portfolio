from datetime import date
from datetime import timedelta
import time


def date_of_birth_for_age_years(today: date,years: int):

    try:
        return today.replace(year=today.year - years)
    except ValueError:
        return today.replace(month=2,day=28,year=today.year - years)

def unique_full_name(prefix="Test User"):
    return f"{prefix} {int(time.time())}"

def date_of_birth_entry_format(d:date,fmt: str = "DD-MM-YYYY"):

    if fmt == "DD-MM-YYYY":
        return d.strftime("%d-%m-%Y")
    if fmt == "YYYY-MM-DD":
        return d.strftime("%Y-%m-%d")
    if fmt == "MM/DD/YYYY":
        return d.strftime("%m/%d/%Y")
    return d.strftime("%d-%m-%Y")

def add_days(d: date, days: int) -> date:
    return d + timedelta(days=days)

def unique_email(prefix="qa"):
    return f"{prefix}_{time.time_ns()}@example.com"
