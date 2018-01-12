# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
发电机页面基本方法
'''


class generator_page(BasePage):
    """定位器"""
    generatorName_loc = (By.CSS_SELECTOR, "input[name='deviceNodeName']")                   # 名称
    generatorModel_loc = (By.CSS_SELECTOR, "input[name='model']")                           # 型号
    generatorRatedPower_loc = (By.CSS_SELECTOR, "input[name='ratedPower']")                 # 额定功率
    generatorRatedCapacity_loc = (By.CSS_SELECTOR, "input[name='ratedCapacity']")           # 额定容量
    generatorRatedPowerFactor_loc = (By.CSS_SELECTOR, "input[name='ratedPowerFactor']")     # 额定功率因数
    generatorRatedVoltage_loc = (By.CSS_SELECTOR, "input[name='ratedVoltage']")             # 额定电压
    generatorRatedSpeed_loc = (By.CSS_SELECTOR, "input[name='ratedSpeed']")                 # 额定转速
    generatorRatedCurrent_loc = (By.CSS_SELECTOR, "input[name='ratedCurrent']")             # 额定电流
    generatorRemark_loc = (By.CSS_SELECTOR, "textarea[name='note']")                        # 备注

    # 输入名称
    def input_generatorName(self, generatorName):
        self.send_keys(generatorName, *self.generatorName_loc)

    # 输入型号
    def input_generatorModel(self, generatorModel):
        self.send_keys(generatorModel, *self.generatorModel_loc)

    # 输入额定功率
    def input_generatorRatedPower(self, generatorRatedPower):
        self.send_keys(generatorRatedPower, *self.generatorRatedPower_loc)

    # 输入额定容量
    def input_generatorRatedCapacity(self, generatorRatedCapacity):
        self.send_keys(generatorRatedCapacity, *self.generatorRatedCapacity_loc)

    # 输入额定功率因数
    def input_generatorRatedPowerFactor(self, generatorRatedPowerFactor):
        self.send_keys(generatorRatedPowerFactor, *self.generatorRatedPowerFactor_loc)

    # 输入额定电压
    def input_generatorRatedVoltage(self, generatorRatedVoltage):
        self.send_keys(generatorRatedVoltage, *self.generatorRatedVoltage_loc)

    # 输入额定转速
    def input_generatorRatedSpeed(self, generatorRatedSpeed):
        self.send_keys(generatorRatedSpeed, *self.generatorRatedSpeed_loc)

    # 输入额定电流
    def input_generatorRatedCurrent(self, generatorRatedCurrent):
        self.send_keys(generatorRatedCurrent, *self.generatorRatedCurrent_loc)

    # 输入备注
    def input_generatorRemark(self, generatorRemark):
        self.send_keys(generatorRemark, *self.generatorRemark_loc)
