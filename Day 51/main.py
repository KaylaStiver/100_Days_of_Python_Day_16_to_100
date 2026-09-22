from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

load_dotenv()

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = os.getenv("Y_EMAIL")
Y_PASSWORD = os.getenv("Y_PASSWORD")
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEEDTEST_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # Go to speedtest.net and start speed test
        self.driver.get(SPEEDTEST_URL)
        go_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button")
        go_btn.click()
        sleep(60) # Wait a minute for test to finish

        # Dismiss irrelevant pop-up
        dismiss_btn = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/button")
        dismiss_btn.click()
        sleep(2)

        # Grab download and upload speed results
        self.down = float(self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3").text)
        self.up = float(self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3").text)
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        # Log into Y account
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(Y_EMAIL)

        password_text = self.driver.find_element(By.ID, "password")
        password_text.send_keys(Y_PASSWORD)

        submit_button = self.driver.find_element(By.TAG_NAME,"button")
        submit_button.click()
        sleep(2)

        # Compose tweet based on speed test results and post tweet
        tweet_input = self.driver.find_element(By.ID, "tweet-compose")
        tweet_input.send_keys(f"Hey ISP, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_post = self.driver.find_element(By.ID, "post-btn")
        tweet_post.click()
        sleep(2)
        self.driver.quit() # Close the bot

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()