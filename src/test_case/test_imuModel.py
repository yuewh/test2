# coding:utf-8
__author__ = 'luws'

import unittest
from selenium import webdriver
from src.common.excel_data import excel_data
from src.group.imuModel import imu_model
from src.group.login import login

'''
IMU模板页面测试
'''


class TestImuModel(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        login(self.driver).login('admin_yny', '123456')
        self.imuModel = imu_model(self.driver)
        self.sheetname = 'imuModel'
        self.testdata = excel_data().get_list(self.sheetname)

    def tearDown(self):
        self.driver.quit()

    def test_createImuModel_inputAll(self):
        """创建imu模板：输入所有字段,验证提示信息是否正确"""
        testdata = self.testdata[0]
        self.imuModel.create_imuModel_inputAll(
            imuModelName=testdata[1], imuModelModel=testdata[2], imuModelProductName=testdata[3],
            imuModelCloudCommunicationStyle=testdata[4], imuModelSupportF223=testdata[5], remark=testdata[6],
            acquisitionAndCommunicationMode=testdata[7].split(','), portNum=int(testdata[8])
        )
        getInfo = self.imuModel.get_ImuModelInfo()
        try:
            self.assertEqual(getInfo, testdata[9], self.sheetname + testdata[0] + '测试失败：' + getInfo)
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])

    def test_createImuModel_inputRequired(self):
        """创建imu模板：输入必填字段,验证提示信息是否正确"""
        testdata = self.testdata[1]
        self.imuModel.create_imuModel_inputRequired(
            imuModelName=testdata[1], imuModelModel=testdata[2], imuModelProductName=testdata[3],
            imuModelCloudCommunicationStyle=testdata[4], acquisitionAndCommunicationMode=testdata[7]
        )
        getInfo = self.imuModel.get_ImuModelInfo()
        try:
            self.assertEqual(getInfo, testdata[9], self.sheetname + testdata[0] + '测试失败：' + getInfo)
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])

    def test_createImuModel_detail(self):
        """创建imu模板：输入所有字段,验证详情内容是否与输入值一致"""
        testdata = self.testdata[2]
        self.imuModel.create_imuModel_inputAll(
            imuModelName=testdata[1], imuModelModel=testdata[2], imuModelProductName=testdata[3],
            imuModelCloudCommunicationStyle=testdata[4], imuModelSupportF223=testdata[5], remark=testdata[6],
            acquisitionAndCommunicationMode=testdata[7].split(','), portNum=int(testdata[8])
        )
        # 验证IMU模板列表中是否有刚才创建的那个
        imuModelNameList = self.imuModel.query_imuModelNameList()
        try:
            self.assertIn(testdata[1], imuModelNameList, self.sheetname + testdata[0] + '测试失败：未找到' + testdata[1])
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])

        # 验证详情各字段内容是否正确
        self.imuModel.click_queryImuModel(imuModelName=testdata[1])
        imuModelDetail = self.imuModel.query_imuModelDetail()
        basicInfo = imuModelDetail[0]
        portInfo = imuModelDetail[1]
        # print(basicInfo)
        # print(portInfo)
        # 验证基本信息是否正确
        try:
            self.assertEqual(basicInfo[0], testdata[1], '测试失败：保存后IMU模板型号不一致')
            self.assertEqual(basicInfo[1], testdata[2], '测试失败：保存后IMU模板型号编码不一致')
            self.assertEqual(basicInfo[2], testdata[3], '测试失败：保存后IMU模板生产厂家不一致')
            self.assertEqual(basicInfo[3], testdata[9], '测试失败：保存后IMU模板厂商编码不一致')
            self.assertEqual(basicInfo[4], testdata[4], '测试失败：保存后IMU模板默认云端通信方式不一致')
            self.assertEqual(basicInfo[5], testdata[5], '测试失败：保存后IMU模板是否支持223不一致')
            self.assertEqual(basicInfo[6], testdata[6], '测试失败：保存后IMU模板备注不一致')
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])

        # 验证通道个数是否正确
        try:
            self.assertEqual(testdata[8], len(portInfo), '测试失败：保存后通道数量不一致')
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])
        # 验证每个通道是否正确
        for i in range(len(portInfo)):
            portDetail = portInfo[i]                # 获取的IMU模板详情中的通道列表，一个通道为一个list
            portType = testdata[7].split(',')       # 测试数据中的通道类型列表
            try:
                self.assertEqual(portDetail[0], portDetail[1], '测试失败：通道号有误')
                self.assertEqual(portDetail[2], portType[i], '测试失败：%s通道类型有误' % portDetail[1])
            except AssertionError:
                self.imuModel.img_screenshot(testdata[0])

    def test_deleteImuModel(self):
        """删除IMU模板：验证删除后该IMU是否还在列表中"""
        testdata = self.testdata[3]
        self.imuModel.create_imuModel_inputRequired(
            imuModelName=testdata[1], imuModelModel=testdata[2], imuModelProductName=testdata[3],
            imuModelCloudCommunicationStyle=testdata[4], acquisitionAndCommunicationMode=testdata[7])
        # 验证IMU模板列表中是否有刚才创建的那个
        imuModelNameList = self.imuModel.query_imuModelNameList()
        try:
            self.assertIn(testdata[1], imuModelNameList, self.sheetname + testdata[0] + '测试失败：未找到' + testdata[1])
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])
        # 执行删除
        self.imuModel.click_deleteImuModel(testdata[1])
        self.imuModel.click_submitDelectImuModel()

        # 验证IMU模板列表中是否有刚才创建的那个
        imuModelNameList = self.imuModel.query_imuModelNameList()
        try:
            self.assertNotIn(testdata[1], imuModelNameList, self.sheetname + testdata[0] + '测试失败：未找到' + testdata[1])
        except AssertionError:
            self.imuModel.img_screenshot(testdata[0])

    def test_deleteImuModel_info(self):
        """删除IMU模板：验证删除后页面提示是否正确，此处使用之前用例中已经创建的数据"""
        testdata = self.testdata[4]
        self.imuModel.delete_imuModel(testdata[1])
        getInfo = self.imuModel.get_ImuModelInfo()
        try:
            self.assertEqual(getInfo, self.testdata[9], self.sheetname + testdata[0] + '测试失败：' + getInfo)
        except AssertionError:
            self.imuModel.img_screenshot(self.testdata[0])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestImuModel('test_deleteImuModel'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
