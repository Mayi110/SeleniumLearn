from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.51kaihui.com/login/index")
driver.implicitly_wait(10)

driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("18513510827")
driver.find_element_by_id("nloginpwd").send_keys("123456")
driver.find_element_by_id("loginsubmit1").click()

driver.implicitly_wait(10)

driver.find_element_by_id("se5").click()
driver.find_element_by_xpath(".//*[@id='group_569']").click()
deletes = driver.find_elements_by_link_text("删除")
deletes.pop(-2).click()
print("before delete:", len(deletes))
# print(deletes.pop())
i = 0
for delete in deletes:
    delete.click()
    driver.switch_to.alert().accept()
    time.sleep(1)
    i += 1

print("all delete number is", i)


time.sleep(5)
driver.quit()
