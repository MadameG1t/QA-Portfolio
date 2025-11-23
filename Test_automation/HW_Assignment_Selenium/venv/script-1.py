
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Instantiate a webdriver object
driver = webdriver.Chrome()
time.sleep(2)#this is for demo purpose

#Navigate to a web page using get method
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)#this is for demo purpose

#request browser title
title = driver.title
print(driver.title)#print the title of the driver

#Implicit wait
driver.implicitly_wait(1000)

#Find element
text_box = driver.find_element(by=By.NAME,value="my-text")
submit_button=driver.find_element(by=By.CSS_SELECTOR,value="button")

#take action
text_box.send_keys("First Selenium Script")
time.sleep(3)

submit_button.click()
time.sleep(3)

