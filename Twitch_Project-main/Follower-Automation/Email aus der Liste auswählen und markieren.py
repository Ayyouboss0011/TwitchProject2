import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

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

                # Initialize the Chrome driver
                driver = webdriver.Chrome()
                driver.get("https://example.com")  # Replace with the URL of the page containing the input field

                # Find the email input field and enter the email
                email_input = driver.find_element(By.CSS_SELECTOR, '#email-input')
                email_input.clear()
                email_input.send_keys(email)

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

