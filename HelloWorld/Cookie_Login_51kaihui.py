from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.51kaihui.com/login/index")
driver.implicitly_wait(10)
print(driver.get_cookies())

# 登录51kaihui
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("18513510827")
driver.find_element_by_id("nloginpwd").send_keys("111111")
driver.find_element_by_id("loginsubmit1").click()
print(driver.get_cookies())

# driver.add_cookie({'name': 'iactiveImmValue', 'value': '18513510827'})
# print(driver.get_cookies())
driver.get("https://www.51kaihui.com/")
driver.find_element_by_link_text("用户登录").click()
time.sleep(1)

driver.quit()