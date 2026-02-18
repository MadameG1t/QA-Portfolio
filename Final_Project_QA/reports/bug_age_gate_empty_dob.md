# BUG REPORT – Age Gate: Empty DOB Treated as Underage

## Bug ID
AGE-001

## Title
Empty Date of Birth is treated as "Underage" instead of showing validation error.

## Environment
- Website: https://grocerymate.masterschool.com
- Browser: Chrome
- Automation: Selenium + Pytest
- Test Case: test_age_gate_cases[empty_dob]

## Preconditions
User navigates to the Store page and Age Verification modal appears.

## Steps to Reproduce
1. Open Store page.
2. Wait for Age Verification popup.
3. Leave Date of Birth field empty.
4. Click "Confirm".

## Expected Result
An error message appears:
"DOB is required" or similar validation message.

## Actual Result
System displays underage message:
"You are underage. You can still browse the site..."

## Severity
Medium

## Priority
High

## Status
Open

## Notes
Validation logic does not differentiate between empty input and underage DOB.