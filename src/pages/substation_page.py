# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
配电房页面基本方法
'''


class substation_page(BasePage):
    """定位器"""
    """添加配电房页面"""
    substationName_loc = (By.CSS_SELECTOR, "input[name='substationName']")                      # 配电房名称
    substationLaunchDate_loc = (By.ID, 'launchDate')                                            # 投运日期
    substationReactivePowerCompensationCapacity_loc = (                                         # 无功补偿容量
        By.CSS_SELECTOR, "input[name='reactivePowerCompensationCapacity']")
    substationInterlockingType_loc = (By.CSS_SELECTOR, "select[data-ng-model='model.interlockingType']")   # 防误方式
    substationIsIndependentBuilding_loc = (By.CSS_SELECTOR, "select[name='isIndependentBuilding']")        # 是否独立建筑物
    substationPosition_loc = (By.CSS_SELECTOR, "select[name='position']")                       # 配电房位置
    substationEarthingResistance_loc = (By.CSS_SELECTOR, "input[name='earthingResistance']")    # 接地电阻
    substationNetworkCondition_loc = (By.CSS_SELECTOR, "select[data-ng-model='model.networkCondition']")   # 现场网络情况
    substationBandwidth_loc = (By.CSS_SELECTOR, "select[data-ng-model='model.bandwidth']")      # 信号类型
    substationServiceProviderName_loc = (By.CSS_SELECTOR, "input[name='serviceProviderName']")  # 代维单位
    substationAddress_loc = (By.CSS_SELECTOR, "input[name='capacityPrice']")                    # 配电房地址
    substationRemark_loc = (By.CSS_SELECTOR, "textarea[name='remark']")                         # 备注

    # 输入配电房名称
    def input_substationName(self, substationName):
        self.send_keys(substationName, *self.substationName_loc)

    # 输入投运日期
    def input_substationLaunchDate(self, substationLaunchDate):
        self.check_dataFormat(substationLaunchDate)
        js = "$('#launchDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.substationLaunchDate_loc).send_keys(substationLaunchDate)
        self.click(*self.substationName_loc)  # 收起日期控件

    # 输入无功补偿容量
    def input_substationReactivePowerCompensationCapacity(self, substationReactivePowerCompensationCapacity):
        self.send_keys(substationReactivePowerCompensationCapacity,
                       *self.substationReactivePowerCompensationCapacity_loc)

    # 选择防误方式
    def input_substationInterlockingType(self, substationInterlockingType):
        self.select_by_option(substationInterlockingType, *self.substationInterlockingType_loc)

    # 选择是否独立建筑物
    def input_substationIsIndependentBuilding(self, substationIsIndependentBuilding):
        self.select_by_option(substationIsIndependentBuilding, *self.substationIsIndependentBuilding_loc)

    # 选择配电房位置
    def input_substationPosition(self, substationPosition):
        self.select_by_option(substationPosition, *self.substationPosition_loc)

    # 输入接地电阻
    def input_substationEarthingResistance(self, substationEarthingResistance):
        self.send_keys(substationEarthingResistance, *self.substationEarthingResistance_loc)

    # 选择现场网络情况
    def input_substationNetworkCondition(self, substationNetworkCondition):
        self.select_by_option(substationNetworkCondition, *self.substationNetworkCondition_loc)

    # 选择信号类型
    def input_substationBandwidth(self, substationBandwidth):
        self.select_by_option(substationBandwidth, *self.substationBandwidth_loc)

    # 输入代维单位
    def input_substationServiceProviderName(self, substationServiceProviderName):
        self.send_keys(substationServiceProviderName, *self.substationServiceProviderName_loc)

    # 输入配电房地址
    def input_substationAddress(self, substationAddress):
        self.send_keys(substationAddress, *self.substationAddress_loc)

    # 输入备注
    def input_substationRemark(self, substationRemark):
        self.send_keys(substationRemark, *self.substationRemark_loc)
