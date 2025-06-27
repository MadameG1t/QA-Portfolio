
**Design of test cases, based on the new features added to our webshop product.**

**New Added Features**

### **1. Age Restriction for purchases**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify user exactly 16 years old.
        - **Input**: Date of Birth = (Today - 16 years)
        - **Expected Outcome**: Age verification successful.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify purchase eligibility for user just below 16 years old.
        - **Input**: Date of Birth = (Today - 16 years + 1 day)
        - **Expected Outcome**: Error message "You must be at least 16 years old to purchase a product."
3. **Equivalence Partitioning**:
    - **Test Case**: Verify aligibility for users below the age of 16.
        - **Input**: Date of Birth = (Today - 15 years)
        - **Expected Outcome**: Error message displayed.
4. **Equivalence Partitioning**:
    - **Test Case**: Verify eligibility of purchase for users above the age of 16.
        - **Input**: Date of Birth = (Today - 17 years)
        - **Expected Outcome**: You are of age.Now you can view and purchase products.
5. **Error Guessing**:
    - **Test Case**: Verify system behavior when Date of Birth is not entered.
        - **Input**: Date of Birth field left empty.
        - **Expected Outcome**: Error message "Date of Birth is required."
6. **Error Guessing**:
    - **Test Case**: Verify system behavior when an invalid Date of Birth format is entered.
        - **Input**: Date of Birth = "13/25/2008"
        - **Expected Outcome**: Error message "Invalid Date of Birth format. Please use DD-MM-YYYY."

### **2. 5 Star rating System**

**Test Design Techniques**: positive testing,negative testing,integration testing.

### Test Cases:

1. **Positive Testing**:
    - **Test Case**: Verify the user can submit one star review.
        - **Input**: Navigate to product and give 1 start rating.
        - **Expected Outcome**: one star review is stored and visible.
    - **Test Case**: Verify the user can submit two star review.
        - **Input**: Navigate to product and submit two star review.
        - **Expected Outcome**: two star review is stored and visible.
    - **Test Case**: Verify the user can submit three star review.
        - **Input**: Navigate to product and give three star reviews.
        - **Expected Outcome**: three star review is stored and visible.
    - **Test Case**: Verify the user can submit four star review.
        - **Input**: Navigate to product and submit a 4 star review.
        - **Expected Outcome**: four star review is stored and visible.
    - **Test Case**: Verify the user can submit five star review.
        - **Input**: Navigate to product and submit 5 star rating.
        - **Expected Outcome**: five star review is stored and visible.
    - **Test Case**: Verify the user can submit a written review.
        - **Input**: Navigate to product and submit a written review.
        - **Expected Outcome**: written review is stored and visible.
    - **Test Case**: Verify the user can edit a written feedback.
        - **Input**: Navigate to product and edit a written feedback.
        - **Expected Outcome**: edited feedback submitted and updated.
 - **Test Case**: Verify the user can delete a written feedback.
        - **Input**: Navigate to product and delete a written feedback.
        - **Expected Outcome**:  feedback has been successfully deleted.
   **Negative Testing**:
    - **Test Case**: Verify the webshop can handle a Zero-star rating as invalid.
        - **Input**: Navigate to product and find the 5 star rating option.
        - **Expected Outcome**: Error message " Data entry invalid. Please select stars to rate the product again."
  
2. **Integration testing**:
    - **Test Case**: Verify the rating system functions correctly by providing an average rating number.
        - **Input**: selecting a star rating.
        - **Expected Outcome**: Average star rating displayed in product browsing site.


### **3. Shipping Cost feature**

**Test Design Techniques**: Boundary Value Analysis (BVA), positive testing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify the system calculates a free shipping cost for purchases above $21.
        - **Input**: User check out total purchase amount.
        - **Expected Outcome**: Message displayed Your shipping fee for this purchase if free.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify the purchase amount for $19.
        - **Input**: Total purchase of products is $19.
        - **Expected Outcome**: This purchase has additional shipping cost. Purchases above $20 get free shipping.
     
3. Boundary value analysis for $20, what happens if you purchase $20?
          
3. Make sure that shipping prices adjust accordingly when an item is deleted.




