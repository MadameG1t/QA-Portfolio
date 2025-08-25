This document contains test cases described in test plan.

### Scenario 1: Valid Date of Birth - verify users with exact 18 years old.

As a user of Grocerymate, I am able to purchase alcohol if I'm 18 years old.

| Step# | Action                        | Expected outcome                                                                                   | OK/NOK | URL                      | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to login page Grocerymate     | Login page appears                                                                                  | OK     | [https://grocerymate.masterschool.com/](https://grocery.masterschool.com/) |               |
| 3d    | Write gschadebrodtz@gmail.com as e-mail address |                                                                                                     |        |                          |               |
| 3e    | Password is 'h3ll0Fr3sh' |                                                                                                     |        |                          |               |
| 4     | Click sign up                 | You are directed to the login page. The e-mail and password are filled automatically                | OK     |                          |               |
| 5     | Click on log in               | You are successfully logged in                                                                      | OK     |                          |               |                                                                                                 |        |                          |               |
| 3b    | Fill 03-04-2007 as Date of Birth same as testing date 03-04-2025|                                                                                                     |        |                          |               |
| 3c    | Age verification Successful       |  A modal pop up window confirms Im of age                                                                                                  |     OK   |                          |               |


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



### Scenario 1: Valid Date of Birth - verify users above 18 years old.

As a user of Grocerymate, I am able to purchase alcohol if I'm 18 years old.

| Step# | Action                        | Expected outcome                                                                                   | OK/NOK | URL                      | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to login page Grocerymate     | Login page appears                                                                                  | OK     | [https://grocerymate.masterschool.com/](https://grocery.masterschool.com/) |               |
| 3d    | Write gschadebrodtz@gmail.com as e-mail address |                                                                                                     |        |                          |               |
| 3e    | Password is 'h3ll0Fr3sh' |                                                                                                     |        |                          |               |
| 4     | Click sign up                 | You are directed to the login page. The e-mail and password are filled automatically                | OK     |                          |               |
| 5     | Click on log in               | You are successfully logged in                                                                      | OK     |                          |               |                                                                                                 |        |                          |               |
| 3b    | Fill 03-04-2007 as Date of Birth |                                                                                                     |        |                          |               |
| 3c    | Age verification Successful       |  A modal pop up window confirms Im of age                                                                                                  |     OK   |                          |               |


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


### Scenario 2: Invalid Date of Birth - verify users below 17 years old.

As a user of GroceryMate, I am not able to purchase alcohol if Im a little under 18 years old.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page Grocerymate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'Age verification modal'|                                                            |        |                                                    |                             |
| 3b    | Fill 13-09-2007 as Date of Birth     |                                                            |        |                                                    |                             |                                 |                             |
| 4     | Error Message                        | You are underage. You can still browse the site but you cannot view alcohol products.  | OK    |                                                    | |


<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/57438c87-3d05-4ce7-9dfb-a6ac9da717e2" />

<img width="1170" height="2532" alt="Image" src="https://github.com/user-attachments/assets/b15886ba-1d62-4a30-888c-9bac551255ca" />

### Scenario 2: Invalid Date of Birth

As a user of GroceryMate, I am not able to purchase alcohol if one day younger than 18 years old.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page Grocerymate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'Age verification modal'|                                                            |        |                                                    |                             |
| 3b    | Fill 26-08-2007 as Date of Birth for test date 25-08-2025     |                                                            |        |                                                    |                             |                                 |                             |
| 4     | Error Message                        | You are underage. You can still browse the site but you cannot view alcohol products.  | OK    |                                                    | |

<img width="1170" height="2532" alt="IMG_0828" src="https://github.com/user-attachments/assets/62961462-8280-4c44-9edb-bd23f61d16d0" />
<img width="1170" height="2532" alt="IMG_0829" src="https://github.com/user-attachments/assets/10b0a7cf-4f64-42c1-b118-394efae59f75" />

### Scenario 2: Valid Date of Birth

As a user of GroceryMate, I am able to purchase alcohol if I turned 18 years old today.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page Grocerymate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'Age verification modal'|                                                            |        |                                                    |                             |
| 3b    | Fill 25-08-2007 as Date of Birth for test date 25-08-2025     |                                                            |        |                                                    |                             |                                 |                             |
| 4     | Error Message                        | You are underage. You can still browse the site but you cannot view alcohol products.  | OK    |                                                    | |

<img width="1170" height="2532" alt="IMG_0830" src="https://github.com/user-attachments/assets/f326cf4a-f216-4d04-afd8-1616cc283ebc" />
<img width="1170" height="2532" alt="IMG_0831" src="https://github.com/user-attachments/assets/1f1177b9-824e-459d-a7b0-42629f16b727" />

### Scenario 2: Invalid Date of Birth : user no entry for age.



| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page Grocerymate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://grocerymate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'Age verification modal'|                                                            |        |                                                    |                             |
| 3b    | Leave blank the age verification modal     |                                                            |        |                                                    |                             |                                 |                             |
| 4     | Error Message                        | Invalid input. Please enter a date of birth in DD-MM-YYYY format.  | NOK    |   https://github.com/MadameG1t/QA-Portfolio/issues/3


<img width="1170" height="2532" alt="IMG_0832" src="https://github.com/user-attachments/assets/9c4417d6-dca4-4c55-bdcf-23ce854b3eb8" />
<img width="1170" height="2532" alt="IMG_0833" src="https://github.com/user-attachments/assets/1f8c5569-679a-4204-b563-ebace6196828" />


