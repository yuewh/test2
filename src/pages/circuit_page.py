# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
回路页面基本方法
'''


class circuit_page(BasePage):
    """定位器"""
    circuitName_loc = (By.ID, 'shortName')                                                      # 名称
    circuitPurpose_loc = (By.CSS_SELECTOR, "select[name='purpose']")                            # 负荷用途
    circuitIsContactCircuit_loc = (By.CSS_SELECTOR, "select[name='isContactCircuit']")          # 是否联络回路
    circleRatedVoltage_loc = (By.ID, 'ratedVoltage ')                                           # 额定电压
    circleRatedVoltageSelectList_loc = (                                                        # 额定电压的选项
        By.CSS_SELECTOR, "ul[data-ng-show='listShow && !((supplyVoltages|filterByVal:model.ratedVoltage).empty)'] > li")
    circleContactCircuit_loc = (By.ID, 'contactCircuit ')                                       # 关联设备
    circleContactCircuitSelectList_loc = (                                                      # 关联设备的选项
        By.CSS_SELECTOR, "ul[data-ng-show='listShow1 && !((contactCircuitList|filterByVal:model.contactCircuit)."
                         "empty)'] > li")

    # 输入名称
    def input_circuitName(self, circuitName):
        self.send_keys(circuitName, *self.circuitName_loc)

    # 输入负荷用途
    def input_circuitPurpose(self, circuitPurpose):
        self.send_keys(circuitPurpose, *self.circuitPurpose_loc)

    # 选择是否联络回路
    def input_circuitIsContactCircuit(self, circuitIsContactCircuit):
        self.select_by_option(circuitIsContactCircuit, *self.circuitIsContactCircuit_loc)

    # 选择关联设备
    def input_circleContactCircuit(self, circleContactCircuit):
        self.click(*self.circleContactCircuit_loc)
        self.click_valueFromList(circleContactCircuit, self.circleContactCircuitSelectList_loc)

    # 选择额定电压
    def input_circleRatedVoltage(self, circleRatedVoltage):
        self.click(*self.circleRatedVoltage_loc)
        self.click_valueFromList(circleRatedVoltage, self.circleRatedVoltageSelectList_loc)
