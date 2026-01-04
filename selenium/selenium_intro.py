from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://webscraper.io/test-sites/e-commerce/static")
title = driver.title
print(title)

price_dollar = driver.find_element(By.CLASS_NAME, "price").text
locator1 = driver.find_element(By.XPATH, "//h2[normalize-space()='E-commerce training site']").text
locator2 = driver.find_element(By.CSS_SELECTOR, "div[class='jumbotron'] h2").text
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(price_dollar, locator1 , locator2)


time.sleep(10)
#driver.close() #closes a particular tab
driver.quit() #closes the whole program

