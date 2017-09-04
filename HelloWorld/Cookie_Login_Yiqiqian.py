from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://signit.cn/wesign/login.html")
driver.implicitly_wait(10)
print(driver.get_cookies())

driver.find_element_by_xpath(".//*[@id='loginCount']").clear()
driver.find_element_by_xpath(".//*[@id='loginCount']").send_keys("980850796@qq.com")
driver.find_element_by_xpath(".//*[@id='loginPwd']").clear()
driver.find_element_by_xpath(".//*[@id='loginPwd']").send_keys("123456a")
driver.find_element_by_xpath(".//*[@id='js-login']").click()
print(driver.get_cookies())

driver.quit()

