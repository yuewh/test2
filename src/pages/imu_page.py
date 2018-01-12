# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from time import sleep

'''
IMU基本方法
'''


class imu_page(BasePage):

    """定位器"""
    imu_loc = (                                                               # IMU配置按钮
        By.CSS_SELECTOR, "#root > div > div > div[class^='section'] > div[class^='content'] > div > "
                         "div[class^='header'] > div[class^='menu'] > ul > li > span")
    """imu配置页面"""
    createImuButton_loc = (
        By.CSS_SELECTOR, "button[type='button']")           # 添加按钮

    imuNameList_loc = (By.CSS_SELECTOR, "div[class^='role_title'] > span")      # IMU名称行
    expandButtonList_loc = (                                                  # 所有展开按钮
        By.CSS_SELECTOR, "a[style='margin-left: 20px;'] > span.fa-angle-double-down.fa")

    """imu添加页面"""
    imuCodeInput_loc = (By.ID, 'code')                                        # imu设备编码
    imuNameInput_loc = (By.ID, 'position')                                    # imu名称（位置）
    imuProduceDateInput_loc = (                                               # imu出厂日期
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(5) > div > div.ant-col-12.ant-form-item-control-wrapper > div > span > div > "
        "span")
    imuProductCodeInput_loc = (By.ID, 'productCode')                          # imu出厂编号
    imuProtocolInput_loc = (                                                  # imu通讯协议
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(7) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div > "
        "div > div")
    imuSupportF223Input_loc = (                                               # imu是否支持223
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(9) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div > "
        "div")
    imuSoftwareVersionInput_loc = (By.ID, 'softwareVersion')                  # 软件版本
    imuInvertingConnectIpAddressInput_loc = (                                 # 反向链接IP地址
        By.ID, 'invertingConnectIpAddress')
    imuInvertingConnectionPortInput_loc = (By.ID, 'invertingConnectionPort')  # 反向链接端口号
    imuCloudCommunicationStyleInput_loc = (                                   # 云端通信方式
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(13) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div > "
        "div")
    imuWirelessCommunicationStyleInput_loc = (                                # 无线通信方式
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(14) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div > "
        "div")
    imuCloudCommunicationAntennaTypeInput_loc = (                             # 通信天线类型
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(15) > div > div.ant-col-12.ant-form-item-control-wrapper > div > div > div > "
        "div")
    imuSimCodeInput_loc = (By.ID, 'simCode')                                  # SIM卡号
    imuSimPropertyRightsInput_loc = (By.ID, 'simPropertyRights')              # SIM卡产权
    imuDebugDateInput_loc = (                                                 # 调试时间
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(18) > div > div.ant-col-12.ant-form-item-control-wrapper > div > span > "
        "div > span")
    imuGuiderInput_loc = (By.ID, 'guider')                                    # 指导人员
    imuInstallerInput_loc = (By.ID, 'installer')                              # 安装人员
    imuLaunchDateInput_loc = (                                                # 投运日期
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div[class^='role_content'] > div > form > "
        "div.ant-row-flex > div:nth-child(21) > div > div.ant-col-12.ant-form-item-control-wrapper > div > span > "
        "div > span")
    imuRemarkInput_loc = (By.ID, 'remark')                                    # 备注
    calendarInput_loc = (                                                     # 日期控件的输入栏
        By.CSS_SELECTOR,
        'body > div:last-child > div > div > div > div > div > div > input')
    imuAcquisitionAndCommunicationModeList_loc = (                            # 通道类型列
        By.CSS_SELECTOR,
        "div[class^='role___'] > div[class^='role_content'] > div > form > div.ant-row > div > div > div > div > div > "
        "div[class^='stateTable'] > div > div > div > div > div > div > table > tbody.ant-table-tbody > tr > "
        "td:nth-child(2)")
    imuProtocolroleList_loc = (                                               # 通道类型为LAN的协议列
        By.CSS_SELECTOR,
        "div[class^='role___'] > div[class^='role_content'] > div > form > div.ant-row > div > div > div > div > div > "
        "div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div > div > "
        "div > div")
    imuSubmitButton_loc = (                                                   # 添加imu的确定按钮
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div.ant-row-flex > div.ant-col-6 > div > div > div > "
        "div > div > button")
    imuCancelButton_loc = (                                                   # 添加imu的取消按钮
        By.CSS_SELECTOR,
        "#root > div > div > div[class^='section'] > div[class^='content'] > div > div[class^='undefined'] > div > "
        "div.ant-spin-nested-loading > div > div:nth-child(1) > div.ant-row-flex > div.ant-col-6 > div > div > div > "
        "div > div > button:nth-child(2)")
    ImuInfo_loc = (                                                           # 保存提示
        By.CSS_SELECTOR, 'div.ant-message > span > div > div > div > span')

    # 点击IMU配置按钮
    def click_imuButton(self):
        self.click(*self.imu_loc)

    # 根据IMU名称，点击编辑按钮
    def click_updateImuButton(self, imuName):
        n = self.get_elementNum(imuName, *self.imuNameList_loc)
        self.click(By.CSS_SELECTOR, "div[class^='undefined'] > div > div.ant-spin-nested-loading > div > "
                                    "div:nth-child(%s) > div.ant-row-flex > div.ant-col-6 > div > div > div > div > "
                                    "div > button" % n)

    # 根据IMU名称，点击删除按钮
    def click_deleteImuButton(self, imuName):
        n = self.get_elementNum(imuName, *self.imuNameList_loc)
        self.click(By.CSS_SELECTOR, "div[class^='undefined'] > div > div.ant-spin-nested-loading > div > "
                                    "div:nth-child(%s) > div.ant-row-flex > div.ant-col-6 > div > div > div > div > "
                                    "div > button:nth-child(2)" % n)

    # 点击所有展开按钮
    def click_allExpandButton(self):
        expandButtonList = self.find_elements(*self.expandButtonList_loc)
        for n in expandButtonList:
            for j in range(10):
                try:
                    n.click()
                    break
                except Exception:
                    sleep(0.5)

    # 根据IMU名称点击配置按钮
    def click_configureImuButton(self, imuName):
        n = self.get_elementNum(imuName, *self.imuNameList_loc)
        self.click(By.CSS_SELECTOR, "div[class^='undefined'] > div > div.ant-spin-nested-loading > div > "
                                    "div:nth-child(%s) > div[class^='role_content'] > div > div > button" % n)

    # 点击添加按钮
    def click_createImuButton(self):
        self.click(*self.createImuButton_loc)

    # 在imu添加页面，输入imu设备编码
    def input_imuCode(self, imuCode):
        self.find_element(*self.imuCodeInput_loc).send_keys(str(imuCode))

    # 在imu添加页面，输入imu名称（位置）
    def input_imuName(self, imuName):
        self.find_element(*self.imuNameInput_loc).send_keys(str(imuName))

    # 在imu添加页面，输入imu出厂日期
    def input_imuProduceDate(self, imuProduceDate):
        self.check_dataFormat(imuProduceDate)
        self.click(*self.imuProduceDateInput_loc)
        self.find_element(*self.calendarInput_loc).send_keys(str(imuProduceDate))
        self.click(*self.imuCodeInput_loc)

    # 在imu添加页面，输入出厂编号
    def input_imuProductCode(self, imuProductCode):
        self.find_element(*self.imuProductCodeInput_loc).send_keys(str(imuProductCode))

    # 在imu添加页面，选择通讯协议
    def input_imuProtocol(self, imuProtocol):
        self.click(*self.imuProtocolInput_loc)
        self.select_in_LastDiv(str(imuProtocol))

    # 在imu添加页面，选择是否支持223
    def input_imuSupportF223(self, imuSupportF223):
        self.click(*self.imuSupportF223Input_loc)
        self.select_in_LastDiv(str(imuSupportF223))

    # 在imu添加页面，输入软件版本
    def input_imuSoftwareVersion(self, imuSoftwareVersion):
        self.find_element(*self.imuSoftwareVersionInput_loc).send_keys(str(imuSoftwareVersion))

    # 在imu添加页面，输入反向链接IP地址
    def input_imuInvertingConnectIpAddress(self, imuInvertingConnectIpAddress):
        self.find_element(*self.imuInvertingConnectIpAddressInput_loc).send_keys(str(imuInvertingConnectIpAddress))

    # 在imu添加页面，输入反向链接端口号
    def input_imuInvertingConnectionPort(self, imuInvertingConnectionPort):
        self.find_element(*self.imuInvertingConnectionPortInput_loc).send_keys(str(imuInvertingConnectionPort))

    # 在imu添加页面，选择云端通信方式
    def input_imuCloudCommunicationStyle(self, imuCloudCommunicationStyle):
        self.click(*self.imuCloudCommunicationStyleInput_loc)
        self.select_in_LastDiv(str(imuCloudCommunicationStyle))

    # 在imu添加页面，选择无线通信方式
    def input_imuWirelessCommunicationStyle(self, imuWirelessCommunicationStyle):
        self.click(*self.imuWirelessCommunicationStyleInput_loc)
        self.select_in_LastDiv(str(imuWirelessCommunicationStyle))

    # 在imu添加页面，选择通信天线类型
    def input_imuCloudCommunicationAntennaType(self, imuCloudCommunicationAntennaType):
        self.click(*self.imuCloudCommunicationAntennaTypeInput_loc)
        self.select_in_LastDiv(str(imuCloudCommunicationAntennaType))

    # 在imu添加页面，输入SIM卡号
    def input_imuSimCode(self, imuSimCode):
        self.find_element(*self.imuSimCodeInput_loc).send_keys(str(imuSimCode))

    # 在imu添加页面，输入SIM卡产权
    def input_imuSimPropertyRights(self, imuSimPropertyRights):
        self.find_element(*self.imuSimPropertyRightsInput_loc).send_keys(str(imuSimPropertyRights))

    # 在imu添加页面，输入调试时间
    def input_imuDebugDate(self, imuDebugDate):
        self.click(*self.imuDebugDateInput_loc)
        self.find_element(*self.calendarInput_loc).send_keys(str(imuDebugDate))
        self.click(*self.imuCodeInput_loc)

    # 在imu添加页面，输入指导人员
    def input_imuGuider(self, imuGuider):
        self.find_element(*self.imuGuiderInput_loc).send_keys(str(imuGuider))

    # 在imu添加页面，输入安装人员
    def input_imuInstaller(self, imuInstaller):
        self.find_element(*self.imuInstallerInput_loc).send_keys(str(imuInstaller))

    # 在imu添加页面，输入投运日期
    def input_imuLaunchDate(self, imuLaunchDate):
        self.check_dataFormat(imuLaunchDate)
        self.click(*self.imuLaunchDateInput_loc)
        self.find_element(*self.calendarInput_loc).send_keys(str(imuLaunchDate))
        self.click(*self.imuCodeInput_loc)

    # 在imu添加页面，输入备注
    def input_imuRemark(self, imuRemark):
        self.find_element(*self.imuRemarkInput_loc).send_keys(str(imuRemark))

    # 获取通道类型列内容
    def get_imuAcquisitionAndCommunicationModeList(self):
        return self.get_infoList(*self.imuAcquisitionAndCommunicationModeList_loc)

    # 在imu添加页面，为所有通道类型为LAN的选择协议（默认为tcp-C）
    def input_allImuProtocolrole(self, ImuProtocolrole):
        imuAcquisitionAndCommunicationModeList = self.get_infoList(*self.imuAcquisitionAndCommunicationModeList_loc)
        i = 1
        for n in imuAcquisitionAndCommunicationModeList:
            if n == 'LAN':
                self.click(
                    By.CSS_SELECTOR, "div[class^='role___'] > div[class^='role_content'] > div > form > div.ant-row > "
                                     "div > div > div > div > div > div:nth-child(2) > div > div > div > div > div > "
                                     "div > table > tbody > tr:nth-child(%s) > td:nth-child(3) > div > div > div > "
                                     "div" % i)
                self.select_in_LastDiv(ImuProtocolrole[i - 1])
                i += 1

    # 在imu添加页面，为所有通道类型为LAN的输入目标IP
    def input_allImuIp(self,
                       ip       # 目标IP，list[str,str,......]，*.*.*.*
                       ):
        imuAcquisitionAndCommunicationModeList = self.get_infoList(*self.imuAcquisitionAndCommunicationModeList_loc)
        i = 1
        for n in imuAcquisitionAndCommunicationModeList:
            if n == 'LAN':
                self.find_element(
                    By.CSS_SELECTOR, "div[class^='role___'] > div[class^='role_content'] > div > form > div.ant-row > "
                                     "div > div > div > div > div > div:nth-child(2) > div > div > div > div > div > "
                                     "div > table > tbody > tr:nth-child(%s) > td:nth-child(4) > input" % i
                ).send_keys(str(ip[i - 1]))
                i += 1

    # 在imu添加页面，为所有通道类型为LAN的输入目标端口
    def input_allImuPort(self,
                         port       # 目标端口，list[str,str,......]
                         ):
        imuAcquisitionAndCommunicationModeList = self.get_infoList(*self.imuAcquisitionAndCommunicationModeList_loc)
        i = 1
        for n in imuAcquisitionAndCommunicationModeList:
            if n == 'LAN':
                self.find_element(
                    By.CSS_SELECTOR, "div[class^='role___'] > div[class^='role_content'] > div > form > div.ant-row > "
                                     "div > div > div > div > div > div:nth-child(2) > div > div > div > div > div > "
                                     "div > table > tbody > tr:nth-child(%s) > td:nth-child(5) > input" % i
                ).send_keys(str(port[i - 1]))
                i += 1

    # 在imu添加页面，为所有协议为UDP-C或UDP-S的输入组播地址
    def input_allImuBroadCast(self,
                              broadCast       # 组播地址，list[str,str,......]
                              ):
        imuProtocolroleList = self.get_infoList(*self.imuProtocolroleList_loc)
        i = 1
        for n in imuProtocolroleList:
            if n == 'UDP-C' or n == 'UDP-S':
                self.find_element(
                    By.CSS_SELECTOR, "div[class^='role___'] > div[class^='role_content'] > div > form > div.ant-row > "
                                     "div > div > div > div > div > div:nth-child(2) > div > div > div > div > div > "
                                     "div > table > tbody > tr:nth-child(%s) > td:nth-child(6) > input" % i
                ).send_keys(str(broadCast[i - 1]))
                i += 1

    # 在imu添加页面，点击确定按钮
    def click_createSubmit(self):
        self.click(*self.imuSubmitButton_loc)

    # 在imu添加页面，点击取消按钮
    def click_createCancel(self):
        self.click(*self.imuSubmitButton_loc)

    # 获取点击添加 / 删除 / 编辑等按钮后的页面顶部持续5秒的提示消息
    def get_imuInfo(self):
        try:
            ImuInfo = self.find_element(*self.ImuInfo_loc).text
        except Exception:
            ImuInfo = '未找到页面提示'
        return ImuInfo

    # 获取所有IMU名称标题行
    def query_imuNameList(self):
        return self.get_infoList(*self.imuNameList_loc)

    # 获取指定IMU的所有详细信息（前置条件：已经展开IMU详情）[[基本信息],[[通道1], [通道2], ......]]
    def query_imuDetail(self, imuName):
        imuDetail = []                                      # 存储所有信息
        basicInfo = []                                      # 存储基本信息
        portInfo = []                                       # 存储通道信息
        # 获取要查询的IMU对应的是第几个
        n = self.get_elementNum(imuName, *self.imuNameList_loc)
        # 获取基本信息
        basicInfo_loc = self.find_elements(
            By.CSS_SELECTOR, "div[class^='role___']:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > "
                             "div:nth-child(3) > div > div:nth-child(1) > div:nth-child(2) > div > span" % n)
        for m in basicInfo_loc:
            basicInfo.append(m.text)
        imuDetail.append(basicInfo)
        # 分别获取LAN和RS485下面的通道信息
        # 定位到LAN和RS485
        LANRS485_loc = self.find_elements(
            By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > "
                             "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > "
                             "div:nth-child(2) > div:nth-child(1) > div.ant-row > div:nth-child(1) > div > div > "
                             "div > div" % n)
        for i, m in enumerate(LANRS485_loc):
            # 定位到每一个通道
            everyPort_loc = self.find_elements(
                By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) "
                                 "> div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > "
                                 "div:nth-child(2) > div:nth-child(1) > div.ant-row > div:nth-child(1) > div > div "
                                 "> div > div:nth-child(%s) > div > div > div > div > div > div > table > tbody > "
                                 "tr" % (n, i+1))
            for j, o in enumerate(everyPort_loc):
                # 定位到每一个通道下的每一个字段信息
                everyPortInfo_loc = self.find_elements(
                    By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) "
                                     "> div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > "
                                     "div:nth-child(2) > div:nth-child(1) > div.ant-row > div:nth-child(1) > div > div "
                                     "> div > div:nth-child(%s) > div > div > div > div > div > div > table > tbody > "
                                     "tr:nth-child(%s) > td" % (n, i+1, j+1))
                # 获取每一个字段的信息
                everyPortInfo = []
                for p in everyPortInfo_loc:
                    tempdata = p.text
                    everyPortInfo.append(tempdata)
                portInfo.append(everyPortInfo)
        imuDetail.append(portInfo)
        return imuDetail
