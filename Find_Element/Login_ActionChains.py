from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://www.purvar.com/")
driver.implicitly_wait(10)

menu = driver.find_element_by_css_selector(".itcompreserv>a")
ActionChains(driver).move_to_element(menu).perform()
driver.find_element_by_link_text(u"ICT服务").click()

time.sleep(5)

driver.quit()