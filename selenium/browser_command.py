from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to specify ChromeDriver path
from selenium.webdriver.common.by import By  # Import By for locating elements
import time  # Import time for sleep

# Set Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True) 
# Specify the path to the ChromeDriver executable
service = Service(executable_path=r"C:\Users\awaki\Desktop\100.py\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options) # Initialize the Chrome WebDriver with the specified service and options
driver.get('https://opensource-demo.orangehrmlive.com/')

#driver.minimize_window() #minimize window size
#driver.maximize_window() #Maximizes wndow size to max
#driver.fullscreen_window() #opens the browser in fullscreen mode
#driver.set_window_size(width=768, height=1024)

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value='.oxd-text.oxd-text--p.orangehrm-login-forgot-header').click()
print(driver.title)
time.sleep(5)
driver.back() #.back method carries your backward in browser history
print(driver.title)
time.sleep(5)
driver.forward() #carries forward in your browser history
print(driver.title)
time.sleep(10)

driver.quit()