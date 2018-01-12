# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
开关页面基本方法
'''


class switch_page(BasePage):
    """定位器"""
    switchName_loc = (By.CSS_SELECTOR, "input[name='name']")                            # 设备名称
    switchType_loc = (By.CSS_SELECTOR, "select[name='switchType']")                     # 开关类型
    switchIsDoublePowerAutomaticSwitch_is_loc = (                                       # 是否双电源开关-是
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.powerStrategy-right.dataZn.th.mg-lf10p.top-15p > div.ng-scope > div > div > '
                         'form > div:nth-child(4) > div > div > div:nth-child(1) > div.fl-left.mg-rt4p.mg-top3p > '
                         'label > span.toggle-radio')
    switchIsDoublePowerAutomaticSwitch_not_loc = (                                      # 是否双电源开关-否
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.powerStrategy-right.dataZn.th.mg-lf10p.top-15p > div.ng-scope > div > div > '
                         'form > div:nth-child(4) > div > div > div:nth-child(2) > div.fl-left.mg-rt4p.mg-top3p > '
                         'label > span.toggle-radio')
    switchStandbyType_loc = (By.CSS_SELECTOR, "select[name='standbyType']")             # 开关作用
    switchModel_loc = (By.CSS_SELECTOR, "input[name='model']")                          # 型号
    switchRatedVoltage_loc = (By.CSS_SELECTOR, "input[name='ratedVoltage']")            # 额定电压
    switchRatedCurrent_loc = (By.CSS_SELECTOR, "input[name='ratedCurrent']")            # 额定电流
    switchRemark_loc = (By.CSS_SELECTOR, "textarea[name='remark']")                     # 备注

    # 输入设备名称
    def input_switchName(self, switchName):
        self.send_keys(switchName, *self.switchName_loc)

    # 选择开关类型
    def input_switchType(self, switchType):
        self.select_by_option(switchType, *self.switchType_loc)

    # 选择是否双电源开关
    def input_switchIsDoublePowerAutomaticSwitch(self, switchIsDoublePowerAutomaticSwitch):
        try:
            assert str(switchIsDoublePowerAutomaticSwitch) == '是' or str(switchIsDoublePowerAutomaticSwitch) == '否', \
                '参数错误：switchIsDoublePowerAutomaticSwitch应输入是或否'
        except AssertionError:
            self.mylog.error('参数错误：switchIsDoublePowerAutomaticSwitch应输入是或否')
        if str(switchIsDoublePowerAutomaticSwitch) == '是':
            self.click(*self.switchIsDoublePowerAutomaticSwitch_is_loc)
        else:
            self.click(*self.switchIsDoublePowerAutomaticSwitch_not_loc)

    # 选择开关作用
    def input_switchStandbyType(self, switchStandbyType):
        self.select_by_option(switchStandbyType, *self.switchStandbyType_loc)

    # 输入型号
    def input_switchModel(self, switchModel):
        self.send_keys(switchModel, *self.switchModel_loc)

    # 输入额定电压
    def input_switchRatedVoltage(self, switchRatedVoltage):
        self.send_keys(switchRatedVoltage, *self.switchRatedVoltage_loc)

    # 输入额定电流
    def input_switchRatedCurrent(self, switchRatedCurrent):
        self.send_keys(switchRatedCurrent, *self.switchRatedCurrent_loc)

    # 输入备注
    def input_switchRemark(self, switchRemark):
        self.send_keys(switchRemark, *self.switchRemark_loc)
