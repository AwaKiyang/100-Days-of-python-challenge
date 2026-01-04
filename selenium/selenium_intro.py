from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get("https://webscraper.io/test-sites/e-commerce/static") #website to scrape
title = driver.title
print(title)

price_dollar = driver.find_element(By.CLASS_NAME, "price").text
locator1 = driver.find_element(By.XPATH, "//h2[normalize-space()='E-commerce training site']").text
locator2 = driver.find_element(By.CSS_SELECTOR, "div[class='jumbotron'] h2").text
html_element = driver.find_element(By.CLASS_NAME, "price")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(price_dollar, locator1 , locator2)
print(html_element.tag_name) #gets the tag name of the html element
print(html_element.get_attribute("palceholder")) #gets the value of the place holder of the html element


time.sleep(10)
#driver.close() #closes a particular tab
driver.quit() #closes the whole program

