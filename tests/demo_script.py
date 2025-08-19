from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# * Initialize the Chrome driver
driver = webdriver.Safari()

# * Open a website
driver.get("http://demostore.supersqa.com")
time.sleep(1)  # Wait for the page to load

# * Click on "My Account" Tab
my_account_tab = driver.find_element(by=By.LINK_TEXT, value="My account")
my_account_tab.click()
time.sleep(1)  # Wait for the page to load

# * Scroll the page by 300 pixels down
driver.execute_script("window.scrollBy(0, 300);")

time.sleep(1)

# * Find and fill the "Username" field
user_name_fiels = driver.find_element(by=By.ID, value="username")
user_name_fiels.send_keys("Aditya")

time.sleep(1)  # Wait for a second

# * Find and fill the "Password" field
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys("password")

time.sleep(1)

# * Check the "Remember Me" checkbox
remember_me_checkbox = driver.find_element(by=By.ID, value="rememberme")
remember_me_checkbox.click()

time.sleep(1)

# * Click on the Login Buttom
login_button = driver.find_element(by=By.NAME, value="login")
login_button.click()

time.sleep(1)

# * Get the Error
error_message = driver.find_element(by=By.CSS_SELECTOR, value="ul.woocommerce-error li")
print(error_message)

driver.quit() # Close the browser
