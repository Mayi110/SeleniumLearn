class Function(object):
    def __init__(self, driver):
        self._driver = driver

    def login_(self, name, pwd):
        self._driver.find_element_by_link_text("用户登录").click()
        self._driver.find_element_by_id("loginname").clear()
        self._driver.find_element_by_id("loginname").send_keys(name)
        self._driver.find_element_by_id("nloginpwd").send_keys(pwd)
        self._driver.find_element_by_id("loginsubmit1").click()

    def logout_(self):
        self._driver.find_element_by_link_text("注销").click()

    # def search_key(self, key):
    #     self._driver.find_element_by_id("kw").clear()
    #     self._driver.find_element_by_id("kw").send_keys(key)
    #     self._driver.find_element_by_id("su").click()