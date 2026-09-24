from time import sleep
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdxuQzoQ3q3q_l140__gOpRQqcYZwGrMc_in0wM9gNo5sbMxg/viewform?usp=publish-editor"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

page = requests.get(ZILLOW_CLONE_URL) # Go to Zillow clone
soup = BeautifulSoup(page.content, 'html.parser') # Scrape site

property_list = []
price_list = []
address_list = []

properties = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor", href=True) # Find all anchors with links
for prop in properties:
    property_list.append(prop.get("href")) # Add link to list

prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
for price in prices:
    trunc_price = re.split(r'[/+]', price.text)[0] # Remove unwanted characters
    price_list.append(trunc_price) # Add cleaned price to list

addresses = soup.find_all("address")
for address in addresses:
    remove = "\n|"
    clean_add = address.text.translate(str.maketrans("", "", remove)).strip() # Remove all new lines, pipes, and white space
    address_list.append(clean_add) # Add cleaned address to list

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL) # Go to google form

# Loop through all properties and add the cleaned data from the lists to input fields
for index in range(len(property_list)):
    sleep(2)
    address_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(address_list[index])

    price_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price_list[index])

    property_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_field.send_keys(property_list[index])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click() # Submit form
    sleep(2) # Wait for form

    return_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    return_button.click() # Return to form to start next entry

driver.quit() # Quit running once all properties have been entered
