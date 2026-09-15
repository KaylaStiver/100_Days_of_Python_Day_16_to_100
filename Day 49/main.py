from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

booked = 0
waitlisted = 0
already_applied = 0
total_class = 0
class_name = ""
class_date = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

email_input = driver.find_element(By.ID, "email-input")
email_input.send_keys("kaylatest@example.com")

password_text = driver.find_element(By.ID, "password-input")
password_text.send_keys("test123")

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click()
sleep(1.5)

tuesday_classes = driver.find_elements(By.CSS_SELECTOR, "div [id*='tue'] div [class*='ClassCard_cardHeader']")
thursday_classes = driver.find_elements(By.CSS_SELECTOR, "div [id*='thu'] div [class*='ClassCard_cardHeader']")
tue_thursday_classes = tuesday_classes + thursday_classes # add tue and thu classes together

for _class in tue_thursday_classes: # loop through classes
    if "6:00 PM" in _class.text:
        class_name = _class.find_element(By.TAG_NAME, "h3").text
        class_date = _class.find_element(By.XPATH,"./ancestor::div[1]/preceding-sibling::h2[starts-with(@id, 'day-title-')]").text # going up a div to find date of current class
        button = _class.find_element(By.TAG_NAME, "button")
        total_class += 1

        if button.text == "Booked":
            print(f"✓ Already booked: {class_name} for {class_date}")
            already_applied += 1
        elif button.text == "Waitlisted":
            print(f"✓ Already waitlisted: {class_name} for {class_date}")
            already_applied += 1
        elif button.text == "Join Waitlist":
            print(f"✓ Join waitlist: {class_name} for {class_date}")
            waitlisted += 1
            button.click()
        else:
            print(f"✓ Booked: {class_name} for {class_date}")
            booked += 1
            button.click()
print("\n")

print("--- BOOKING SUMMARY ---") # summary of bot actions
print(f"Classes booked: {booked}")
print(f"Waitlists joined: {waitlisted}")
print(f"Already booked/waitlisted: {already_applied}")
print(f"Total Tue/Thu 6pm classes processed: {total_class}")
print("\n")

if booked > 0 or waitlisted > 0:
    print("--- DETAILED CLASS LIST ---") # new actions taken on this run
if booked > 0:
    print(f"• [New Booking] {class_name} on {class_date}")
    print("\n")
elif waitlisted > 0:
    print(f"• [New Waitlist] {class_name} on {class_date}")
    print("\n")

driver.get("https://appbrewery.github.io/gym/my-bookings/") # go to bookings
sleep(1.5)

print("--- VERIFICATION RESULT ---") # verifying all actions went through
print(f"Expected: {total_class} bookings")
bookings =  driver.find_elements(By.CSS_SELECTOR, "div [class*='MyBookings_bookingDetails']")
print(f"Confirmed: {len(bookings)} bookings")

if total_class == len(bookings):
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"MISMATCH: Missing {total_class - len(bookings)} bookings")


