from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
driver.implicitly_wait(10)
print(driver.get_cookies())

driver.find_element_by_name("email").send_keys('18513510827')
driver.find_element_by_name("password").send_keys('hongchenzimo')
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()