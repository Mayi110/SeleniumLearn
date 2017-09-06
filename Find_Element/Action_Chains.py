from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)

menu = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(menu).click(driver.find_element_by_link_text('搜索历史')).perform()
ActionChains(driver).move_to_element(menu).perform()
driver.find_element_by_link_text("搜索历史").click()

driver.quit()