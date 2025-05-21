## The assignment

****Write down which critical questions you can ask as a tester. Think of at least 3 questions per new feature. In the next session we will discuss these questions; after this you will receive the details of the requirements. 

## **The software**

You will test a webshop, which can be found here: https://grocerymate.masterschool.com/

The webshop has the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favourites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

**You are going to test the new developed features. The new features are written below.**

## New features

### **1. Product Rating System**

**Requirement:** Users should be able to rate products with a 5-star system and have the option to add written feedback.

Questions:

- At what point of the process will rating be available, after purchase, simply login in to rate a past order?
- where should the rating a product be? in a separate website, in the purchase website in a follow up email to the consumer requesting for feedback?
- Will the written feedback be public on the website, or will it be an internal feedback for the company?
- if the feedback is requested by email, should the email be sent a couple of days after it has been confirmed the user received the purchase?

**Detailed requirement:** After purchasing an item, the system should send an email to users requesting to rate the product. Users should have the option to choose stars in a 5-star system and leave written feedback.

*** according to the website there is not email involved. In this case is after purchasing the item, user should be able to write the feedback. 

### **2. Age Verification for Alcoholic Products**

**Requirement:** Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions**:

1. How should the age verification be implemented? (e.g., date of birth input)
2. What format should the date of birth be in? (e.g., MM/DD/YYYY)
3. What error message should be displayed if the user is under 18?
4. Are there any specific legal disclaimers or privacy notices required for age verification?

detailed requirement: The user should get a modal when navigating the alcoholic products category. The modal should ask for date of birth in the format dd.mm.yyyy to verify users age eligibility of 18+. User must input their age before accessing the alcoholic products. If user is underaged, he wont be allowed to access the alcohol section and will receive an error message.

### **3. Shipping Cost Changes (send this done to Marina on Slack)**

**Requirement:** Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.
