from selenium import webdriver


def broswer():
    driver = webdriver.Firefox()
    return driver


if __name__ == '__main__':
    dr = broswer()
    dr.get(u'http://test2.liveuc.net/imm-web')
    dr.quit()