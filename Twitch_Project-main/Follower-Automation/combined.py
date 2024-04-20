from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
import pandas as pd
import csv
import re

# Path to your Chrome WebDriver executable
chrome_driver_path = '/path/to/chromedriver.exe'  # Replace with your actual path

# Initialize a Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Open the browser in a maximized window
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Navigate to Twitch.tv
driver.get('https://www.twitch.tv')

# Execute JavaScript to click the "Sign In" button using the JavaScript selector
try:
    js_script = 'document.querySelector("#root > div > div.Layout-sc-1xcs6mc-0.jCYBxv > nav > div > div.Layout-sc-1xcs6mc-0.wNwlN > div.Layout-sc-1xcs6mc-0.eTolXv > div > div.Layout-sc-1xcs6mc-0.hqWiNh.anon-user > div:nth-child(2) > button").click();'
    driver.execute_script(js_script)
except Exception as e:
    print("Error: Unable to execute JavaScript to click the Sign In button")

# Wait for the Sign In page to load (you may need to adjust the wait time)
time.sleep(5)

###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator
###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator
###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator
###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator
###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator###Name Generator


# Load the CSV file with names
names_df = pd.read_csv('/home/ubuntu/Desktop/Twitch BOT/Gamertags.csv')  # Replace with the actual path

# Function to generate a random password
def generate_random_password(password_length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(password_length))

# Function to generate gamer-style usernames with alphanumeric characters
def generate_gamer_username(name, min_length=4, max_length=25):
    # Remove special characters and spaces from the name
    alphanumeric_name = ''.join(char for char in name if char.isalnum())
    
    modifiers = ["xX", "Pro", "Epic", "The", "Shadow", "Ninja", "Gamer", "Sniper", "Noob", "Cyber"]
    separator = random.choice([""])
    
    modifier = random.choice(modifiers)

    max_attempts = 100
    for _ in range(max_attempts):
        username = f"{modifier}{alphanumeric_name}{separator}"
        if min_length <= len(username) <= max_length:
            return username

    return ""

# Generate gamer-style usernames
num_usernames = 10
usernames = []
for _ in range(num_usernames):
    random_name = random.choice(names_df['Name'])
    gamer_username = generate_gamer_username(random_name, min_length=4, max_length=25)
    usernames.append(gamer_username)


###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator
###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator
###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator
###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator
###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator###PasswordGenerator

# Generate a random password
password_length = 10
generated_password = generate_random_password(password_length)


###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields
###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields
###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields
###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields###Paste Username and Password inside Fields


# Locate the username and password input fields using XPath and enter the generated values
username_field = driver.find_element(By.XPATH, '//*[@id="signup-username"]')  # XPath for the username input field
password_field = driver.find_element(By.XPATH, '//*[@id="password-input"]')    # XPath for the password input field

# Enter the generated username and password
username_field.send_keys(usernames[0])  # You can choose a username from the list
password_field.send_keys(generated_password)

# Wait
time.sleep(2)

# Execute JavaScript to click the "Next Step" button using the provided JS path
js_click_next_button = 'document.querySelector("body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-1xcs6mc-0.dyCtLD > div > div > div.Layout-sc-1xcs6mc-0.hJDYkS > div > form > div.Layout-sc-1xcs6mc-0.koFZug > button").click();'

try:
    driver.execute_script(js_click_next_button)
except Exception as e:
    print("Error: Unable to execute JavaScript to click the 'Next Step' button")

# Wait
time.sleep(3)

# Execute JavaScript to click the "Use email instead" button using the provided JS path
js_click_use_email_button = 'document.querySelector("body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-1xcs6mc-0.dyCtLD > div > div > div.Layout-sc-1xcs6mc-0.hJDYkS > div > form > div.Layout-sc-1xcs6mc-0.lpnVMY > div > div:nth-child(2) > div.Layout-sc-1xcs6mc-0.czEOvg > button > div > div.Layout-sc-1xcs6mc-0.eHKPFw").click();'

try:
    driver.execute_script(js_click_use_email_button)
except Exception as e:
    print("Error: Unable to execute JavaScript to click the 'Use email instead' button")

# Wait
time.sleep(3)

#insert an Email from Emails.csv inside the Twitch window and declare it as "USED"

csv_file_path = "/home/ubuntu/Desktop/Twitch BOT/Emails.csv"  # Replace with the actual path to your CSV file
email_column_index = 0  # Replace with the index of the column containing the emails (0-based index)

email_found = False

# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Open the CSV file in read mode
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)  # Read all rows into a list

    # Iterate over each row in the CSV file
    for row in rows:
        if len(row) > email_column_index:
            email = row[email_column_index]

            # Check if the value in the column matches the email pattern
            if re.match(email_pattern, email):
                print(email)
                email_found = True

                # Find the email input field and enter the email
                email_input = driver.find_element(By.CSS_SELECTOR, '#email-input')
                email_input.clear()
                email_input.send_keys(email)

                # Wait for a moment to observe the input, you can adjust this delay
                time.sleep(2)

                # Close the driver
                driver.quit()

                # Remove the "@" symbol from the email in the CSV file
                updated_email = email.replace("@", "")
                row[email_column_index] = updated_email

                # Write the updated rows back to the CSV file
                with open(csv_file_path, 'w', newline='') as updated_csv_file:
                    csv_writer = csv.writer(updated_csv_file)
                    csv_writer.writerows(rows)

                break

# If no valid email was found, print a message
if not email_found:
    print("No valid email found in the CSV file.")

# Wait for a moment to observe the input, you can adjust this delay
time.sleep(2)




# Close the browser when you're done
driver.quit()
