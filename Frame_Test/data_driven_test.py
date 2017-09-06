from selenium import webdriver
from modularized_test import Function

f = open('user_info', 'r')
user_infos = f.readlines()
f.close()

driver = webdriver.Firefox()
driver.get("https://www.51kaihui.com")
for user_info in user_infos:
    name = user_info.split()[0]
    pwd = user_info.split()[1]
    Function(driver).login_(name, pwd)
    Function(driver).logout_()
driver.quit()
