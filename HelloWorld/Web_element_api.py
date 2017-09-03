from selenium import webdriver

driver = webdriver.Firefox()

url = 'https://baidu.com'

driver.get(url)

size = driver.find_element_by_css_selector('#kw').size
print(size)

attribute = driver.find_element_by_css_selector('#kw').get_attribute('type')
print(attribute)

text = driver.find_element_by_xpath(".//*[@id='su']").text
print(text)

result = driver.find_element_by_css_selector('#kw').is_displayed()
print(result)

driver.quit()
