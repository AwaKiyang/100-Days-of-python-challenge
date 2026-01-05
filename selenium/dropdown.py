from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support.select import Select #enables us to locate and slect options found in the dropdown menu
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get('https://the-internet.herokuapp.com/dropdown') #website with dropdown

dropdown_element = driver.find_element(By.ID, value="dropdown") #using the BY locator to locate the dropdown element

dropdown_options = Select(dropdown_element) #enables us to wrap the drop_down element
print(dropdown_options.options) #returns a list of available options
print(len(dropdown_options.options)) #returns the numebr of options available

for opt in dropdown_options.options:   #iterating through the list of options belonging to the tag
    print(opt.text)

'''
# Select the value by visible text
# Select the value by index
# Select the option by using a value
'''
time.sleep(2)
#dropdown_options.select_by_visible_text("Option 1") #selecting by using the options visible text
dropdown_options.select_by_value("2") #selecting option with value 2
#dropdown_options.select_by_index(index=1) #selecting option by using its index NB if there is a placeholder text it will consider it during indexing

time.sleep(3)
driver.quit()