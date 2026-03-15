QA Automated Test Suite
Automated end‑to‑end tests for the Market Mate (GroceryMate) web application.

This suite covers core user flows such as cart behavior, shipping cost calculation, age restrictions, star ratings, and general UI interactions.
The project uses Python, Selenium WebDriver, and pytest.

Test Structure Overview
Features covered:
• Age gate / age restriction
• Shopping cart & checkout
• Shipping cost calculation
• Star rating & review system
• Product purchase logic
• Utility helpers and page object model (POM)


Running the Test Suite
Install dependencies:
pip install -r requirements.txt

Run all tests:
pytest -q

Run a specific file:
pytest tests/test_shipping_cost.py -q

Run with browser visible (if headless mode is disabled):
pytest --headed


Known Bugs & XFAIL Tests:

Some tests expose verified bugs in the application.
Instead of failing the entire test suite, these tests are marked as XFAIL (expected failure) using:


@pytest.mark.xfail(reason="BUG: <description>")
These tests will run, but even if they fail, pytest will treat the failure as expected and will not produce a failing exit code.

Current XFAIL Tests
1. Shipping Cost Module
Test:
test_removing_item_recalculates_shipping

Bug:
Shipping cost does not recalculate after removing an item from the cart.
Expected: total drops below 20 → shipping becomes 5€
Actual: shipping stays at 0€

Test:
test_shipping_recalculates_when_total_drops_below_20

Bug:
Shipping cost stays at 0€ even after quantity reduction brings the total below 20€.

Both issues confirm inconsistent shipping recalculation logic in cart updates.

2. Age Gate Module
Test:
test_age_gate_cases[empty_dob]

Bug:
Empty date of birth is incorrectly treated as “underage” instead of returning
"Date of birth is required".

Test:
test_age_gate_cases[invalid_dob]

Bug:
Invalid date format is flagged as “underage” instead of
"Invalid date format".

These tests are marked xfail until the frontend validation is fixed.

Test Pass/Fail Philosophy
• A PASS verifies expected, correct application behavior.
• A FAIL indicates a regression or new defect.
• An XFAIL identifies known bugs that development has not yet addressed.
• An XPASS (unexpected pass) signals a bug is likely fixed and the test should be updated.

This strategy maintains stability in CI pipelines while still exposing real defects during development.

Project Structure 


Final_Project_QA/
│
├── pages/                  
├── tests/                  
│   ├── test_shipping_cost.py
│   ├── test_age_restriction.py
│   ├── test_star_rating.py
│   └── ...
├── utils/                 
├── drivers/             
├── requirements.txt
└── README.md       

Contributing
When adding new tests:

Follow the Page Object Model structure
Keep tests isolated and deterministic
Use XFAIL for confirmed bugs
Add comments describing verification points
Ensure CI remains stable