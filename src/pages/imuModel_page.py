# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
IMU模板基本方法
'''


class imuModel_page(BasePage):
    """ 定位器 """
    model_loc = (By.CSS_SELECTOR, '.tt2 > ul > li:nth-child(2)')                # 设备模板按钮
    """IMU模板页面"""
    createImuModel_loc = (By.CSS_SELECTOR, "button[type='button']")              # 添加按钮
    imuModelList_loc = (By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr')          # 单行imu模板
    imuModelNameList_loc = (By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr > td:nth-child(2)')     # 所有IMU型号字段
    submitDeleteImuModel_loc = (                                                # 点击删除以后二次确认的确认按钮
        By.CSS_SELECTOR,
        'body > div:last-child > div > div > div > div.ant-popover-inner > div > div > div.ant-popover-buttons > '
        'button:nth-child(2)')
    cancelDeleteImuModel_loc = (                                                # 点击删除以后二次确认的取消按钮
        By.CSS_SELECTOR,
        'body > div:last-child > div > div > div > div.ant-popover-inner > div > div > div.ant-popover-buttons > '
        'button')

    """IMU模板添加页面"""
    # 基本信息
    imuModelNameInput_loc = (By.ID, 'name')                                     # IMU型号
    imuModelModelInput_loc = (By.ID, 'model')                                   # IMU型号编码
    imuModelProductNameInput_loc = (                                            # 生产厂家
        By.CSS_SELECTOR,
        '#root > div > div > div.section___2uy8q.ant-layout > div.content___2x5ax.ant-layout-content > div > '
        'div.undefined.content___3gHkO.ant-layout > div > div > div > div > form > div:nth-child(3) > '
        'div:nth-child(1) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div')
    imuModelCloudCommunicationStyleInput_loc = (                                # 默认云端通信方式
        By.CSS_SELECTOR,
        '#root > div > div > div.section___2uy8q.ant-layout > div.content___2x5ax.ant-layout-content > div > '
        'div.undefined.content___3gHkO.ant-layout > div > div > div > div > form > div:nth-child(4) > '
        'div:nth-child(1) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div')
    imuModelSupportF223Input_loc = (                                            # 是否支持223
        By.CSS_SELECTOR,
        '#root > div > div > div.section___2uy8q.ant-layout > div.content___2x5ax.ant-layout-content > div > '
        'div.undefined.content___3gHkO.ant-layout > div > div > div > div > form > div:nth-child(4) > '
        'div:nth-child(2) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div')
    imuModelRemarkInput_loc = (By.ID, 'remark')                                 # 备注
    # 通道列表
    createPort_loc = (                                                           # 添加按钮
        By.CSS_SELECTOR,
        '#root > div > div > div.section___2uy8q.ant-layout > div.content___2x5ax.ant-layout-content > div > '
        'div.undefined.content___3gHkO.ant-layout > div > div > div > div > form > div:nth-child(7) > div > div > '
        'div > div > div > div:nth-child(1) > button')

    # 提交
    submit_loc = (By.CSS_SELECTOR, "button[type='submit']")                     # 保存按钮
    cancel_loc = (By.CLASS_NAME, '.ant-btn.default___t6qVU.ant-btn-lg')         # 取消按钮
    createImuModelInfo_loc = (By.CSS_SELECTOR, 'div.ant-message > span > div > div > div > span')  # 保存提示
    createImuModelPortInfo_loc = (By.CLASS_NAME, '.ant-form-explain')            # 通道列表的提示信息

    """IMU模板详情页面"""
    basicInfoList_loc = (By.CSS_SELECTOR, '.ant-form-item-control > span')      # 所有基本信息字段
    portInfoList_loc = (By.CSS_SELECTOR, '.ant-table-tbody > tr')               # 单行通道

    # 点击设备模板按钮
    def click_model(self):
        self.click(*self.model_loc)
        self.switch_to_window()

    # 在IMU模板页面点击添加按钮
    def click_createImuModel(self):
        self.click(*self.createImuModel_loc)

    # 根据IMU型号，在IMU模板页面点击对应的删除按钮
    def click_deleteImuModel(self,
                             imuModelName       # IMU型号，str
                             ):
        n = self.get_elementNum(str(imuModelName), *self.imuModelNameList_loc)
        self.click(
            By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(6) > div > a:nth-child(2)' % n)

    # 点击删除二次确认中的确定按钮
    def click_submitDelectImuModel(self):
        self.click(*self.submitDeleteImuModel_loc)

    # 点击删除二次确认中的取消按钮
    def click_cancelDelectImuModel(self):
        self.click(*self.cancelDeleteImuModel_loc)

    # 根据IMU型号，在IMU模板页面点击对应的详情按钮
    def click_queryImuModel(self,
                            imuModelName        # IMU型号，str
                            ):
        n = self.get_elementNum(str(imuModelName), *self.imuModelNameList_loc)
        self.click(By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(6) > div > a' % n)

    # 获取页面上所有IMU模板的所有内容
    def query_imuModelList(self):
        imuModelList = []
        imuModelList_loc = self.find_elements(*self.imuModelList_loc)
        for n in range(1, len(imuModelList_loc)+1):
            tempList = []
            imuModelNum = self.find_element(
                By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td' % n)
            imuModelName = self.find_element(
                By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(2)' % n)
            imuModelProductName = self.find_element(
                By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(3)' % n)
            imuModelCloudCommunicationStyle = self.find_element(
                By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(4)' % n)
            imuModelPortNum = self.find_element(
                By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(5)' % n)
            tempList.append(imuModelNum.text)
            tempList.append(imuModelName.text)
            tempList.append(imuModelProductName.text)
            tempList.append(imuModelCloudCommunicationStyle.text)
            tempList.append(imuModelPortNum.text)
            imuModelList.append(tempList)
        return imuModelList

    # 获取页面上所有IMU模板的IMU型号字段
    def query_imuModelNameList(self):
        imuModelNameList = []
        imuModelNameList_loc = self.find_elements(*self.imuModelNameList_loc)
        for n in imuModelNameList_loc:
            imuModelName = n.text
            imuModelNameList.append(imuModelName)
        return imuModelNameList

    # 在imu添加页面，输入IMU型号
    def input_imuModelName(self,
                           imuModelName     # IMU型号，str
                           ):
        self.find_element(*self.imuModelNameInput_loc).send_keys(str(imuModelName))

    # 在imu添加页面，输入IMU型号编码
    def input_imuModelModel(self,
                            imuModelModel       # IMU型号，str
                            ):
        self.find_element(*self.imuModelModelInput_loc).send_keys(str(imuModelModel))

    # 在imu添加页面，选择生产厂家
    def input_imuModelProductName(self,
                                  imuModelProductName       # IMU生产厂家，str
                                  ):
        self.click(*self.imuModelProductNameInput_loc)
        self.select_in_LastDiv(imuModelProductName)

    # 在imu添加页面，选择默认云端通信方式
    def input_imuModelCloudCommunicationStyle(self,
                                              imuModelCloudCommunicationStyle       # imu默认云端通信方式，str
                                              ):
        self.click(*self.imuModelCloudCommunicationStyleInput_loc)
        self.select_in_LastDiv(imuModelCloudCommunicationStyle)

    # 在imu添加页面，选择是否支持223
    def input_imuModelSupportF223(self,
                                  imuModelSupportF223       # imu是否支持223，str
                                  ):
        self.click(*self.imuModelSupportF223Input_loc)
        self.select_in_LastDiv(imuModelSupportF223)

    # 在imu添加页面，输入备注
    def input_remark(self,
                     remark     # imu备注
                     ):
        self.find_element(*self.imuModelRemarkInput_loc).send_keys(str(remark))

    # 在imu添加页面，点击通道的添加按钮
    def click_createPort(self):
        self.click(*self.createPort_loc)

    # 在imu添加页面，选择通道类型
    def input_acquisitionAndCommunicationMode(self,
                                              portNumber,       # IMU通道号，int
                                              acquisitionAndCommunicationMode       # IMU通道类型，str
                                              ):
        self.click(
            By.CSS_SELECTOR, 'tbody.ant-table-tbody > tr:nth-child(%s) > td:nth-child(2) > div > div' % str(portNumber))
        self.select_in_LastDiv(acquisitionAndCommunicationMode)

    # 在imu添加页面，点击保存按钮
    def click_submit(self):
        self.click(*self.submit_loc)

    # 在imu添加页面，点击取消按钮
    def click_cancel(self):
        self.click(*self.cancel_loc)

    # 获取点击添加/删除等按钮后的页面顶部持续5秒的提示消息
    def get_ImuModelInfo(self):
        try:
            createImuModelInfo = self.find_element(*self.createImuModelInfo_loc).text
        except Exception:
            createImuModelInfo = '未找到页面提示'
        return createImuModelInfo

    # 获取通道列表中的提示消息
    def get_createImuModelPortInfo(self):
        try:
            createImuModelPortInfo = self.find_element(*self.createImuModelPortInfo_loc).text
        except Exception:
            createImuModelPortInfo = '未找到页面提示'
        return createImuModelPortInfo

    # 获取IMU模板详情中的信息,包括基本信息和通道信息(前置条件:已经在详情页面)
    def query_imuModelDetail(self):
        imuModelDetail = []             # 存储所有信息
        basicInfo = []                  # 存储基本信息
        portInfo = []                   # 存储通道信息
        basicInfoList = self.find_elements(*self.basicInfoList_loc)
        portInfoList = self.find_elements(*self.portInfoList_loc)
        # 获取基本信息
        for n in basicInfoList:
            everybasicInfo = n.get_attribute('title')
            basicInfo.append(everybasicInfo)
        imuModelDetail.append(basicInfo)
        # 获取通道信息
        for m in portInfoList:
            everyportInfo = m.text
            portInfo.append(everyportInfo.split())
        imuModelDetail.append(portInfo)
        return imuModelDetail
