Preconditions
	•	User is on checkout page with at least one product in cart.

Steps to Reproduce (Bug A)
	1.	Go to store, add a product to cart.
	2.	Navigate to /checkout.
	3.	Increase quantity until Product Total ≥ 20€.
	4.	Observe Shipment = 0€.
	5.	Decrease quantity until Product Total < 20€.
	6.	Observe Shipment remains 0€.

Expected Result
	•	When Product Total drops below 20€, Shipment becomes 5€.

Actual Result
	•	Shipment stays 0€ even when Product Total is below 20€.

Severity
	•	High (pricing error: user gets free shipping incorrectly)

