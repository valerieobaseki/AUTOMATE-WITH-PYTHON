
from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# Github credentials
username = "username"
password = "password"

# initialize the Chrome driver
driver = webdriver.Chrome()
# head to github login page
driver.get("https://example.com/signin")
# find username/email field and send the username itself to the input field
driver.find_element("id", "user_session_username").send_keys(username)
# find password input f/.ield and insert password as well
driver.find_element("id", "user_session_password").send_keys(password)
# click login button
driver.find_element("name", "button").click()

#direct audio download link
driver.get("https://example.com/recordings/filename.mp3")
#wait a few seconds to allow download to complete
time.sleep(10)

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")



# close the driver
driver.close()







