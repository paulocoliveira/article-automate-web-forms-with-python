import time
from selenium.webdriver.common.by import By
from selenium import webdriver

username = "paulocol"
accessToken = "8Yl2j4huUuLPcQIkt54LrxujI0Of43g1vZaSAbBiCi8FRMdi7Y"
gridUrl = "hub.lambdatest.com/wd/hub"

lt_options = {
    "user" : username,
    "accessKey" : accessToken,
    "build" : "your build name",
    "name" : "your test name",
    "platformName" : "Windows 11",
    "browserName" : "Chrome",
    "browserVersion" : "latest",
    "selenium_version": "latest"
}

web_driver = webdriver.ChromeOptions()
options = web_driver
options.set_capability('LT:Options', lt_options)

url = "https://"+username+":"+accessToken+"@"+gridUrl
browser = webdriver.Remote(
    command_executor=url,
    options=options
)

browser.maximize_window()
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

time.sleep(5)

#filling in the form
first_name = browser.find_element(By.ID, "input-firstname")
first_name.send_keys("FirstName")

last_name = browser.find_element(By.ID, "input-lastname")
last_name.send_keys("LastName")

email = browser.find_element(By.ID, "input-email")
email.send_keys("your-email88@example.com")

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