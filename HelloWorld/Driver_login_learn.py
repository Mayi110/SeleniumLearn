from selenium import webdriver
import time

driver = webdriver.Firefox()

url = 'https://mail.qq.com'
# url = 'http://mail.163.com/'
driver.get(url)
#在网速或其它原因导致元素还未加载完成，就进行定位时会报错，因此需要自己定义方法，或者等待
# while 1:
#     start = time.clock()
#     try:
#         driver.find_element_by_css_selector('#u')
#         print('find')
#         end = time.clock()
#         break
#     except:
#         print('not find')
# print('time:'+str(end-start))

#是因为element包含在frame内，因此需要在查找元素前加入转到frame语句
frame=driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame)


driver.find_element_by_css_selector('#u').clear()
driver.find_element_by_css_selector('#u').send_keys('980850796@qq.com')
driver.find_element_by_css_selector('#p').clear()
driver.find_element_by_css_selector('#p').send_keys('hongchenzimo')
driver.find_element_by_css_selector('#login_button').click()
driver.quit()