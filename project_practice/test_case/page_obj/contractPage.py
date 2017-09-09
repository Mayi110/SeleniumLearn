from selenium.webdriver.common.by import By
from .base import Page


class Contract(Page):
    '''
    用户通讯录界面
    '''

    url = 'user/contact'
    #定位通讯录页面
    contract_open_loc = (By.ID, 'se5')
    #定位元素
    contract_add_group_loc = (By.XPATH, ".//*[@id='settings-nav']/div[2]/span[2]/a")
    contract_add_linkman_loc = (By.XPATH, ".//*[@id='date_range_control']/div/button[1]")
    contract_edit_group_loc = (By.XPATH, ".//*[@id='date_range_control']/div/button[2]")
    contract_delete_group_loc = (By.XPATH, ".//*[@id='date_range_control']/div/button[3]")
    contract_select_group_loc = (By.ID, 'group_569')
    contract_edit_groupname_loc = (By.ID, 'groupName')
    contract_edit_groupname_sure_loc = (By.XPATH, ".//*[@id='groupForm']/button[1]")
    #定位最后一个分组
    contract_final_group_loc = (By.XPATH, ".//*[@id='contactUl']/li[4]")

    #打开通讯录页面
    def contract_open(self):
        self.find_element(*self.contract_open_loc).click()

    #添加组
    def contract_add_group(self, new_groupname):
        self.find_element(*self.contract_add_group_loc).click()
        self.frame("ifr_popup0")
        self.find_element(*self.contract_edit_groupname_loc).send_keys(new_groupname)
        self.find_element(*self.contract_edit_groupname_sure_loc).click()
        self.refresh()

    #得到最后一个分组的名称
    def contract_get_final_group_name(self):
        return self.find_element(*self.contract_final_group_loc).text


