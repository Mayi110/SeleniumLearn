from selenium import webdriver
import unittest
import HTMLTestRunner


class LoginTest(unittest.TestCase):
    def setUp(self):
        self._driver = webdriver.Firefox()
        self.base_url = "https://baidu.com"
        print('test start')

    def test_case(self):
        driver = self._driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('baidu')
        driver.find_element_by_id('su').click()

    def tearDown(self):
        self._driver.quit()
        print('test end')


if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(LoginTest('test_case'))
    fp = open('C:\\Users\\admin\\Desktop\\report.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况:')

    runner.run(test)
    fp.close()
