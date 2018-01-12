# coding:utf-8
__author__ = 'luws'
from src.pages.sensor_page import sensor_page
from time import sleep
'''
二次设备-传感器-组合方法
'''


class sensor(sensor_page):
    # 全绑定信号量至单个监测对象,开关全绑定遥信量，其他全绑定遥测量
    def bindPoint(self,
                  monitoredObject,                              # 监测对象
                  monitoredObjectType,                          # 监测对象类型,(配电房；变压器；回路；开关；发电机；母线)
                  sensorPositionDescribe='开关上端',             # 监测点位置
                  sensorMonitoringLevel='关口',                  # 监测点级别
                  sensorIsUsedCalculateResult='是'               # 是否用于计量结算
                  ):
        # 校验字段

        # action
        self.click_bindPoint(monitoredObject)
        sleep(1)
        if monitoredObjectType == '配电房' or monitoredObjectType == '回路' or monitoredObjectType == '变压器':
            self.input_sensorPositionDescribe(sensorPositionDescribe)
        if monitoredObjectType == '回路':
            self.input_sensorMonitoringLevel(sensorMonitoringLevel)
            self.input_sensorIsUsedCalculateResult(sensorIsUsedCalculateResult)

        self.click_metricTypeSelectButton()
        if monitoredObjectType == '开关':
            self.input_metricType('遥测')
        else:
            self.input_metricType('遥信')
        self.click_searchMetricTypeButton()
        self.click_bindAll()

    # 创建传感器，输入必填字段
    def create_sensor_inputRequired(self,
                                    sensorName,  # 传感器名称（位置）
                                    sensorDtuCode,  # 对应通信管理机
                                    sensorChannelName,  # 对应通道
                                    monitoredObject,  # 监测对象
                                    monitoredObjectType='回路',  # 监测对象类型,(配电房；变压器；回路；开关；发电机；母线)
                                    sensorMeasuringPointSequence=1,  # 测量点序号
                                    sensorAddress=1,  # 通信地址
                                    sensorDtuType='IMU',  # 对应通信管理机类型
                                    sensorType='表计类',  # 传感器类型
                                    sensorModel='常用告警',  # 传感器型号
                                    sensorPropertyRight='云能源',  # 产权
                                    sensorPositionDescribe='开关上端',  # 监测点位置
                                    sensorMonitoringLevel='关口',  # 监测点级别
                                    sensorIsUsedCalculateResult='是'  # 是否用于计量结算
                                    ):

        # action
        # 点击添加按钮
        self.click_createSensorButton()
        # 输入必填信息
        self.input_sensorName(sensorName)
        self.input_sensorType(sensorType)
        sleep(1)
        self.input_sensorModel(sensorModel)
        self.input_sensorPropertyRight(sensorPropertyRight)
        self.input_sensorMeasuringPointSequence(sensorMeasuringPointSequence)
        self.input_sensorAddress(sensorAddress)
        self.input_sensorDtuType(sensorDtuType)
        self.input_sensorDtuCode(sensorDtuCode)
        self.input_sensorChannelName(sensorChannelName)
        # 挂接
        self.bindPoint(monitoredObject, monitoredObjectType, sensorPositionDescribe, sensorMonitoringLevel,
                       sensorIsUsedCalculateResult)
        # 点击保存按钮
        self.click_submitCreateSensorButton()

    # 创建传感器，输入所有字段（非必填字段可选填）
    def create_sensor_inputAll(self,
                               sensorName,  # 传感器名称（位置）
                               sensorDtuCode,  # 对应通信管理机
                               sensorChannelName,  # 对应通道
                               monitoredObject,  # 监测对象
                               monitoredObjectType='回路',  # 监测对象类型,(配电房；变压器；回路；开关；发电机；母线)
                               sensorType='表计类',  # 传感器类型
                               sensorModel='常用告警',  # 传感器型号
                               sensorPropertyRight='云能源',  # 产权
                               sensorMeasuringPointSequence=1,  # 测量点序号
                               sensorAddress=1,  # 通信地址
                               sensorDtuType='IMU',  # 对应通信管理机类型
                               sensorProductCode='',  # 出厂编号
                               sensorProduceDate='2017-10-10',  # 出厂日期
                               sensorSupplyPhase='A相',  # 供电相位
                               sensorCt='10/5',  # CT变比
                               sensorPt='27500/100',  # PT变比
                               sensorEquipmentStatus='正常',  # 设备状态
                               sensorInstallDate='2017-10-10',  # 调试日期
                               sensorLaunchDate='2017-10-10',  # 投运日期
                               sensorRemark='',  # 备注
                               sensorPositionDescribe='开关上端',  # 监测点位置
                               sensorMonitoringLevel='关口',  # 监测点级别
                               sensorIsUsedCalculateResult='是'  # 是否用于计量结算
                               ):

        # action
        # 点击添加按钮
        self.click_createSensorButton()
        # 输入所有信息
        self.input_sensorName(sensorName)
        self.input_sensorType(sensorType)
        self.input_sensorModel(sensorModel)
        self.input_sensorProductCode(sensorProductCode)
        self.input_sensorProduceDate(sensorProduceDate)
        self.input_sensorPropertyRight(sensorPropertyRight)
        self.input_sensorMeasuringPointSequence(sensorMeasuringPointSequence)
        self.input_sensorAddress(sensorAddress)
        self.input_sensorDtuType(sensorDtuType)
        self.input_sensorDtuCode(sensorDtuCode)
        self.input_sensorChannelName(sensorChannelName)
        self.input_sensorSupplyPhase(sensorSupplyPhase)
        self.input_sensorCt(sensorCt)
        self.input_sensorPt(sensorPt)
        self.input_sensorEquipmentStatus(sensorEquipmentStatus)
        self.input_sensorInstallDate(sensorInstallDate)
        self.input_sensorLaunchDate(sensorLaunchDate)
        self.input_sensorRemark(sensorRemark)
        # 挂接
        self.bindPoint(monitoredObject, monitoredObjectType, sensorPositionDescribe, sensorMonitoringLevel,
                       sensorIsUsedCalculateResult)
        # 点击保存按钮
        self.click_submitCreateSensorButton()

    # 删除一个传感器
    def delete_sensor(self,
                      sensorName                                        # 要删除的传感器的名称
                      ):
        self.click_deleteSensorButton(sensorName)
        self.click_submitDeleteSensorButton()

    # N次复制
    def copy_sensor(self, sensorName, copyNum):
        self.click_selectAllsensorButton()
        # self.click_selectOneSensorButton(sensorName)
        self.click_copySensorButton()
        sleep(1)
        self.input_sensorCopyNum(copyNum)
        self.click_submitCopySensorNumButton()
