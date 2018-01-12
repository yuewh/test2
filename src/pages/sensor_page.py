# coding:utf-8
__author__ = 'lws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from src.common.log import log
from time import sleep

'''
设备管理-传感器配置页面基本方法
'''


class sensor_page(BasePage):

    """定位器"""
    sensor_loc = (                                                                                  # 传感器配置按钮
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='header'] > div[class^='menu'] > ul > li:nth-child(2) > span")

    """传感器配置页面"""
    createSensorButton_loc = (By.CSS_SELECTOR, "div[class^='btnGroup'] > button")                      # 添加按钮
    copySensorButton_loc = (By.CSS_SELECTOR, "div[class^='btnGroup'] > button:nth-child(2)")          # N次复制按钮
    updateSensorListButton_loc = (By.CSS_SELECTOR, "div[class^='btnGroup'] > button:nth-child(3)")    # 编辑列表按钮
    updateSensorStatusListButton_loc = (By.CSS_SELECTOR, "div[class^='btnGroup'] > div")              # 批量修改状态按钮
    submitSelectSensorStatusListButton_loc = (                                                      # 批量修改状态二次确认的确认按钮
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div.ant-popover-inner > div > div > '
                         'div.ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm')
    cancelSelectSensorStatusListButton_loc = (                                                      # 批量修改状态二次确认的取消按钮
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div.ant-popover-inner > div > div > '
                         'div.ant-popover-buttons > button:nth-child(1)')
    queryDtuTypeInput_loc = (By.CSS_SELECTOR, "div[class^='filter'] > div > div > div")               # 对应通信管理机类型
    queryDtuCodeInput_loc = (By.CSS_SELECTOR, "div[class^='filter'] > div:nth-child(2) > div > div")  # 对应通信管理机
    queryChannelNameInput_loc = (By.CSS_SELECTOR, "div[class^='filter'] > div:nth-child(3) > div > div")    # 对应通道
    queryInput_loc = (By.CSS_SELECTOR, "div[class^='filter'] > div:nth-child(4) > input")             # 输入查询关键字
    queryButton_loc = (By.CSS_SELECTOR, "div[class^='filter'] > div:nth-child(5) > button")           # 查询按钮按钮
    sensorNameList_loc = (By.CLASS_NAME, "td[class^=minWidth100]")                                     # IMU名称所在列
    deleteSensorButtonList_loc = (By.CSS_SELECTOR, "a[class*='delete']")         # 删除按钮所在列
    selectAllsensorButton_loc = (                                                                   # 传感器全选按钮
        By.CSS_SELECTOR, 'thead.ant-table-thead > tr > th > span > div > label > span')
    submitDelectSensorButton_loc = (                                                                # 删除传感器二次确认的确定按钮
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div.ant-popover-inner > div > div > '
                         'div.ant-popover-buttons > button:nth-child(2)')
    cancelDelectSensorButton_loc = (                                                                # 删除传感器二次确认的取消按钮
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div.ant-popover-inner > div > div > '
                         'div.ant-popover-buttons > button:nth-child(1)')

    """传感器添加页面"""
    calendarInput_loc = (                                                                           # 日期控件的输入栏
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div > div > div > input')
    sensorNameInput_loc = (By.ID, 'position')                                                       # 传感器名称（位置）
    sensorTypeInput_loc = (                                                                         # 传感器类型
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(2) > "
                         "div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div")
    sensorModelInput_loc = (                                                                        # 传感器型号
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(3) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorProductCodeInput_loc = (By.ID, 'productCode')                                             # 出厂编号
    sensorProduceDateInput_loc = (                                                                  # 出厂日期
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(6) > "
                         "div > div.ant-col-12.ant-form-item-control-wrapper > div > span > div > input")
    sensorPropertyRightInput_loc = (                                                                # 产权
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(7) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorMeasuringPointSequenceInput_loc = (By.ID, 'measuringPointSequence')                       # 测量点号
    sensorAddressInput_loc = (By.ID, 'address')                                                     # 通信地址
    sensorDtuTypeInput_loc = (                                                                      # 对应通信管理机类型
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(10) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorDtuCodeInput_loc = (                                                                      # 对应通信管理机
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(11) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorChannelNameInput_loc = (                                                                  # 对应通道
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(12) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorSupplyPhaseInput_loc = (                                                                  # 供电相位
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(21) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorCtInput_loc = (                                                                           # CT变比
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(22) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorPtInput_loc = (                                                                           # PT变比
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(23) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorEquipmentStatusInput_loc = (                                                              # 设备状态
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(24) > "
                         "div > div:nth-child(2) > div > div > div")
    sensorInstallDateInput_loc = (                                                                  # 调试时间
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(25) > "
                         "div > div:nth-child(2) > div > span > div > input")
    sensorLaunchDateInput_loc = (                                                                   # 投运时间
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > div:nth-child(2) > div:nth-child(26) > "
                         "div > div:nth-child(2) > div > span > div > input")
    sensorRemarkInput_loc = (By.ID, 'remark')                                                       # 备注

    sensorMonitoredObjectNameList_loc = (By.CLASS_NAME, 'item-title ')                              # 一次设备树上的设备名称
    sensorPositionDescribeInput_loc = (                                                             # 监测点位置
        By.CSS_SELECTOR, "div[class^='attr___'] > div:nth-child(1) > span:nth-child(2) > div > div")
    sensorMonitoringLevelInput_loc = (                                                              # 监测点级别
        By.CSS_SELECTOR, "div[class^='attr___'] > div:nth-child(2) > span:nth-child(2) > div > div")
    sensorIsUsedCalculateResultInput_loc = (                                                        # 是否用于计量结算
        By.CSS_SELECTOR, "div[class^='attr___'] > div:nth-child(3) > span:nth-child(2) > div > div")
    sensorBindAllButton_loc = (By.CSS_SELECTOR, "span[class^='ac'] > span:nth-child(1)")              # 全绑定按钮
    sensorUnbindAllButton_loc = (By.CSS_SELECTOR, "span[class^='ac'] > span:nth-child(2)")            # 全解绑按钮
    metricTypeSelect_loc = (By.CSS_SELECTOR, "i.anticon.anticon-filter")    # point分类筛选按钮（遥信or遥测）
    metricItemSelect_loc = (
        By.CSS_SELECTOR, "body > div:last-child > div > div > div > div.ant-popover-inner > div > div > div > "
                         "div.ant-radio-group > label:nth-child(2) > span.ant-radio")  # point分类筛选遥信单选框
    analogItemSelect_loc = (
        By.CSS_SELECTOR, "body > div:last-child > div > div > div > div.ant-popover-inner > div > div > div > "
                         "div.ant-radio-group > label:nth-child(1) > span.ant-radio")  # point分类筛选遥测单选框
    searchMetricTypeButton_loc = (
        By.CSS_SELECTOR, "body > div:last-child > div > div > div > div.ant-popover-inner > div > div > div > "
                         "div[class^='btns'] > div[class^='bs']")  # point分类筛选器中的搜索按钮
    resetMetricTypeButton_loc = (
        By.CSS_SELECTOR, "body > div:last-child > div > div > div > div.ant-popover-inner > div > div > div > "
                         "div[class^='btns'] > div[class^='br']")  # point分类筛选器中的重置按钮

    submitCreateSensorButton_loc = (By.CSS_SELECTOR, 'div.ant-col-6.ant-col-offset-4 > button:nth-child(1)')     # 确定按钮
    cancelCreateSensorButton_loc = (By.CSS_SELECTOR, 'div.ant-col-6.ant-col-offset-4 > button:nth-child(2)')     # 取消按钮
    """N次复制-复制规则弹窗"""
    sensorCopyNum_loc = (                                                                           # N次复制次数
        By.CSS_SELECTOR, "body > div:last-child > div > div[class*='mdlConfirm'] > div > div.ant-modal-content > "
                         "div.ant-modal-body > div > div > div > div > div:nth-child(2) > input")
    submitCopySensorNumButton_loc = (
        By.CSS_SELECTOR, "body > div:last-child > div > div[class*='mdlConfirm'] > div > div.ant-modal-content > "
                         "div.ant-modal-footer > span > span:nth-child(1) > button")     # N次复制确定按钮
    cancelCopySensorNumButton_loc = (
        By.CSS_SELECTOR, "body > div:last-child > div > div[class*='mdlConfirm'] > div > div.ant-modal-content > "
                         "div.ant-modal-footer > span > span:nth-child(2) > button")     # N次复制取消按钮
    """N次复制&编辑列表的编辑页面"""
    bindButtonList_loc = (By.CSS_SELECTOR, 'span.ant-input-group-addon')                               # 传感器位置栏的绑定按钮
    submitUpdateAllSensorButton_loc = (                                                                # 保存按钮
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > button:nth-child(1)")
    cancelUpdateAllSensorButton_loc = (                                                                # 取消按钮
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='undefined'] > div > div > div > div > button:nth-child(2)")
    """关联监测点位置弹窗"""
    submitBindPointButton_loc = (
        By.CSS_SELECTOR, "div.ant-modal-footer > span > span:nth-child(1) > button")     # 确定按钮
    cancelBindPointButton_loc = (
        By.CSS_SELECTOR, "div.ant-modal-footer > span > span:nth-child(2) > button")     # 取消按钮

    # 点击传感器配置按钮
    def click_sensor(self):
        self.click(*self.sensor_loc)

    # 查询传感器-选择对应通信管理机类型
    def input_dtuType(self,
                      dtuType       # 对应通信管理机类型，str，IMU或专变终端
                      ):
        self.click(*self.queryDtuTypeInput_loc)
        self.select_in_LastDiv(str(dtuType))

    # 查询传感器-选择对应通信管理机
    def input_dtuCode(self,
                      dtuCode       # 对应通信管理机, str,len=16
                      ):
        # 验证输入的参数长度是否正确
        try:
            assert len(dtuCode) == 16, '输入参数有误：' + dtuCode
        except AssertionError as e:
            log().error('输入参数有误：' + dtuCode)
            raise e
        self.click(*self.queryDtuCodeInput_loc)
        self.select_in_LastDiv(str(dtuCode))

    # 查询传感器-选择对应通道
    def input_channelName(self,
                          channelName       # 对应通道，str
                          ):
        self.click(*self.queryChannelNameInput_loc)
        self.select_in_LastDiv(str(channelName))

    # 查询传感器-输入查询关键字
    def input_key(self, key):
        self.find_element(*self.queryInput_loc).send_keys(key)

    # 查询传感器-点击查询按钮
    def click_queryButton(self):
        self.click(*self.queryButton_loc)

    # 点击添加按钮
    def click_createSensorButton(self):
        self.click(*self.createSensorButton_loc)

    # 点击N次复制按钮
    def click_copySensorButton(self):
        self.click(*self.copySensorButton_loc)

    # 点击编辑列表按钮
    def click_updateSensorListButton(self):
        self.click(*self.updateSensorListButton_loc)

    # 批量修改状态
    def updateSensorStatusList(self,
                               sensorStat       # 要修改的传感器状态
                               ):
        self.click(*self.updateSensorStatusListButton_loc)
        self.select_in_LastDiv(str(sensorStat))

    # 批量修改状态-点击二次确认的确认按钮
    def click_submitUpdateSensorStatusList(self):
        self.click(*self.submitSelectSensorStatusListButton_loc)

    # 批量修改状态-点击二次确认的取消按钮
    def click_cancelUpdateSensorStatusList(self):
        self.click(*self.cancelSelectSensorStatusListButton_loc)

    # 根据传感器名称，点击详情按钮
    def click_querySensorButton(self, sensorName):
        self.input_key(sensorName)
        self.click_queryButton()
        n = self.get_elementNum(sensorName, *self.sensorNameList_loc)
        self.click(
            By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > "
                             "div > div > div > div[class^='stateTable'] > div > div > div > div > div > div > table > "
                             "tbody > tr:nth-child(%s) > td:nth-child(11) > div > a" % (n-1))

    # 根据传感器名称，点击编辑按钮
    def click_updateSensorButton(self, sensorName):
        self.input_key(sensorName)
        self.click_queryButton()
        n = self.get_elementNum(sensorName, *self.sensorNameList_loc)
        self.click(
            By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > "
                             "div > div > div > div[class^='stateTable'] > div > div > div > div > div > div > table > "
                             "tbody > tr:nth-child(%s) > td:nth-child(11) > div > a:nth-child(2)" % (n-1))

    # 根据传感器名称，点击删除按钮
    def click_deleteSensorButton(self, sensorName):
        self.input_key(sensorName)
        self.click_queryButton()
        n = self.get_elementNum(sensorName, *self.sensorNameList_loc)
        self.click(
            By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > "
                             "div > div > div > div[class^='stateTable'] > div > div > div > div > div > div > table > "
                             "tbody > tr:nth-child(%s) > td:nth-child(11) > div > a:nth-child(3)" % (n-1))

    # 根据传感器名称，点击删除按钮后二次确认的确认按钮
    def click_submitDeleteSensorButton(self):
        self.click(*self.submitDelectSensorButton_loc)

    # 根据传感器名称，点击删除按钮后二次确认的取消按钮
    def click_cancelDeleteSensorButton(self):
        self.click(*self.cancelDelectSensorButton_loc)

    # 点击全选按钮
    def click_selectAllsensorButton(self):
        self.click(*self.selectAllsensorButton_loc)

    # 根据传感器名称，点击一个传感器的复选框
    def click_selectOneSensorButton(self, sensorName):
        self.input_key(sensorName)
        self.click_queryButton()
        sleep(0.5)
        n = self.get_elementNum(sensorName, *self.sensorNameList_loc)
        self.click(
            By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > "
                             "div > div > div > div[class^='stateTable'] > div > div > div > div > div > div > table > "
                             "tbody > tr:nth-child(%s) > td:nth-child(1) > span > label > span" % (n-1))

    # 在传感器添加页面，输入传感器名称（位置）
    def input_sensorName(self, sensorName):
        self.find_element(*self.sensorNameInput_loc).send_keys(str(sensorName))

    # 在传感器添加页面，选择传感器类型
    def input_sensorType(self, sensorType):
        self.click(*self.sensorTypeInput_loc)
        self.select_in_LastDiv(sensorType)

    # 在传感器添加页面，选择传感器型号
    def input_sensorModel(self, sensorModel):
        self.click(*self.sensorModelInput_loc)
        self.select_in_LastDiv(str(sensorModel))

    # 在传感器添加页面，输入出厂编号
    def input_sensorProductCode(self, sensorProductCode):
        self.find_element(*self.sensorProductCodeInput_loc).send_keys(str(sensorProductCode))

    # 在传感器添加页面，输入出厂日期
    def input_sensorProduceDate(self, sensorProduceDate):
        self.check_dataFormat(sensorProduceDate)
        self.click(*self.sensorProduceDateInput_loc)
        self.find_element(*self.calendarInput_loc).send_keys(str(sensorProduceDate))
        self.click(*self.sensorNameInput_loc)

    # 在传感器添加页面，选择产权
    def input_sensorPropertyRight(self, sensorPropertyRight):
        self.click(*self.sensorPropertyRightInput_loc)
        self.select_in_LastDiv(str(sensorPropertyRight))

    # 在传感器添加页面，输入测量点序号
    def input_sensorMeasuringPointSequence(self, sensorMeasuringPointSequence):
        self.find_element(*self.sensorMeasuringPointSequenceInput_loc).send_keys(str(sensorMeasuringPointSequence))

    # 在传感器添加页面，输入通信地址
    def input_sensorAddress(self, sensorAddress):
        self.find_element(*self.sensorAddressInput_loc).send_keys(str(sensorAddress))

    # 在传感器添加页面，选择对应通信管理机类型
    def input_sensorDtuType(self, sensorDtuType):
        self.click(*self.sensorDtuTypeInput_loc)
        self.select_in_LastDiv(str(sensorDtuType))

    # 在传感器添加页面，选择对应通信管理机
    def input_sensorDtuCode(self, sensorDtuCode):
        self.click(*self.sensorDtuCodeInput_loc)
        self.select_in_LastDiv(str(sensorDtuCode))

    # 在传感器添加页面，选择对应通道
    def input_sensorChannelName(self, sensorChannelName):
        self.click(*self.sensorChannelNameInput_loc)
        self.select_in_LastDiv(str(sensorChannelName))

    # 在传感器添加页面，选择供电相位
    def input_sensorSupplyPhase(self, sensorSupplyPhase):
        self.click(*self.sensorSupplyPhaseInput_loc)
        self.select_in_LastDiv(str(sensorSupplyPhase))

    # 在传感器添加页面，选择CT变比
    def input_sensorCt(self, sensorCt):
        self.click(*self.sensorCtInput_loc)
        self.select_in_LastDiv(str(sensorCt))

    # 在传感器添加页面，选择PT变比
    def input_sensorPt(self, sensorPt):
        self.click(*self.sensorPtInput_loc)
        self.select_in_LastDiv(str(sensorPt))

    # 在传感器添加页面，选择设备状态
    def input_sensorEquipmentStatus(self, sensorEquipmentStatus):
        self.click(*self.sensorEquipmentStatusInput_loc)
        self.select_in_LastDiv(str(sensorEquipmentStatus))

    # 在传感器添加页面，输入调试日期
    def input_sensorInstallDate(self, sensorInstallDate):
        self.check_dataFormat(sensorInstallDate)
        self.click(*self.sensorInstallDateInput_loc)
        self.find_element(*self.calendarInput_loc).send_keys(str(sensorInstallDate))
        self.click(*self.sensorNameInput_loc)

    # 在传感器添加页面，输入投运日期
    def input_sensorLaunchDate(self, sensorLaunchDate):
        self.check_dataFormat(sensorLaunchDate)
        self.click(*self.sensorLaunchDateInput_loc)
        self.find_element(*self.calendarInput_loc).send_keys(str(sensorLaunchDate))
        self.click(*self.sensorNameInput_loc)

    # 在传感器添加页面，输入备注
    def input_sensorRemark(self, sensorRemark):
        self.find_element(*self.sensorRemarkInput_loc).send_keys(str(sensorRemark))

    # 在传感器添加页面，点击设备树上的设备层级
    def click_bindPoint(self,
                        monitoredObject,          # 监测对象(设备名称)，str
                        ):
        n = self.get_elementNum(monitoredObject, *self.sensorMonitoredObjectNameList_loc)
        sensorMonitoredObjectNameList = self.find_elements(*self.sensorMonitoredObjectNameList_loc)
        for i in range(10):
            try:
                sensorMonitoredObjectNameList[n - 1].click()
                break
            except Exception:
                sleep(0.5)

    # 在传感器添加页面，选择监测点位置
    def input_sensorPositionDescribe(self, sensorPositionDescribe):
        self.click(*self.sensorPositionDescribeInput_loc)
        self.select_in_LastDiv(sensorPositionDescribe)

    # 在传感器添加页面，选择监测点级别
    def input_sensorMonitoringLevel(self, sensorMonitoringLevel):
        self.click(*self.sensorMonitoringLevelInput_loc)
        self.select_in_LastDiv(sensorMonitoringLevel)

    # 在传感器添加页面，选择是否用于计量结算
    def input_sensorIsUsedCalculateResult(self, sensorIsUsedCalculateResult):
        self.click(*self.sensorIsUsedCalculateResultInput_loc)
        self.select_in_LastDiv(sensorIsUsedCalculateResult)

    # 在传感器添加页面，在绑定传感器区域，点击全绑定
    def click_bindAll(self):
        self.click(*self.sensorBindAllButton_loc)

    # 在传感器添加页面，在绑定传感器区域，点击point分类的筛选按钮
    def click_metricTypeSelectButton(self):
        self.click(*self.metricTypeSelect_loc)

    # 在传感器添加页面，在绑定传感器区域，点击point分类筛选器中选择遥信或遥测
    def input_metricType(self, metricType):
        try:
            assert str(metricType) == '遥信' or str(metricType) == '遥测', '参数错误：metricType应输入遥信或遥测'
        except AssertionError:
            self.mylog.error('参数错误：metricType应输入遥信或遥测')
        if str(metricType) == '遥测':
            self.click(*self.metricItemSelect_loc)
        else:
            self.click(*self.analogItemSelect_loc)

    # 在传感器添加页面，在绑定传感器区域，点击point分类筛选器中的搜索按钮
    def click_searchMetricTypeButton(self):
        self.click(*self.searchMetricTypeButton_loc)

    # 在传感器添加页面，点击确定按钮
    def click_submitCreateSensorButton(self):
        self.click(*self.submitCreateSensorButton_loc)

    # 在传感器添加页面，点击取消按钮
    def click_cancelCreateSensorButton(self):
        self.click(*self.cancelCreateSensorButton_loc)

    # 在N次复制页面-复制规则弹窗，输入N次复制次数
    def input_sensorCopyNum(self, sensorCopyNum):
        self.send_keys(sensorCopyNum, *self.sensorCopyNum_loc)

    # 在N次复制页面-复制规则弹窗，点击确定按钮
    def click_submitCopySensorNumButton(self):
        self.click(*self.submitCopySensorNumButton_loc)

    # 在N次复制页面-复制规则弹窗，点击取消按钮
    def click_cancelCopySensorNumButton(self):
        self.click(*self.cancelCopySensorNumButton_loc)

    # 在N次复制编辑页面，根据序号点击传感器位置的绑定按钮，打开关联监测点位置弹窗
    def click_bindSensorButton(self, num):
        sensorList = self.find_elements(*self.bindButtonList_loc)
        for i in range(10):
            try:
                sensorList[num-1].click()
                break
            except Exception:
                sleep(0.5)

    # 在N次复制编辑页面，点击保存按钮
    def click_submitUpdateAllSensorButton(self):
        self.click(*self.submitUpdateAllSensorButton_loc)

    # 在N次复制编辑页面，点击取消按钮
    def click_cancelUpdateAllSensorButton(self):
        self.click(*self.cancelUpdateAllSensorButton_loc)

    # 在关联监测点位置弹窗中，点击确定按钮
    def click_submitBindPointButton(self):
        self.click(*self.submitBindPointButton_loc)

    # 在关联监测点位置弹窗中，点击取消按钮
    def click_cancelBindPointButton(self):
        self.click(*self.cancelBindPointButton_loc)
