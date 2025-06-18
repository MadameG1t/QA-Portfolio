**Test Plan for Webshop**

### **1. Analyze the Product**

**Objective**

**What is the objective?**

The objective of the webshop is for users to buy grocery store products online and get them delivered at home. 
The addition of the new features allows the product to be delivered according to standarized rules for alcohol consumption aka age restriction.
We want to make sure that according to the German rules and regulations, we need people below 16 years of age to be unable to purchase alcohol,
so we need to add this feature to the website. 
Deliver within the country and abroad incurring shipping cost and allow the users to rate the products accordingly, because 
we see a lot of users stopping the process because users see shipping prices and assume it is a standard and decide to not buy.

**User Base**

**Who will the product be used by? Who are your user stakeholders?**

The product will be used by existing and new users of the webshop platform, including individuals aged 16 and above. 
Our main user based are adults, our average user may be 25 years old, but we have from 18 and above registered users. We may have users
that are minors, so we need to make a distinction to make sure minors dont purchase alcohol.
(try to Identify the stakeholders for this website)

**Hardware and Software Specifications**

- **Hardware Requirements:**
    - Devices: PCs, laptops, smartphones, tablets
    - Specifications: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
    - Operating Systems: testing will be only performed in MacOS. 
    - Browsers: testing will be only perform in Chrome.
    - Dependencies: Backend services, third-party ad services, payment gateways

**Product Functionality**

**What is the functionality of the product? Existing and to be added functionality.**
(funcitonality is what has been tested before, new functionality is what is to be testes)

The functionality of the product is to sell consumable products for daily life, food, drinks and home supplies. 
The existing functionality considers the selection of products, the birth date entry to confirm age above 16, 
adding a rating from 1 to 5 stars to the product, registering user and have favourite items saved. 

### **2. Design the Test Strategy**

**Scope of Testing**

- **In Scope: Which functionalities are in scope of testing?**
    - Age verification for alcohol purchases without an account created.
    - Product rating system.
    - Shipping cost charges.
- **Out of Scope: What is out of scope for testing?** (add the old funcionalities to the out of scope)
    - Backend database operations not affecting the user interface.
    - user interface and product aesthetical design.
    - availability of products.
    - Log in/ registration 

**Type of Testing**

**What types of testing is necessary for the new functionalities?**

- Functional Testing : to ensure age gate works as intended. Crucial to verify the systems ability to identify users age
and grant or deny access accordingly. Verify users can submit ratings, view ratings and calculate the average rating correctly.
Valid and invalid inputs for shipping cost test. Verify calculation of shipping cost according to postal code, national and international.

- non-functional testing:


Out of scope:

regression testing:


- Usability Testing : This involves evaluating how intuitive the rating system is to the user. Is it complex or easy answer?
- Mobile testing : verify that the products funcitonality isn't affected by mobile format.
- Acceptance testing : testing from the perspective of the end user aka Stakeholders to ensure verification system meets their specific requirements
for age verification, for rating a product and for shipping cost. 

**Risks and Issues**

(what are some problems that I may run into? once I am automating, add what went wrong and what could be done better. I anticipate I will run problems with cookies. Age verification window wont come after loeading the website again.)

- **Delays in development**
    - Mitigation: Implement a buffer period in the schedule.
- **Lack of test data**
    - Mitigation: Create mock data sets for testing purposes.
- **Resource unavailability**
    - Mitigation: Identify backup resources.

**Test Logistics**

- **Jane Smith** - Test Manager
- **Gretchen Schadebrodt** - QA Engineer (Functional and Regression Testing)
- **Alice Johnson** - QA Engineer (Performance and Security Testing)
- **Robert Brown** - QA Engineer (Usability Testing)
- **Maria Garcia** - End User for UAT

### **3. Define Test Objectives**

**Objectives and Outcomes**

- **Functionality:** All features perform correctly according to specifications. Ensure the three new features work as intended.
Ratings can be submitted, underaged people cannot purchase products, shipping cost work according to post code. With the result that
we use local laws and we give more value to the customer.
- **GUI:** The interface is intuitive, responsive, and free of defects. Verify that company standards are being used.
- **Performance:** The platform meets performance benchmarks under load.
- **Security:** No significant vulnerabilities are detected.
- **Usability:** Users can navigate and use the platform easily. (this wont be applicable to this exercise)

### **4. Define Test Criteria**

**Suspension Criteria**

- Testing will be suspended if critical defects are found that block further testing.
- Lack of necessary resources or test environment failures.

**Exit Criteria**

- All planned tests have been executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- Performance metrics meet the defined standards.
- Security vulnerabilities have been identified and addressed.
- User acceptance testing has been completed, and sign-off has been obtained.

### **5. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome), operating systems (macOS)
- **Infrastructure:** Test environments, automation tools, performance testing tools

### **6. Plan Test Environment**

(give a bit of information of how, I can use google research or chatgpt to see what this process could look like, how do
we move between test environments) Who is testing what on which environment? 
- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

### **7. Schedule and Estimation**
(update it to 2025, its a fantasy game, maybe more realistic hours)
| Activity | Start Date | End Date | Environment | Responsible Person | Estimated Effort |
| --- | --- | --- | --- | --- | --- |
| Test Planning | 01/08/2024 | 05/08/2024 | All | Test Manager | 20 hours |
| Test Case Design | 06/08/2024 | 15/08/2024 | All | QA Team | 40 hours |
| Unit Testing | 16/08/2024 | 25/08/2024 | DEV | Development Team | 60 hours |
| Integration Testing | 26/08/2024 | 30/08/2024 | TEST | QA Team | 30 hours |
| System Testing | 01/09/2024 | 10/09/2024 | TEST | QA Team | 80 hours |
| Regression Testing | 11/09/2024 | 15/09/2024 | TEST | QA Team | 40 hours |
| Performance Testing | 16/09/2024 | 18/09/2024 | TEST | QA Team | 20 hours |
| Security Testing | 19/09/2024 | 21/09/2024 | TEST | QA Team | 20 hours |
| UAT | 22/09/2024 | 30/09/2024 | ACC | End Users | 50 hours |
| Production Release | 01/10/2024 | 01/10/2024 | PROD | DevOps Team | 10 hours |

### **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**
