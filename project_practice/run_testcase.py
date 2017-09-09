import unittest

test_dir = r"D:\My Study\Python2\XiaoZzi\SeleniumLearn\project_practice\test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)