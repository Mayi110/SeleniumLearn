from selenium import webdriver
import time

driver = webdriver.Firefox()

url_first = u'https://www.baidu.com/'
#可能会导致webdriver找不到元素，某些页面没有随之缩放
# driver.set_window_size(480,400)
driver.get(url_first)
time.sleep(2)
url_second = u'https://tieba.baidu.com/index.html'
driver.get(url_second)
time.sleep(2)
driver.back()
driver.find_element_by_css_selector('#kw').send_keys('selenium3')
driver.find_element_by_css_selector('#su').click()
time.sleep(2)
driver.refresh()
driver.quit()