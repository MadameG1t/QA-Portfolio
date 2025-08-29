This document contains test cases described in test plan.

### Scenario 1: Valid Date of Birth - verify users with exact 18 years old.

As a user of Grocerymate, I am able to purchase alcohol if I'm 18 years old.

| Step# | Action                                                           | Expected outcome                                                                     | OK/NOK | URL                                                                        | Link to issue |
|-------|------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                                     | Login page appears                                                                   | OK     | [https://grocerymate.masterschool.com/](https://grocery.masterschool.com/) |               |
| 3d    | Write gschadebrodtz@gmail.com as e-mail address                  |                                                                                      |        |                                                                            |               |
| 3e    | Password is 'h3ll0Fr3sh'                                         |                                                                                      |        |                                                                            |               |
| 4     | Click sign up                                                    | You are directed to the login page. The e-mail and password are filled automatically | OK     |                                                                            |               |
| 5     | Click on log in                                                  | You are successfully logged in                                                       | OK     |                                                                            |               |                                                                                                 |        |                          |               |
| 3b    | Fill 03-04-2007 as Date of Birth same as testing date 03-04-2025 |                                                                                      |        |                                                                            |               |
| 3c    | Age verification Successful                                      | A modal pop up window confirms Im of age                                             | OK     |                                                                            |               |

![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/7313f2c9-b90d-4c6c-8bc4-41e9db6d73e5" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/20676b28-5b45-4c85-987c-0fbd3f3111be" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/e311a6df-05aa-4cf7-b7d1-0caeed6dd350" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/7539a008-b782-4ca1-82b5-5211b25da787" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/3c5a806b-b801-477d-ae0b-d9fa9a83acad" />

### Scenario 2: Valid Date of Birth - verify users above 18 years old.

As a user of Grocerymate, I am able to purchase alcohol if I'm 18 years old.

| Step# | Action                                          | Expected outcome                                                                     | OK/NOK | URL                                                                        | Link to issue |
|-------|-------------------------------------------------|--------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                    | Login page appears                                                                   | OK     | [https://grocerymate.masterschool.com/](https://grocery.masterschool.com/) |               |
| 3d    | Write gschadebrodtz@gmail.com as e-mail address |                                                                                      |        |                                                                            |               |
| 3e    | Password is 'h3ll0Fr3sh'                        |                                                                                      |        |                                                                            |               |
| 4     | Click sign up                                   | You are directed to the login page. The e-mail and password are filled automatically | OK     |                                                                            |               |
| 5     | Click on log in                                 | You are successfully logged in                                                       | OK     |                                                                            |               |                                                                                                 |        |                          |               |
| 3b    | Fill 03-04-2007 as Date of Birth                |                                                                                      |        |                                                                            |               |
| 3c    | Age verification Successful                     | A modal pop up window confirms Im of age                                             | OK     |                                                                            |               |

![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/7313f2c9-b90d-4c6c-8bc4-41e9db6d73e5" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/20676b28-5b45-4c85-987c-0fbd3f3111be" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/e311a6df-05aa-4cf7-b7d1-0caeed6dd350" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/7539a008-b782-4ca1-82b5-5211b25da787" />
![image]
<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/3c5a806b-b801-477d-ae0b-d9fa9a83acad" />

### Scenario 3: Invalid Date of Birth - verify users below 17 years old.

As a user of GroceryMate, I am not able to purchase alcohol if Im a little under 18 years old.

| Step# | Action                           | Expected outcome                                                                      | OK/NOK | URL                                                                         | Link to issue |
|-------|----------------------------------|---------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate     | Login page appears                                                                    | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                 | You are directed to the sign up page                                                  | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Age verification modal' |                                                                                       |        |                                                                             |               |
| 3b    | Fill 13-09-2007 as Date of Birth |                                                                                       |        |                                                                             |               |                                 |                             |
| 4     | Error Message                    | You are underage. You can still browse the site but you cannot view alcohol products. | OK     |                                                                             |               |

<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/57438c87-3d05-4ce7-9dfb-a6ac9da717e2" />

<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/b15886ba-1d62-4a30-888c-9bac551255ca" />

### Scenario 4: Invalid Date of Birth - user younger than 18 years old by one day.

As a user of GroceryMate, I am not able to purchase alcohol if one day younger than 18 years old.

| Step# | Action                                                    | Expected outcome                                                                      | OK/NOK | URL                                                                         | Link to issue |
|-------|-----------------------------------------------------------|---------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                              | Login page appears                                                                    | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                                          | You are directed to the sign up page                                                  | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Age verification modal'                          |                                                                                       |        |                                                                             |               |
| 3b    | Fill 26-08-2007 as Date of Birth for test date 25-08-2025 |                                                                                       |        |                                                                             |               |                                 |                             |
| 4     | Error Message                                             | You are underage. You can still browse the site but you cannot view alcohol products. | OK     |                                                                             |               |

<img width="1170" height="2532" alt="IMG_0828" src="https://github.com/user-attachments/assets/62961462-8280-4c44-9edb-bd23f61d16d0" />
<img width="1170" height="2532" alt="IMG_0829" src="https://github.com/user-attachments/assets/10b0a7cf-4f64-42c1-b118-394efae59f75" />

### Scenario 5: Valid Date of Birth. User exact 18 years old.

As a user of GroceryMate, I am able to purchase alcohol if I turned 18 years old today.

| Step# | Action                                                    | Expected outcome                                                                      | OK/NOK | URL                                                                         | Link to issue |
|-------|-----------------------------------------------------------|---------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                              | Login page appears                                                                    | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                                          | You are directed to the sign up page                                                  | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Age verification modal'                          |                                                                                       |        |                                                                             |               |
| 3b    | Fill 25-08-2007 as Date of Birth for test date 25-08-2025 |                                                                                       |        |                                                                             |               |                                 |                             |
| 4     | Error Message                                             | You are underage. You can still browse the site but you cannot view alcohol products. | OK     |                                                                             |               |

<img width="1170" height="2532" alt="IMG_0830" src="https://github.com/user-attachments/assets/f326cf4a-f216-4d04-afd8-1616cc283ebc" />
<img width="1170" height="2532" alt="IMG_0831" src="https://github.com/user-attachments/assets/1f1177b9-824e-459d-a7b0-42629f16b727" />

### Scenario 6: Invalid Date of Birth : user no entry for age.

| Step# | Action                                 | Expected outcome                                                  | OK/NOK | URL                                                                         | Link to issue |
|-------|----------------------------------------|-------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate           | Login page appears                                                | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                       | You are directed to the sign up page                              | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Age verification modal'       |                                                                   |        |                                                                             |               |
| 3b    | Leave blank the age verification modal |                                                                   |        |                                                                             |             |                                 |                             |
| 4     | Error Message                          | Invalid input. Please enter a date of birth in DD-MM-YYYY format. | NOK    |                                                                             |https://github.com/MadameG1t/QA-Portfolio/issues/3  |

### Scenario 7: Invalid Date of Birth : user entry invalid format.

| Step# | Action                            | Expected outcome                                                  | OK/NOK | URL                                                                         | Link to issue |
|-------|-----------------------------------|-------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate      | Login page appears                                                | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                  | You are directed to the sign up page                              | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Age verification modal'  |                                                                   |        |                                                                             |               |
| 3b    | Enter invalid format "DD/MM/YYYY" |                                                                   |        |                                                                             |               |                                 |                             |
| 4     | Error Message                     | Invalid input. Please enter a date of birth in DD-MM-YYYY format. | NOK    | https://github.com/MadameG1t/QA-Portfolio/issues/4                          

### Scenario 8: Entry of a star rating system with comment.

| Step# | Action                                           | Expected outcome                               | OK/NOK | URL                                                                         | Link to issue |
|-------|--------------------------------------------------|------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                     | Login page appears                             | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                                 | You are directed to the sign up page           | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Star rating system and comment modal'   |                                                |        |                                                                             |               |
| 3b    | Select 5 stars and add a comment to the product. |                                                |        |                                                                             |               |                                 |                             |
| 4     | Star and comment                                 | My 5 star rating and a comment to the product. | NOK    | https://github.com/MadameG1t/QA-Portfolio/issues/5                          

<img width="1170" height="2532" alt="IMG_0783" src="https://github.com/user-attachments/assets/b8bae386-65da-4531-92c4-0724dfa4f675" />
<img width="1170" height="2532" alt="IMG_0784" src="https://github.com/user-attachments/assets/487f93f6-4caf-4552-bf0c-2f95f1b20b86" />

### Scenario 9: Verify user can delete star rating and comment entry.

| Step# | Action                                       | Expected outcome                             | OK/NOK | URL                                                                         | Link to issue |
|-------|----------------------------------------------|----------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                 | Login page appears                           | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                             | You are directed to the sign up page         | OK     | /auth                                                                       |               |
| 3a    | Select review on product.                    |                                              |        |                                                                             |               |
| 3b    | Deleting star and review given to a product. |                                              |        |                                                                             |               |                                 |                             |
| 4     | Modal message                                | Are you sure you want to delete this review? | OK     |

<img width="1170" height="2532" alt="IMG_0785" src="https://github.com/user-attachments/assets/53d0fc3f-f074-4861-a818-98dc0739aa73" />
<img width="1170" height="2532" alt="IMG_0786" src="https://github.com/user-attachments/assets/e8cc6fc3-8ff2-4b7e-b8fd-141727c4b7c9" />

### Scenario 10: Verify user can delete star rating and comment entry.

| Step# | Action                                         | Expected outcome                           | OK/NOK | URL                                                                         | Link to issue |
|-------|------------------------------------------------|--------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                   | Login page appears                         | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                               | You are directed to the sign up page       | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Start rating modal with 0 stars'      |                                            |        |                                                                             |               |
| 3b    | Give Zero star review and submitt your review. |                                            |        |                                                                             |               |                                 |                             |
| 4     | Error message                                  | Please rate the product from 1 to 5 stars. | OK     |

<img width="1170" height="2532" alt="IMG_0787" src="https://github.com/user-attachments/assets/82833b61-42b5-4d41-b810-bcc34a69bb57" />
<img width="1170" height="2532" alt="IMG_0788" src="https://github.com/user-attachments/assets/46c0d71e-951d-495e-860b-a0de80ba2ee5" />

### Scenario 11: Verify user can edit star rating and comment entry.

| Step# | Action                                                                | Expected outcome                                                 | OK/NOK | URL                                                                         | Link to issue |
|-------|-----------------------------------------------------------------------|------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                                          | Login page appears                                               | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                                                      | You are directed to the sign up page                             | OK     | /auth                                                                       |               |
| 3a    | Fill in 'Start rating modal with 1 to 5 stars and submit your rating. |                                                                  |        |                                                                             |               |
| 3b    | Select three dots next to the submitted rating and select edit.       |                                                                  |        |                                                                             |               |                                 |                             |
| 4     | edit                                                                  | Modal with star rating system and comment available for editing. | OK     |

<img width="1170" height="2532" alt="IMG_0789" src="https://github.com/user-attachments/assets/d39ab9fb-db8b-4a3b-bdd8-a6a04b29b7d8" />
<img width="1170" height="2532" alt="IMG_0790" src="https://github.com/user-attachments/assets/e8cdaf9c-f482-4c24-8809-4ecef32fe489" />
<img width="1170" height="2532" alt="IMG_0791" src="https://github.com/user-attachments/assets/04ea1985-9376-48aa-8c2f-b164e7ca5fdc" />

### Scenario 12: Verify Shipment fee is Zero for purchases equal to 20euros.

| Step# | Action                                                  | Expected outcome                                 | OK/NOK | URL                                                                         | Link to issue |
|-------|---------------------------------------------------------|--------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                            | Login page appears                               | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                                        | You are directed to the sign up page             | OK     | /auth                                                                       |               |
| 3a    | Select product and quantity                             |                                                  |        |                                                                             |               |
| 3b    | Shipment calculation for 20 euro basket should be Zero. |                                                  |        |                                                                             |               |                                 |                             |
| 4     | message at the bottom                                   | Free shipment if your purchase is 20 eu or more. | OK     |

<img width="1170" height="2532" alt="IMG_0794" src="https://github.com/user-attachments/assets/cd049e17-0526-41fc-b9e7-b06d74d18a62" />

### Scenario 13: Verify Shipment fee recalculation once an item is removed from the shopping cart.

| Step# | Action                                                         | Expected outcome                                 | OK/NOK | URL                                                                         | Link to issue |
|-------|----------------------------------------------------------------|--------------------------------------------------|--------|-----------------------------------------------------------------------------|---------------|
| 1     | Go to login page Grocerymate                                   | Login page appears                               | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on Sign up                                               | You are directed to the sign up page             | OK     | /auth                                                                       |               |
| 3a    | Select product and reduce the purchase quantity                |                                                  |        |                                                                             |               |
| 3b    | Shipment calculation for under 20 euro basket should be 5 euro |                                                  | NOK    | https://github.com/MadameG1t/QA-Portfolio/issues/6                          |               |                                 |                             | 
| 4     | message at the bottom                                          | Free shipment if your purchase is 20 eu or more. | OK     | 
