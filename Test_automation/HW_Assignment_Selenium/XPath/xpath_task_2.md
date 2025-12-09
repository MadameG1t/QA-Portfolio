# Write the XPath for the highlighted icon/button given in the image below.

//div[contains(@class, 'headerIcon')]

# Write the XPath of all input fields (Email address, Password), sign in button, 
# Create a new account link, and Go to Home link

email = //input[@type='email' and @placeholder='Email Address']
password = //input[@type='password' and @placeholder='Password']
sign in button = //button[contains(@class, 'submit-btn')]
'create a new account' link = //a[contains(@class, 'switch-link') and @href='#!']
'Go to Home' link = //a[contains(@class, 'home-link') and @href='#!']

# Now, on the same link as in Part 2, click on Create a new account, you will see the following UI:
# Write the XPath for all input fields (Full Name, Email address, Password), Sign Up button.

Full Name = //input[@type='text' and @placeholder='Full Name']
Email address = //input[@type='email' and contains(@placeholder, 'Email address')]
Password = //input[@type='password' and @placeholder='Password']
Sing Up button = //button[contains(@class, 'submit-btn') and text()='Sign Up']


