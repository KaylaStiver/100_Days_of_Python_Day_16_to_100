from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_text = driver.find_element(By.CSS_SELECTOR, "input.form-control.top")
first_text.send_keys("Jane")

last_text = driver.find_element(By.CSS_SELECTOR, "input.form-control.middle")
last_text.send_keys("Doe")

email_text = driver.find_element(By.CSS_SELECTOR, "input.form-control.bottom")
email_text.send_keys("test@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

