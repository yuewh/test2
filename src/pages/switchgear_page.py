# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
开关柜页面基本方法
'''


class switchgear_page(BasePage):

    """定位器"""
    switchgearName_loc = (By.CSS_SELECTOR, "input[name='deviceNodeName']")          # 名称
    switchgearSerialNumber_loc = (By.CSS_SELECTOR, "input[name='serialNumber']")    # 编号
    switchgearDeviceType_loc = (By.CSS_SELECTOR, "input[name='deviceType']")        # 型号

    # 输入名称
    def input_switchgearName(self, switchgearName):
        self.send_keys(switchgearName, *self.switchgearName_loc)

    # 输入编号
    def input_switchgearSerialNumber(self, switchgearSerialNumber):
        self.send_keys(switchgearSerialNumber, *self.switchgearSerialNumber_loc)

    # 输入型号
    def input_switchgearDeviceType(self, switchgearDeviceType):
        self.send_keys(switchgearDeviceType, *self.switchgearDeviceType_loc)