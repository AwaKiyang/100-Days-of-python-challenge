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

driver.get("https://cosmocode.io/automation-practice-webtable/") #website containing web table

table_checkboxes = driver.find_elements(By.CLASS_NAME, value="hasVisited") 

table = driver.find_element(By.ID, value="countries") # locating the table by using its ID
table_rows = driver.find_elements(By.TAG_NAME, value='tr') # locate table rows by using tag_name

print(len(table_rows))


def data_extraction(): 
    """
    Docstring for data_extraction fo data form table (Country, Capital, currency, and language) 
    as list
    """
    #######------Creating respective list contain table columns info----########
    countries_list = list() 
    capital_list = list()
    currency_list = list()
    language_list = list()

    #creating a for loop which iterate from the list of rows#
    for tableRow in table_rows:
        row = tableRow.find_elements(By.TAG_NAME, value="td")   #creating a list from table and storing row data
        countries_list.append(row[1].text) #appending country a index1 from row data
        capital_list.append(row[2].text) #appending capital a index2 from row data
        currency_list.append(row[3].text) #appending currency a index3 from row data
        language_list.append(row[4].text) #appending language a index4 from row data

    #returning the output as list of country,capital,currency and language respectively
    return f'#########-country-##########{countries_list}\n#@@@@@@@@@@-capital-@@@@@@@@@@{capital_list}\n$$$$$$$-currency-$$$$$$$$$$$${currency_list}\n%%%%%%%%%%-language-%%%%%%%%%{language_list}'

time.sleep(3)
driver.quit()
