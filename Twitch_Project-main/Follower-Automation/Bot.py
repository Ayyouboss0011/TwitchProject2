from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your Chrome WebDriver executable
chrome_driver_path = '/path/to/chromedriver.exe'  # Replace with your actual path

# Initialize a Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Open the browser in maximized window
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Navigate to Twitch.tv
driver.get('https://www.twitch.tv')

# Execute JavaScript to click the "Sign Up" button using the JavaScript selector
try:
    js_script = 'document.querySelector("#root > div > div.Layout-sc-1xcs6mc-0.jCYBxv > nav > div > div.Layout-sc-1xcs6mc-0.wNwlN > div.Layout-sc-1xcs6mc-0.eTolXv > div > div.Layout-sc-1xcs6mc-0.hqWiNh.anon-user > div:nth-child(2) > button").click();'
    driver.execute_script(js_script)
except Exception as e:
    print("Error: Unable to execute JavaScript to click the Sign Up button")

# Wait for 5 seconds
time.sleep(5)

# You can add more code here to interact with the sign-up page if needed

# Close the browser when you're done
driver.quit()
