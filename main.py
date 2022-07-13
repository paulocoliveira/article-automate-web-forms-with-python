import random
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#lambdatest setup and opening the desired website
username = "Your Lambda Username"
accessToken = "Your Lambda Access Key"
gridUrl = "hub.lambdatest.com/wd/hub"

capabilities = {
    'LT:Options' : {
        "user" : "Your Lambda Username",
        "accessKey" : "Your Lambda Access Key",
        "build" : "your build name",
        "name" : "your test name",
        "platformName" : "Windows 11",
    },
    "browserName" : "Chrome",
    "browserVersion" : "103.0",
}

url = "https://"+username+":"+accessToken+"@"+gridUrl

browser = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)

browser.maximize_window()
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

#filling in the form
first_name = browser.find_element(By.ID, "input-firstname")
first_name.send_keys("FirstName")

last_name = browser.find_element(By.ID, "input-lastname")
last_name.send_keys("LastName")

random_email = str(random.randint(0,99999)) + "@example.com"

email = browser.find_element(By.ID, "input-email")
email.send_keys("your-email4@example.com")

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

#asserting that the browser title is correct
assert browser.title == "Your Account Has Been Created!"

#closing the browser
browser.quit()

