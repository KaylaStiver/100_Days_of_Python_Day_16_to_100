from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Using the XPath to scrape the event dates and names
py_events = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")
event_list = py_events[0].text.splitlines()

# Empty dict to hold parent
parent_dict = {}
# Empty dict to nest
event_dict = {}
# Variable to track index in event_list
event_count = 0
# Variable to track index in parent_dict
index = 0

# Looping through the events
for event in event_list:
    # If event is even, it will contain a date. The event_dict will also be wiped.
    if event_count % 2 == 0:
        event_dict = {"time": event}
    # If odd, the event will contain a name. This marks the completion of the event_dict.
    else:
        event_dict["name"] = event
        parent_dict[index] = event_dict # Added to parent dict.
        index += 1 # Index of parent dict moved
    event_count += 1 # Increase event count for conditional

print(parent_dict)
driver.quit()