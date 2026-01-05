from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep
import requests #using request to check for broken links

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get('https://jqueryui.com/') #website with broken links

website_links = driver.find_elements(By.TAG_NAME, value="a") # Find all anchor elements (<a>) on the page
print(len(website_links))

# Iterate through each link found
for link in website_links:
    href = link.get_attribute('href')     # Get the 'href' attribute (URL) of the link
    reponse = requests.get(href)        # Send a GET request to the URL to check its status
    if reponse.status_code >= 400:      # If the status code is 400 or higher, the link is considered broken
        print(f"this url {href} is a broken link with status code {reponse.status_code}")  #printing url and status code

time.sleep(5) # Wait for 5 seconds before closing the browser (for observation)
driver.quit() # Close the browser and end the WebDriver session