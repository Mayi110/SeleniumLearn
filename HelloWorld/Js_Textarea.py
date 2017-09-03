from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.51kaihui.com/login/index")
driver.implicitly_wait(10)
#登录
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("18513510827")
driver.find_element_by_id("nloginpwd").send_keys("123456")
driver.find_element_by_id("loginsubmit1").click()
#会议编辑
driver.find_element_by_xpath(".//*[@id='id6']/span/a[1]").click()
text = "会议信息哈哈哈"
js = "var sum=document.getElementById('id_message'); sum.value='" + text + "';"
driver.execute_script(js)
driver.find_element_by_xpath(".//*[@id='schedule_button']").click()

driver.quit()
