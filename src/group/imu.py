# coding:utf-8
__author__ = 'luws'
from src.pages.imu_page import imu_page
from time import sleep
from selenium.common.exceptions import TimeoutException
'''
二次设备-IMU-组合方法
'''


class imu(imu_page):
    # 创建imu，输入必填字段(imu编码对应的通信协议只有串口，没有LAN，云端通信方式选有线，不用增加填写的字段)
    def create_imu_inputRequired(self,
                                 imuCode,  # imu设备编码,00020001开头
                                 imuName,  # imu名称（位置）
                                 imuProductCode,  # 出厂编号
                                 imuProtocol='376.1',  # 通讯协议
                                 imuSupportF223='是',  # 是否支持223
                                 imuCloudCommunicationStyle='有线',  # 云端通信方式
                                 ):
        self.click_createImuButton()
        try:
            self.input_imuCode(imuCode)
            self.input_imuName(imuName)
            self.input_imuProductCode(imuProductCode)
            self.input_imuProtocol(imuProtocol)
            self.input_imuSupportF223(imuSupportF223)
            self.input_imuCloudCommunicationStyle(imuCloudCommunicationStyle)
            self.click_createSubmit()
        except Exception:
            self.click_createImuButton()
            self.input_imuCode(imuCode)
            self.input_imuName(imuName)
            self.input_imuProductCode(imuProductCode)
            self.input_imuProtocol(imuProtocol)
            self.input_imuSupportF223(imuSupportF223)
            self.input_imuCloudCommunicationStyle(imuCloudCommunicationStyle)
            self.click_createSubmit()

    # 创建imu，输入所有字段(imu编码对应的通信协议只有串口，没有LAN)
    def create_imu_inputAll(self,
                            imuCode,  # imu设备编码,00020001开头
                            imuName,  # imu名称（位置）
                            imuProduceDate,  # 出厂日期
                            imuProductCode,  # 出厂编号
                            imuProtocol='376.1',  # 通讯协议
                            imuSupportF223='是',  # 是否支持223
                            imuSoftwareVersion='',  # 软件版本
                            imuInvertingConnectIpAddress='',  # 反向链接IP地址
                            imuInvertingConnectionPort='',  # 反向链接端口号
                            imuCloudCommunicationStyle='有线',  # 云端通信方式
                            imuDebugDate='2017-11-11',  # 调试时间
                            imuGuider='',  # 指导人员
                            imuInstaller='',  # 安装人员
                            imuLaunchDate='2017-11-11',  # 投运日期
                            imuRemark='',  # 备注
                            imuWirelessCommunicationStyle='',  # 无线通信方式

                            imuCloudCommunicationAntennaType='',  # 通信天线类型
                            imuSimCode='',  # SIM卡号
                            imuSimPropertyRights='',  # SIM卡产权
                            allImuProtocolrole='',  # 通道类型为LAN的协议
                            allImuIp='',  # 通道类型为LAN的目标IP
                            allImuPort='',  # 通道类型为LAN的目标端口
                            allImuBroadCast='',  # 通道类型为LAN,协议为UDP-C或UDP-S的组播地址
                            ):
        self.click_createImuButton()
        self.input_imuCode(imuCode)
        self.input_imuName(imuName)
        self.input_imuProduceDate(imuProduceDate)
        self.input_imuProductCode(imuProductCode)
        self.input_imuProtocol(imuProtocol)
        self.input_imuSupportF223(imuSupportF223)
        self.input_imuSoftwareVersion(imuSoftwareVersion)
        self.input_imuInvertingConnectIpAddress(imuInvertingConnectIpAddress)
        self.input_imuInvertingConnectionPort(imuInvertingConnectionPort)
        self.input_imuCloudCommunicationStyle(imuCloudCommunicationStyle)
        if imuCloudCommunicationStyle == '无线':
            self.input_imuWirelessCommunicationStyle(imuWirelessCommunicationStyle)
            self.input_imuCloudCommunicationAntennaType(imuCloudCommunicationAntennaType)
            self.input_imuSimCode(imuSimCode)
            self.input_imuSimPropertyRights(imuSimPropertyRights)
        self.input_imuDebugDate(imuDebugDate)
        self.input_imuGuider(imuGuider)
        self.input_imuInstaller(imuInstaller)
        self.input_imuLaunchDate(imuLaunchDate)
        self.input_imuRemark(imuRemark)
        if 'LAN' in self.get_imuAcquisitionAndCommunicationModeList():
            self.input_allImuProtocolrole(allImuProtocolrole)
            self.input_allImuIp(allImuIp)
            self.input_allImuPort(allImuPort)
            if ('UDP-C' in allImuProtocolrole) or ('UDP-S' in allImuProtocolrole):
                self.input_allImuBroadCast(allImuBroadCast)
        self.click_createSubmit()

    # 删除指定名称的imu
    def delete_imu(self,
                   imuName,                                                 # 要删除的imu名称（位置）
                   ):
        self.click_deleteImuButton(imuName)
