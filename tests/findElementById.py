from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()

driver.get("http://demostore.supersqa.com/")

cart = driver.find_element(by=By.ID, value="site-header-cart")
cart.click()

driver.quit()


