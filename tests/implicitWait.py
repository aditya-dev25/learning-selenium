from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize the driver
driver = webdriver.Chrome()

driver.get('file:///Users/aditya/Desktop/Upskilling/Selenium/python_selenium_course_material/SELENIUM_SECTION/06.%20Waits/page_with_slow_image.html')

'''
Waiting for 6 seconds. It will wait for that time, but checks every 0.5 seconds (not configurable)
ALWAYS waits up to defined seconds before throwing NoSuchElementException
'''

driver.implicitly_wait(6)

image = driver.find_element(by=By.ID, value="the_slow_image")
image.click()
print("Found Image")

time.sleep(3)
# Quit the driver
driver.quit()