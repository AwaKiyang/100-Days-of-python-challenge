from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo') #website containing checkbox

time.sleep(5)
driver.find_element(By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/label[1]/input[1]').click() #checkbox element to be checked
#time.sleep(5)
#driver.find_element(By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/label[1]/input[1]').click() #checkbox element to be unchecked since we a still on the checked element box
time.sleep(10)

driver.quit()

'''
this code helps demonstrate box checking with selenium'''