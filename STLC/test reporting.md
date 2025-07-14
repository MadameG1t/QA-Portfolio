This document contains two example scenarios tested.


### Scenario 1: Valid Date of Birth

As a user of Grocerymate, I am able to purchase alcohol if I'm 18 years old.

| Step# | Action                        | Expected outcome                                                                                   | OK/NOK | URL                      | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to login page Grocerymate     | Login page appears                                                                                  | OK     | [https://grocerymate.masterschool.com/](https://grocery.masterschool.com/) |               |
| 3d    | Write gschadebrodtz@gmail.com as e-mail address |                                                                                                     |        |                          |               |
| 3e    | Password is 'h3ll0Fr3sh' |                                                                                                     |        |                          |               |
| 4     | Click sign up                 | You are directed to the login page. The e-mail and password are filled automatically                | OK     |                          |               |
| 5     | Click on log in               | You are successfully logged in                                                                      | OK     |                          |               |                                                                                                 |        |                          |               |
| 3b    | Fill 03-04-2007 as Date of Birth |                                                                                                     |        |                          |               |
| 3c    | Age verification Successful       |  OK                                                                                                   |        |                          |               |


![image](<img width="1170" height="2532" alt="IMG_0465" src="https://github.com/user-attachments/assets/79535397-fac3-45e7-801e-9b1319d5aaff" />
)
![image](<img width="1170" height="2532" alt="IMG_0466" src="https://github.com/user-attachments/assets/f3c44225-2dad-4997-95e7-8857e4c37ac5" />
)
![image](<img width="1170" height="2532" alt="IMG_0469" src="https://github.com/user-attachments/assets/7e05ce07-8820-4ba0-bfa2-50a9883c677e" />
)
![image](<img width="1170" height="2532" alt="IMG_0470" src="https://github.com/user-attachments/assets/e429406b-aea9-4f14-ab73-7da5a88f2ea3" />
)
![image](<img width="1170" height="2532" alt="IMG_0471" src="https://github.com/user-attachments/assets/939a943d-63fe-4021-9b51-127ba0b50077" />)


### Scenario 2: Invalid Date of Birth

As a user of FindMate, I am not able to sign up when I register with an invalid Date of Birth.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page FindMate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://findmate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'InputValidationTest' as username |                                                            |        |                                                    |                             |
| 3b    | Fill 19-08-1820 as Date of Birth     |                                                            |        |                                                    |                             |
| 3c    | Write 'This is my Bio'               |                                                            |        |                                                    |                             |
| 3d    | Write karin@faculty.masterschool.com as e-mail address |                                                            |        |                                                    |                             |
| 3e    | Password is 'RandomPassword1'        |                                                            |        |                                                    |                             |
| 4     | Click sign up                        | You cannot be 200 years old, so I expect an error message  | NOK    |                                                    | [https://github.com/software-engineering-ms/example-portfolio/issues/2](https://github.com/software-engineering-ms/example-portfolio/issues/2) |
