from selenium import webdriver
from modularized_test import Function
import time

driver = webdriver.Firefox()
driver.get("https://baidu.com")

keys = {'python', '中文', 'context'}
for key in keys:
    Login(driver).search_key(key)
    time.sleep(3)

driver.quit()