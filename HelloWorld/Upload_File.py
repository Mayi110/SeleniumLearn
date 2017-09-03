from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.51kaihui.com/login/index")
driver.implicitly_wait(10)
#登录
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("18513510827")
driver.find_element_by_id("nloginpwd").send_keys("123456")
driver.find_element_by_id("loginsubmit1").click()
#个人中心
driver.find_element_by_link_text("个人中心").click()
driver.find_element_by_id('id_profile_picture').send_keys(u'D:\\651394.png')
driver.find_element_by_id('personal-profile-picture-upload-button').click()

driver.quit()