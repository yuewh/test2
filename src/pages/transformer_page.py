# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
变压器页面基本方法
'''


class transformer_page(BasePage):
    """定位器"""
    transformerPreviousCircuit_loc = (By.CSS_SELECTOR, "input[name='previousCircuit ']")       # 上级开关回路
    transformerPreviousCircuitSelectList_loc = (                                               # 上级开关回路的选项
        By.CSS_SELECTOR, "ul[data-ng-show='listShow && !(circuitList|filterByVal:model.previousCircuit).empty'] > li")
    transformerNextCircuit_loc = (By.CSS_SELECTOR, "input[name='nextCircuit ']")               # 下级开关回路
    transformerNextCircuitSelectList_loc = (                                                   # 下级开关回路的选项
        By.CSS_SELECTOR, "ul[data-ng-show='listShow1 && !(circuitList|filterByVal:model.nextCircuit).empty'] > li")
    transformerName_loc = (By.CSS_SELECTOR, "input[name='transformerName']")                   # 设备名称
    transformerStandbyType_loc = (By.CSS_SELECTOR, "select[name='standbyType']")               # 变压器主备性质
    transformerModel_loc = (By.CSS_SELECTOR, "input[name='model']")                            # 型号
    transformerProductor_loc = (By.CSS_SELECTOR, "input[name='productor']")                    # 生产厂家
    transformerProductCode_loc = (By.CSS_SELECTOR, "input[name='productCode']")                # 出厂编号
    transformerProductDate_loc = (By.ID, 'productDate')                                        # 出厂日期
    transformerRatedCapacity_loc = (By.CSS_SELECTOR, "input[name='ratedCapacity']")            # 额定容量
    transformerInsulatingMedium_loc = (By.CSS_SELECTOR, "select[name='insulatingMedium']")     # 绝缘介质
    transformerIsAmorphous_loc = (By.CSS_SELECTOR, "select[name='isAmorphous']")               # 是否非晶变
    transformerNoLoadCurrent_loc = (By.CSS_SELECTOR, "input[name='noLoadCurrent']")            # 空载电流
    transformerShortCircuitLoss_loc = (By.CSS_SELECTOR, "input[name='shortCircuitLoss']")      # 短路损耗
    transformerNoLoadLoss_loc = (By.CSS_SELECTOR, "input[name='noLoadLoss']")                  # 空载损耗
    transformerLoadLoss_loc = (By.CSS_SELECTOR, "input[name='loadLoss']")                      # 负载损耗
    transformerVoltageRatio_loc = (By.CSS_SELECTOR, "select[name='voltageRatio']")             # 电压比
    transformerOilNumber_loc = (By.CSS_SELECTOR, "select[name='oilNumber']")                   # 油号
    transformerOilWeight_loc = (By.CSS_SELECTOR, "input[name='oilWeight']")                    # 油重
    transformerTotalWeight_loc = (By.CSS_SELECTOR, "input[name='totalWeight']")                # 总重
    transformerShortCircuitImpedance_loc = (By.CSS_SELECTOR, "input[name='shortCircuitImpedance']")  # 短路阻抗
    transformerInsulationAndHeatResistanceLevel_loc = (                                        # 绝缘耐热等级
        By.CSS_SELECTOR, "select[name='insulationAndHeatResistanceLevel']")
    transformerEarthingResistance_loc = (By.CSS_SELECTOR, "input[name='earthingResistance']")  # 接地电阻
    transformerWiringGroup_loc = (By.CSS_SELECTOR, "select[name='wiringGroup']")               # 接线组别
    transformerCoolingMethod_loc = (By.CSS_SELECTOR, "select[name='coolingMethod']")           # 冷却方式
    transformerIsEarthed_loc = (By.CSS_SELECTOR, "select[name='isEarthed']")                   # 低压中性点接地标志
    transformerLaunchDate_loc = (By.ID, 'launchDate')                                          # 投运日期
    transformerInstallDate_loc = (By.ID, 'installDate')                                        # 安装日期
    transformerEnableDate_loc = (By.ID, 'enableDate')                                          # 实际启用日期
    transformerDisableDate_loc = (By.ID, 'disableDate')                                        # 实际停用日期
    transformerPlannedResumeDate_loc = (By.ID, 'plannedResumeDate')                            # 计划恢复日期
    transformerChangeCapacity_loc = (By.CSS_SELECTOR, "input[name='changeCapacity']")          # 变动容量
    transformerExpireDate_loc = (By.ID, 'expireDate')                                          # 到期日期
    transformerIsWholeLowerMonitored_loc = (By.CSS_SELECTOR, "select[name='isWholeLowerMonitored']")  # 下级是否全监测
    transformerRemark_loc = (By.CSS_SELECTOR, "textarea[name='remark']")                       # 备注

    # 选择上级开关回路
    def input_transformerPreviousCircuit(self, transformerPreviousCircuit):
        self.click(*self.transformerPreviousCircuit_loc)
        self.click_valueFromList(transformerPreviousCircuit, self.transformerPreviousCircuitSelectList_loc)

    # 选择下级开关回路
    def input_transformerNextCircuit(self, transformerNextCircuit):
        self.click(*self.transformerNextCircuit_loc)
        self.click_valueFromList(transformerNextCircuit, self.transformerNextCircuitSelectList_loc)

    # 输入设备名称
    def input_transformerName(self, transformerName):
        self.send_keys(transformerName, *self.transformerName_loc)

    # 选择变压器主备性质
    def inpue_transformerStandbyType(self, transformerStandbyType):
        self.select_by_option(transformerStandbyType, *self.transformerStandbyType_loc)

    # 输入型号
    def input_transformerModel(self, transformerModel):
        self.send_keys(transformerModel, *self.transformerModel_loc)

    # 输入生产厂家
    def input_transformerProductor(self, transformerProductor):
        self.send_keys(transformerProductor, *self.transformerProductor_loc)

    # 输入出厂编号
    def input_transformerProductCode(self, transformerProductCode):
        self.send_keys(transformerProductCode, *self.transformerProductCode_loc)

    # 输入出厂日期
    def input_transformerProductDate(self, transformerProductDate):
        self.check_dataFormat(transformerProductDate)
        js = "$('#productDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerProductDate_loc).send_keys(transformerProductDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 输入额定容量
    def input_transformerRatedCapacity(self, transformerRatedCapacity):
        self.send_keys(transformerRatedCapacity, *self.transformerRatedCapacity_loc)

    # 选择绝缘介质
    def input_transformerInsulatingMedium(self, transformerInsulatingMedium):
        self.select_by_option(transformerInsulatingMedium, *self.transformerInsulatingMedium_loc)

    # 选择是否非晶变
    def input_transformerIsAmorphous(self, transformerIsAmorphous):
        self.select_by_option(transformerIsAmorphous, *self.transformerIsAmorphous_loc)

    # 输入空载电流
    def input_transformerNoLoadCurrent(self, transformerNoLoadCurrent):
        self.send_keys(transformerNoLoadCurrent, *self.transformerNoLoadCurrent_loc)

    # 输入短路损耗
    def input_transformerShortCircuitLoss(self, transformerShortCircuitLoss):
        self.send_keys(transformerShortCircuitLoss, *self.transformerShortCircuitLoss_loc)

    # 输入空载损耗
    def input_transformerNoLoadLoss(self, transformerNoLoadLoss):
        self.send_keys(transformerNoLoadLoss, *self.transformerNoLoadLoss_loc)

    # 输入负载损耗
    def input_transformerLoadLoss(self, transformerLoadLoss):
        self.send_keys(transformerLoadLoss, *self.transformerLoadLoss_loc)

    # 选择电压比
    def input_transformerVoltageRatio(self, transformerVoltageRatio):
        self.select_by_option(transformerVoltageRatio, *self.transformerVoltageRatio_loc)

    # 选择油号
    def input_transformerOilNumber(self, transformerOilNumber):
        self.select_by_option(transformerOilNumber, *self.transformerOilNumber_loc)

    # 输入油重
    def input_transformerOilWeight(self, transformerOilWeight):
        self.send_keys(transformerOilWeight, *self.transformerOilWeight_loc)

    # 输入总重
    def input_transformerTotalWeight(self, transformerTotalWeight):
        self.send_keys(transformerTotalWeight, *self.transformerTotalWeight_loc)

    # 输入短路阻抗
    def input_transformerShortCircuitImpedance(self, transformerShortCircuitImpedance):
        self.send_keys(transformerShortCircuitImpedance, *self.transformerShortCircuitImpedance_loc)

    # 选择绝缘耐热等级
    def input_transformerInsulationAndHeatResistanceLevel(self, transformerInsulationAndHeatResistanceLevel):
        self.select_by_option(transformerInsulationAndHeatResistanceLevel,
                              *self.transformerInsulationAndHeatResistanceLevel_loc)

    # 输入接地电阻
    def input_transformerEarthingResistance(self, transformerEarthingResistance):
        self.send_keys(transformerEarthingResistance, *self.transformerEarthingResistance_loc)

    # 选择接线组别
    def input_transformerWiringGroup(self, transformerWiringGroup):
        self.select_by_option(transformerWiringGroup, *self.transformerWiringGroup_loc)

    # 选择冷却方式
    def input_transformerCoolingMethod(self, transformerCoolingMethod):
        self.select_by_option(transformerCoolingMethod, *self.transformerCoolingMethod_loc)

    # 选择低压中性点接地标志
    def input_transformerIsEarthed(self, transformerIsEarthed):
        self.select_by_option(transformerIsEarthed, *self.transformerIsEarthed_loc)

    # 输入投运日期
    def input_transformerLaunchDate(self, transformerLaunchDate):
        self.check_dataFormat(transformerLaunchDate)
        js = "$('#launchDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerLaunchDate_loc).send_keys(transformerLaunchDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 输入安装日期
    def input_transformerInstallDate(self, transformerInstallDate):
        self.check_dataFormat(transformerInstallDate)
        js = "$('#installDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerInstallDate_loc).send_keys(transformerInstallDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 输入实际启用日期
    def input_transformerEnableDate(self, transformerEnableDate):
        self.check_dataFormat(transformerEnableDate)
        js = "$('#enableDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerEnableDate_loc).send_keys(transformerEnableDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 输入实际停用日期
    def input_transformerDisableDate(self, transformerDisableDate):
        self.check_dataFormat(transformerDisableDate)
        js = "$('#disableDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerDisableDate_loc).send_keys(transformerDisableDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 输入计划恢复日期
    def input_transformerPlannedResumeDate(self, transformerPlannedResumeDate):
        self.check_dataFormat(transformerPlannedResumeDate)
        js = "$('#plannedResumeDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerPlannedResumeDate_loc).send_keys(transformerPlannedResumeDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 输入变动容量
    def input_transformerChangeCapacity(self, transformerChangeCapacity):
        self.send_keys(transformerChangeCapacity, *self.transformerChangeCapacity_loc)

    # 输入到期日期
    def input_transformerExpireDate(self, transformerExpireDate):
        self.check_dataFormat(transformerExpireDate)
        js = "$('#expireDate').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.transformerExpireDate_loc).send_keys(transformerExpireDate)
        self.click(*self.transformerName_loc)  # 收起日期控件

    # 选择下级是否全监测
    def input_transformerIsWholeLowerMonitored(self, transformerIsWholeLowerMonitored):
        self.select_by_option(transformerIsWholeLowerMonitored, *self.transformerIsWholeLowerMonitored_loc)

    # 输入备注
    def input_transformerRemark(self, transformerRemark):
        self.send_keys(transformerRemark, *self.transformerRemark_loc)
