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

#open the herokuapp app login page
driver.get('https://secure-retreat-92358.herokuapp.com/')

f_name = 'AWA'  #user first name
l_name = 'KIYANG' # user last name
email = 'awakiyang9@gmail.com' # user email

f_name_field = driver.find_element(By.NAME, value='fName') #locating the firstname entry by its name
l_name_field = driver.find_element(By.CSS_SELECTOR, value="input[placeholder='Last Name']") #locating the lastname entry by its cssSelector
email_field = driver.find_element(By.XPATH, value="//input[@placeholder='Email address']") #locating the email entry by its xpath
button = driver.find_element(By.TAG_NAME, value="button") #locating button by its tag_name

f_name_field.send_keys(f_name)  #sending firstname into the firstname field
l_name_field.send_keys(l_name) #sending lastname into the lastname field
email_field.send_keys(email) #sending email into the email field

time.sleep(3) #wait 3 sec before clicking the button
button.click() #click the sign up button on the form
#button.send_keys(Keys.ENTER) # alternative of using click() we can use the keyboard keys directly by using the Keys() class
time.sleep(5) # wait 5 sec before closing the browser

driver.quit() #close the browser once everything is done


