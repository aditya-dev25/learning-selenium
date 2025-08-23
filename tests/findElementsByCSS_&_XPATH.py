from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("http://demostore.supersqa.com/")

# * By CSS Selector
# * cart = driver.find_element(by=By.CSS_SELECTOR, value="#site-header-cart > li:nth-child(1) > a")
# * cart.click()

# * By XPATH
cart = driver.find_element(by=By.XPATH, value='//*[@id="site-header-cart"]/li[1]/a')
cart.click()

time.sleep(3)
driver.quit()