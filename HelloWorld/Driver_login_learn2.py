from selenium import webdriver
import requests

url = 'http://mail.163.com/'

# driver = webdriver.Firefox()

# driver.get(url)
header = {'Cache-Control':'max-age=3600'}
response = requests.get(url=url,headers=header)
print(response.headers['Cache-Control'])
