from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
print("Driver Initiated")

driver.get('https://selenium.dev/documentation')
assert 'Selenium' in driver.title
print("Get Page")

elem = driver.find_element(By.ID, 'm-documentationwebdriver')
elem.click()
assert 'WebDriver' in driver.title
print("Get element click")

driver.quit()