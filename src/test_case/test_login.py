# coding:utf-8
__author__ = 'luws'

import unittest
from selenium import webdriver
from src.common.excel_data import excel_data
from src.group.login import login

'''
登录页面测试
'''


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login = login(self.driver, '云运营--后台')
        self.sheetname = 'login'
        self.testdata = excel_data().get_list(self.sheetname)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        """登录页面：输入正确的账号和密码，登录成功，测试是否串号"""
        testdata = self.testdata[0]     # 1条用例
        try:
            self.login.login(testdata[1], testdata[2])
            getUsername = self.login.get_username()
            self.assertEqual(getUsername, testdata[1], self.sheetname + testdata[0] + '测试失败：串号')
        except Exception as e:
            self.login.img_screenshot(testdata[0])
            raise e

    def test_login_fail(self):
        """登录页面：输入不正确的账号和密码，登录失败，测试页面提示是否正确"""
        all_testdata = self.testdata[1:3]       # 3条用例
        for testdata in all_testdata:
            try:
                self.login.login(testdata[1], testdata[2])
                getLoginInfo = self.login.get_loginInfo()
                self.assertEqual(getLoginInfo, testdata[3], self.sheetname + testdata[0] + '测试失败：错误提示有误')
            except Exception as e:
                self.login.img_screenshot(testdata[0])
                raise e


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_login_success'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
