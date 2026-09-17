from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

URL = "https://app.100daysofpython.dev/services/tindog/u/tkIg8guBgyww8PylwLwmW2MDoMG_EkY-"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL) # Go to website

# Log in via fake FaceBook and dismiss pop-ups
login_button = driver.find_element(By.XPATH, "/html/body/header/button")
login_button.click()

sleep(1)
fb_button = driver.find_element(By.XPATH,"//*[@id='login-modal']/div/div/div/button[1]")
fb_button.click()

sleep(1)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window) # Switch to pop up

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("kaylatest@example.com")

password_text = driver.find_element(By.ID, "pass")
password_text.send_keys("test123")

submit_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/button")
submit_button.click()

driver.switch_to.window(base_window) # Switch back to main window
sleep(1)
allow_button = driver.find_element(By.XPATH,"/html/body/main/div/div/form/button")
allow_button.click()
sleep(1)
enable_button = driver.find_element(By.XPATH,"/html/body/main/div/div/form/button[2]")
enable_button.click()

accept_button = driver.find_element(By.XPATH,"/html/body/main/div/div/form/button")
accept_button.click()

swipe = True
while swipe: # Like all profiles every 2 seconds
    try:
        sleep(2)
        accept_button = driver.find_element(By.CSS_SELECTOR, ".btn-like")
        accept_button.click()
        sleep(2)
    except ElementClickInterceptedException: # If a match is found, dismiss notification
        match_link = driver.find_element(By.XPATH, "/html/body/main/div[3]/a")
        match_link.click()