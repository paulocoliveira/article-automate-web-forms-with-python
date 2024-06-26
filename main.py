import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

time.sleep(5)

#filling in the form
first_name = browser.find_element(By.ID, "input-firstname")
first_name.send_keys("FirstName")

last_name = browser.find_element(By.ID, "input-lastname")
last_name.send_keys("LastName")

random_email = str(random.randint(0,99999)) + "@example.com"

email = browser.find_element(By.ID, "input-email")
email.send_keys("your-email8@example.com")

telephone = browser.find_element(By.ID, "input-telephone")
telephone.send_keys("+351999888777")

password = browser.find_element(By.ID, "input-password")
password.send_keys("123456")

password_confirm = browser.find_element(By.ID, "input-confirm")
password_confirm.send_keys("123456")

newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
newsletter.click()

terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
terms.click()

continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
continue_button.click()

time.sleep(5)

#asserting that the browser title is correct
assert browser.title == "Your Account Has Been Created!"

time.sleep(5)

#closing the browser
browser.quit()

