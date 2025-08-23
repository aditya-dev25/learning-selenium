from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get('file:///Users/aditya/Desktop/Upskilling/Selenium/python_selenium_course_material/SELENIUM_SECTION/06.%20Waits/page_with_slow_image.html')


'''
For explicit wait, it will check until some condition is met.
We need to import WAIT & EXPECTED_CONDITIONS classes.
'''

my_image = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "the_slow_image")))
print(my_image.is_displayed()) # Returns True


driver.quit()