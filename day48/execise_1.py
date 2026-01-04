from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True)

# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

# Initialize the Chrome WebDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Python.org homepage
driver.get('https://www.python.org/')

data = dict()  # Dictionary to store event data

# Find all elements containing the event dates using XPath
upcoming_date = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')

# Find all elements containing the event names using XPath
upcoming_event = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

# Iterate over the events and dates, storing them in the data dictionary
for i, date, event in zip(range(len(upcoming_event)), upcoming_date, upcoming_event):
    data[i] = {'time': date.text, 'event': event.text}

print(data)  # Print the collected event data

time.sleep(5)  # Wait for 5 seconds before closing the browser

driver.quit()  # Close the browser and end the WebDriver session
