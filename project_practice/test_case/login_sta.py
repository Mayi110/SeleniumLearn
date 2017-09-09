from time import sleep
import unittest, sys
sys.path.append(".\\models")
sys.path.append(".\\page_obj")
from models import myunit, function
from page_obj.loginPage import Login


class loginTest(myunit.MyTest):
    #测试用户登录
    def user_login_verify(self, username='', password=''):
        Login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名密码为空登录'''
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), '请输入用户名')
        function.insert_img(self.driver, "user_pwd_empty.png")

    def test_login2(self):
        '''用户名正确密码为空登录'''
        self.user_login_verify(username='18513510827')
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), '请输入密码')
        function.insert_img(self.driver, "pwd_empty.png")

    def test_login3(self):
        '''用户名密码不匹配'''
        self.user_login_verify(username='18513510827', password='123456')
        po = Login(self.driver)
        sleep(2)
        self.assertEqual(po.login_error_hint(), '密码错误')
        function.insert_img(self.driver, "pwd_error.png")

    def test_login4(self):
        '''用户名密码正确'''
        self.user_login_verify(username='18513510827', password='111111')
        sleep(2)
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), '哈哈111')
        function.insert_img(self.driver, "user_pwd_true.png")


if __name__ == '__main__':
    unittest.main()