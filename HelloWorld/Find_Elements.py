from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.51kaihui.com/login/index")
driver.implicitly_wait(10)
#登录
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("18513510827")
driver.find_element_by_id("nloginpwd").send_keys("123456")
driver.find_element_by_id("loginsubmit1").click()
#到通讯录页面
driver.find_element_by_id("se5").click()
driver.implicitly_wait(10)
#获取分组人数
driver.find_element_by_xpath(".//*[@id='group_569']").click()
all_deletes = len(driver.find_elements_by_link_text("删除"))
#删除分组中所有用户除了倒数第二个
for i in range(1, all_deletes+1):
    j = 1
    #到分组
    driver.find_element_by_xpath(".//*[@id='group_569']").click()
    time.sleep(1)
    need_deletes = len(driver.find_elements_by_link_text("删除"))
    if need_deletes != 2:
        driver.find_element_by_xpath(".//*[@id='contactMessage']/tr[%d]/td[4]/a[2]" % j).click()
        driver.switch_to.frame("ifr_popup0")
        driver.find_element_by_xpath("html/body/div[1]/button[1]").click()
        driver.refresh()
    else:
        driver.find_element_by_xpath(".//*[@id='contactMessage']/tr[2]/td[4]/a[2]").click()
        driver.switch_to.frame("ifr_popup0")
        driver.find_element_by_xpath("html/body/div[1]/button[1]").click()
        break

time.sleep(1)
driver.quit()

#deletes = driver.find_elements_by_link_text("删除")
# print(deletes)
#deletes.pop(-2).click
# print(deletes)
