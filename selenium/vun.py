from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get('https://www.goethe.de/ins/cm/fr/spr/prf/gzb2.cfm')
time.sleep(2)
procceed = True
while procceed == True:
    driver.find_element(By.ID, value='btn-mjxif1evfihxd').click()
    time.sleep(2)
    driver.find_element(By.ID, value=' id2').click()
    time.sleep(2)
