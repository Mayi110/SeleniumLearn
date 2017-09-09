from time import sleep
import unittest, sys
sys.path.append(".\\models")
sys.path.append(".\\page_obj")
from models import myunit, function
from page_obj.contractPage import Contract
from page_obj.loginPage import Login


class ContractTest(myunit.MyTest):

    def test_contract_add_group(self):
        Login(self.driver).user_login()
        po = Contract(self.driver)
        po.contract_open()
        po.contract_add_group('hahaha')
        sleep(2)
        self.assertEqual(po.contract_get_final_group_name(), 'hahaha')


if __name__ == '__main__':
    unittest.main()
