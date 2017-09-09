from .driver import broswer
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = broswer()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()