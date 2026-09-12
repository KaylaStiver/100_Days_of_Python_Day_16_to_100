from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) # Open in chrome
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3) # Waiting for language select to pop up to choose english
close_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
close_button.click()
sleep(3) # Waiting for main game to load

five_secs = time.time() + 5 # 5 seconds from now
five_mins = time.time() + 5*60 # 5 minutes from now
cookie = driver.find_element(By.ID, "bigCookie") # Grab cookie button
click = True

while click: # Continuously click cookie
    cookie.click()

    if time.time() > five_secs: # Every 5 seconds
        click = False
        unlocked_items = driver.find_elements(By.XPATH, "//*[contains(@class, 'enabled')]") #Grab unlocked items
        for item in reversed(unlocked_items): # Sort by most expensive item first
            item.click() # Buy item
            five_secs = time.time() + 5
            click = True # Resume clicking
            break

    if time.time() > five_mins: # Stop game after 5 minutes
        click = False









