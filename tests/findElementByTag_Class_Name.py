from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com/")

# Find by ClassName
class_Name_single = driver.find_element(by=By.CLASS_NAME, value="product")
print(class_Name_single.text)

print("======")

class_Name = driver.find_elements(by=By.CLASS_NAME, value="product")
for item in class_Name:
    print(item.text)
    print()

print("======")

# Find by Name
byName = driver.find_element(by=By.NAME, value="orderby")
print(byName.text)

print("======")

# Find by TagName
byTag = driver.find_elements(by=By.TAG_NAME, value="a")
print(f'Found {len(byTag)} "a" tags in page')


driver.quit()