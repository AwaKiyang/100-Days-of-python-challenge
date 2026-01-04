from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options

# Define login credentials and URL
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"

# Open the login page
driver.get(login_url)

username_field = driver.find_element(By.ID, "user-name") # Locate the username input field by its ID
password_field = driver.find_element(By.ID, "password") # Locate the password input field by its ID
login_button = driver.find_element(By.CSS_SELECTOR, "#login-button") # Locate the login button by its CSS selector

username_field.send_keys(username)# Enter the username into the username field
password_field.send_keys(password)# Enter the password into the password field

assert login_button.get_attribute("disabled") is None # Assert that the login button is enabled (not disabled)
login_button.click() # Click the login button to submit the form

success_element = driver.find_element(By.CSS_SELECTOR, ".title") # Locate the element that indicates a successful login
assert success_element.text == "Products"# Assert that the text of the success element is "Products"

# Wait for 10 seconds before closing the browser
time.sleep(10)
# Close the browser and end the session
driver.quit()
