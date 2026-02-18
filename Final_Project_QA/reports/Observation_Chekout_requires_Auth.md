Issue:
Navigation smoke test failed when accessing /checkout.

Expected:
User should land on /checkout.

Actual:
User was redirected to /auth.

Root Cause:
Checkout page is protected and requires authentication.
When accessed without login, the system redirects to the authentication page.

Resolution:
Test was updated to use authenticated fixture (purchased_product) before navigating to /checkout.

Result:
Navigation smoke test now passes consistently.