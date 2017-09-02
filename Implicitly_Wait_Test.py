from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Firefox()
driver.get("https://baidu.com")
driver.implicitly_wait(10)

try:
    driver.find_element_by_id("kww").send_keys('selenium2')
except NoSuchElementException as e:
        print(e)
finally:
    driver.quit()