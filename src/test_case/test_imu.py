# coding:utf-8
__author__ = 'luws'

import unittest
from selenium import webdriver
from src.common.excel_data import excel_data
from src.group.deviceManagement import deviceManagement
from src.group.imu import imu
from src.group.login import login

'''
二次设备-IMU页面测试
'''


class TestImu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        login(self.driver).login()
        deviceManagement(self.driver).click_secondaryDevice('1113')
        self.imu = imu(self.driver)
        self.sheetname = 'imu'
        self.testdata = excel_data().get_list(self.sheetname)

    def tearDown(self):
        self.driver.quit()

    def test_createImu_inputAll(self):
        """创建imu：输入所有字段,验证提示信息是否正确"""
        testdata = self.testdata[0]
        self.imu.create_imu_inputAll(
            imuCode=testdata[1], imuName=testdata[2], imuProduceDate=testdata[3], imuProductCode=testdata[4],
            imuProtocol=testdata[5], imuSupportF223=testdata[6], imuSoftwareVersion=testdata[7],
            imuInvertingConnectIpAddress=testdata[8], imuInvertingConnectionPort=testdata[9],
            imuCloudCommunicationStyle=testdata[10], imuDebugDate=testdata[11], imuGuider=testdata[12],
            imuInstaller=testdata[13], imuLaunchDate=testdata[14], imuRemark=testdata[15],
            imuWirelessCommunicationStyle=testdata[16], imuCloudCommunicationAntennaType=testdata[17],
            imuSimCode=testdata[18], imuSimPropertyRights=testdata[19], allImuProtocolrole=testdata[20],
            allImuIp=testdata[21], allImuPort=testdata[22], allImuBroadCast=testdata[23])
        getInfo = self.imu.get_imuInfo()
        try:
            self.assertEqual(getInfo, testdata[24], self.sheetname + testdata[0] + '测试失败：' + getInfo)
        except AssertionError:
            self.imu.img_screenshot(testdata[0])

    def test_createImu_inputRequired(self):
        """创建imu：输入必填字段,验证提示信息是否正确"""
        testdata = self.testdata[1]
        self.imu.create_imu_inputRequired(
            imuCode=testdata[1], imuName=testdata[2], imuProductCode=testdata[4], imuProtocol=testdata[5],
            imuSupportF223=testdata[6])
        getInfo = self.imu.get_imuInfo()
        try:
            self.assertEqual(getInfo, testdata[24], self.sheetname + testdata[0] + '测试失败：' + getInfo)
        except AssertionError:
            self.imu.img_screenshot(testdata[0])

    def test_deleteImu_info(self):
        """删除未挂接传感器的IMU：验证删除后页面提示是否正确，此处使用之前用例中已经创建的数据"""
        testdata = self.testdata[2]
        self.imu.delete_imu(testdata[2])
        getInfo = self.imu.get_imuInfo()
        try:
            self.assertEqual(getInfo, self.testdata[24], self.sheetname + testdata[0] + '测试失败：' + getInfo)
        except AssertionError:
            self.imu.img_screenshot(self.testdata[24])

    def test_deleteImu(self):
        """删除未挂接传感器的IMU：验证删除后该IMU是否还在列表中"""
        testdata = self.testdata[3]
        # 先创建一个IMU，一会删除它
        self.imu.create_imu_inputRequired(imuCode=testdata[1], imuName=testdata[2], imuProductCode=testdata[4],
                                          imuProtocol=testdata[5], imuSupportF223=testdata[6])
        # 验证IMU列表中是否有它
        imuNameList = self.imu.query_imuNameList()
        try:
            self.assertIn(self.testdata[2], imuNameList, self.sheetname + testdata[0] + '测试失败：创建IMU失败')
        except AssertionError:
            self.imu.img_screenshot(self.testdata[0])
        # 删除这个imu
        self.imu.delete_imu(imuName=testdata[2])
        # 验证IMU列表中是否没有了
        imuNameList = self.imu.query_imuNameList()
        try:
            self.assertNotIn(self.testdata[2], imuNameList, self.sheetname + testdata[0] + '测试失败：删除IMU失败')
        except AssertionError:
            self.imu.img_screenshot(self.testdata[0])
