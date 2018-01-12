# coding:utf-8
__author__ = 'luws'
from src.pages.imuModel_page import imuModel_page
from src.common.log import log
'''
IMU模板组合方法
'''


class imu_model(imuModel_page):

    # 创建IMU模板，输入所有字段
    def create_imuModel_inputAll(self, imuModelName,  # IMU型号,str
                                 imuModelModel,  # IMU型号编码,str
                                 imuModelProductName='中恒',  # 生产厂家,str
                                 imuModelCloudCommunicationStyle='有线',  # 默认云端通信方式,str
                                 imuModelSupportF223='是',  # 是否支持223,str
                                 remark='',  # 备注,str
                                 acquisitionAndCommunicationMode='串口,串口',  # 通道类型,list[str, str,......],长度=portNum
                                 portNum=2  # 通道数,int
                                 ):
        # 校验参数合法性
        try:
            assert portNum == len(acquisitionAndCommunicationMode), '参数错误：通道类型list长度不等于通道数'
        except AssertionError:
            log().error('参数错误：通道类型list长度不等于通道数')

        # action
        self.click_model()
        self.click_createImuModel()
        self.input_imuModelName(imuModelName)
        self.input_imuModelModel(imuModelModel)
        self.input_imuModelProductName(imuModelProductName)
        self.input_imuModelCloudCommunicationStyle(imuModelCloudCommunicationStyle)
        self.input_imuModelSupportF223(imuModelSupportF223)
        self.input_remark(remark)
        for i in range(1, portNum+1):
            self.click_createPort()
            self.input_acquisitionAndCommunicationMode(i, acquisitionAndCommunicationMode[i-1])
        self.click_submit()

    # 创建IMU模板，只输入必填字段，只建一个通道
    def create_imuModel_inputRequired(
            self,
            imuModelName,                                       # IMU型号,str
            imuModelModel,                                      # IMU型号编码,str
            imuModelProductName='中恒',                         # 生产厂家,str
            imuModelCloudCommunicationStyle='有线',             # 默认云端通信方式,str
            acquisitionAndCommunicationMode='串口',             # 通道类型,str
    ):

        # action
        self.click_model()
        self.click_createImuModel()
        self.input_imuModelName(imuModelName)
        self.input_imuModelModel(imuModelModel)
        self.input_imuModelProductName(imuModelProductName)
        self.input_imuModelCloudCommunicationStyle(imuModelCloudCommunicationStyle)
        self.click_createPort()
        self.input_acquisitionAndCommunicationMode(1, acquisitionAndCommunicationMode)
        self.click_submit()

    # 删除指定名称的IMU模板
    def delete_imuModel(
            self,
            imuModelName                                # 要删除的IMU模板名称
    ):

        # action
        self.click_model()
        self.click_deleteImuModel(imuModelName)
        self.click_submitDelectImuModel()
