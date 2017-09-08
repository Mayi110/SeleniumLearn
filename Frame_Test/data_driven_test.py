from selenium import webdriver
from modularized_test import Function
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self._driver = webdriver.Firefox()
        self.base_url = "https://www.51kaihui.com"
        print('test start')

    def test_case(self):
        driver = self._driver
        driver.get(self.base_url)
        f = open('user_info', 'r')
        user_infos = f.readlines()
        f.close()
        for user_info in user_infos:
            name = user_info.split()[0]
            pwd = user_info.split()[1]
            Function(driver).login_(name, pwd)
            self.assertIn('即会通|在线商务会议专家', driver.title)
            Function(driver).logout_()
            self.assertIn('logout', driver.current_url)

    def tearDown(self):
        self._driver.quit()
        print('test end')

if __name__ == '__main__':
    unittest.main()