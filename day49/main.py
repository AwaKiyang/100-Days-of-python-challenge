from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.common.keys import Keys  #import keys for entering keybaord keys 

import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True)

# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

# Initialize the Chrome WebDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)