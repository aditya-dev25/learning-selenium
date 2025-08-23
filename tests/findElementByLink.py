from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com/")

# By Link Text
byLinkText = driver.find_element(by=By.LINK_TEXT, value="My account")
byLinkText.click()

time.sleep(3)

# By Partial Link Text
byPartialLinkText = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="eCom Store")
byPartialLinkText.click()

time.sleep(3)

driver.quit()