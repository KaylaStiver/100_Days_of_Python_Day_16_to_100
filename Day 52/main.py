from time import sleep
from appier.config import load_dot_env
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
LOGIN_URL = "https://app.100daysofpython.dev/services/share-a-naan/login"
SIMILAR_ACC = "elaineducasse"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(BASE_URL) # Navigate to login page

        # Enter account information and submit
        email_input = self.driver.find_element(By.NAME, "username")
        email_input.send_keys(EMAIL)

        password_text = self.driver.find_element(By.NAME, "password")
        password_text.send_keys(PASSWORD)

        submit_button = self.driver.find_element(By.TAG_NAME,"button")
        submit_button.click()
        sleep(1) # Wait for site to load

        # Dismiss the following 2 pop-pups
        dismiss_button_1 = self.driver.find_element(By.CLASS_NAME, "naan-popup-dismiss")
        dismiss_button_1.click()

        sleep(1) # Wait for site to load

        dismiss_button_2 = self.driver.find_element(By.XPATH, "//*[@id='popup-notifications']/div/button[2]")
        dismiss_button_2.click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACC}/followers") # Go directly to similar account's follower list
        follower_scroll = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]")
        # Scroll to bottom of follower list to load all accounts
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", follower_scroll)
        sleep(1)

    def follow(self):
        follower_list = self.driver.find_elements(By.CLASS_NAME, "naan-follower-row")
        for follower in follower_list: # For every follower, click the corresponding button
            try: # Try to follow
                follow_btn = follower.find_element(By.TAG_NAME, "button")
                follow_btn.click()
                sleep(1)
            except ElementClickInterceptedException: # If unfollow prompt appears then dismiss
                cancel_btn = follower.find_element(By.XPATH, "/html/body/div[6]/div/button[2]")
                cancel_btn.click()
                sleep(1)

# Create bot and run all defined functions
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()