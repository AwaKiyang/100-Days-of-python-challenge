from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep
import requests #using request to check for broken images

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get('https://the-internet.herokuapp.com/broken_images') #website with broken images

website_images = driver.find_elements(By.TAG_NAME, value='img')
print(len(website_images))


for images in website_images:
    src = images.get_attribute("src")
    response = requests.get(src)
    if response.status_code != 200:
        print(f"image {src} is not found with status code {response.status_code}")

time.sleep(3)
driver.quit()