# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
母线页面基本方法
'''


class generatrix_page(BasePage):
    """定位器"""
    generatrixName_loc = (By.ID, 'name')                                            # 设备名称
    generatrixRatedVoltage_loc = (By.ID, 'ratedVoltage')                            # 额定电压
    generatrixSpecifications_loc = (By.ID, 'specifications')                        # 规格
    generatrixModel_loc = (By.ID, 'model')                                          # 型号
    generatrixRatedLoadFlow_loc = (By.ID, 'ratedLoadFlow')                          # 额定载流量
    generatrixRemark_loc = (By.CSS_SELECTOR, "textarea[name='remark']")             # 备注

    # 输入设备名称
    def input_generatrixName(self, generatrixName):
        self.send_keys(generatrixName, *self.generatrixName_loc)

    # 输入额定电压
    def input_generatrixRatedVoltage(self, generatrixRatedVoltage):
        self.send_keys(generatrixRatedVoltage, *self.generatrixRatedVoltage_loc)

    # 输入规格
    def input_generatrixSpecifications(self, generatrixSpecifications):
        self.send_keys(generatrixSpecifications, *self.generatrixSpecifications_loc)

    # 输入型号
    def input_generatrixModel(self, generatrixModel):
        self.send_keys(generatrixModel, *self.generatrixModel_loc)

    # 输入额定载流量
    def input_generatrixRatedLoadFlow(self,generatrixRatedLoadFlow):
        self.send_keys(generatrixRatedLoadFlow, *self.generatrixRatedLoadFlow_loc)

    # 输入备注
    def input_generatrixRemark(self, generatrixRemark):
        self.send_keys(generatrixRemark, *self.generatrixRemark_loc)
