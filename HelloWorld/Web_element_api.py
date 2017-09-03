from selenium import webdriver
import time

driver = webdriver.Firefox()
url = 'https://baidu.com'
driver.get(url)
driver.set_window_size(480, 600)
driver.execute_script("window.scrollTo(450,150)")
time.sleep(5)

size = driver.find_element_by_css_selector('#kw').size
print(size)
result = driver.find_element_by_css_selector('#kw').is_displayed()
print(result)
attribute = driver.find_element_by_css_selector('#kw').get_attribute('type')
print(attribute)
driver.find_element_by_id('kw').send_keys('selenium2')
time.sleep(3)
driver.execute_script("window.scrollTo(0,300)")
time.sleep(3)

text = driver.find_element_by_xpath(".//*[@id='4']/h3/a").text
print(text)

driver.get_screenshot_as_file(r"D:\selenium_screenshot2.png")

driver.quit()
