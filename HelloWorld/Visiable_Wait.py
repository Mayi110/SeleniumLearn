from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Firefox()
driver.get('https://baidu.com')
#显示等待
element = WebDriverWait(driver, 0.01, 0.5).until(
    ec.presence_of_element_located((By.ID, "kw"))
)
#is_displayed判断元素是否可见
for i in range(1, 10):
    try:
        if driver.find_element_by_css_selector("#k").is_displayed():
            break
    except:
        pass
    time.sleep(i/10000.0)
else:
    print("timeout")
#计算页面打开后元素出现的时间
css_begin = time.clock()
driver.find_element_by_css_selector("#kw")
css_end = time.clock()
print(css_end-css_begin)
xpath_begin = time.clock()
driver.find_element_by_xpath(".//*[@id='su']")
xpath_end = time.clock()
print(xpath_end-xpath_begin)

driver.quit()