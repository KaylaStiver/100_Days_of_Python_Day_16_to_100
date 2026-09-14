from selenium import webdriver
import os

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/") # Open in chrome

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

email_input = driver.find_element(By.ID, "email-input")
email_input.send_keys("yourname@example.com") # Input email

password_text = driver.find_element(By.ID, "password-input")
password_text.send_keys("123456") # Input password

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click() # Submit