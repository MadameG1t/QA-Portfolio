# BUG REPORT – Age Gate: Invalid DOB Format Treated as Underage

## Bug ID
AGE-002

## Title
Invalid DOB format is treated as "Underage" instead of showing format validation error.

## Environment
- Website: https://grocerymate.masterschool.com
- Browser: Chrome
- Automation: Selenium + Pytest
- Test Case: test_age_gate_cases[invalid_dob]

## Preconditions
User navigates to the Store page and Age Verification modal appears.

## Steps to Reproduce
1. Open Store page.
2. Wait for Age Verification popup.
3. Enter invalid DOB format (e.g., 13/25/2008).
4. Click "Confirm".

## Expected Result
An error message appears:
"Invalid date format" or similar validation message.

## Actual Result
System displays underage message instead.

## Severity
Medium

## Priority
High

## Status
Open

## Notes
System does not validate date format before performing age comparison.