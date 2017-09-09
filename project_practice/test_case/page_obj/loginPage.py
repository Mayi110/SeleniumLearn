from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class Login(Page):
    """
    用户登录页面
    """

    url = '/login'

    #定位器
    username_loc = (By.ID, 'loginname')
    pwd_loc = (By.ID, 'nloginpwd')
    submit_loc = (By.ID, 'loginsubmit1')

    #Action
    def login_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.pwd_loc).send_keys(password)

    def login_submit(self):
        self.find_element(*self.submit_loc).click()

    #定义统一登录入口
    def user_login(self, username='18513510827', password = '111111'):
        """获取用户名密码登录"""
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_submit()
        sleep(1)

    login_error_hint_loc = (By.XPATH, ".//*[@id='tip_error']")
    user_login_success_log = (By.XPATH, "html/body/div[1]/div/div[2]/table/tbody/tr/td[1]/a")

    #登录错误提示
    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text

    #登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_log).text