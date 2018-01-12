# coding:utf-8
__author__ = 'luws'

from src.group.login import login
from src.group.customer import customer
from src.group.deviceManagement import deviceManagement
from src.group.employee import employee
from src.group.powerclient import powerclient
from src.group.primaryDevice import primaryDevice, circuit, switch, generatrix, generator, switchgear, transformer, substation
from src.group.imu import imu
from src.group.sensor import sensor
from selenium import webdriver
import random


driver = webdriver.Chrome()     # 浏览器驱动
randnum = random.randint(100000, 999999)     # 取一个随机六位数，用于命名
# 参数值
customerName = '测试服务商' + str(randnum)    # 服务商名称
customerShortName = '服简' + str(randnum)     # 服务商简称
companyName = '测试企业' + str(randnum)     # 企业名称
companyShortName = '企简' + str(randnum)     # 企业简称
companyShortName1 = '平台演进1009'     # 已有的企业名称
customerServiceProvider = '平台测试'    # 企业所属服务商
powerclientName = '测试站点' + str(randnum)  # 用电客户名称
powerClientShortName = '站简' + str(randnum)   # 用电客户简称
powerclientCode = str(randnum)   # 电力户号
employeeName = '测试账号' + str(randnum)     # 人员管理-员工姓名
employeeCellphone = '13777' + str(randnum)   # 人员管理-员工手机号
accountUsername = 'test' + str(randnum)[0:3]     # 平台账号-只取随机数前三位
substationName = '配电房'  # 配电房名称
circuitName = '回路'    # 回路名称后缀
switchName = '开关'    # 开关名称后缀
transformerName = '变压器'     # 变压器名称后缀
generatrixName = '母线'    # 母线名称后缀
sensorName = '传感器'     # 传感器名称后缀
generatorName = '发电机'   # 发电机名称后缀
switchgearName = '开关柜'  # 开关柜名称后缀
imuCode = '0002000199' + str(randnum)       # imu设备编码
imuName = 'imu'
imuProductCode = str(randnum)   # imu出厂编号
sensorChannelName = '1'
# 以下参数可以根据需要修改
circuitNum = 3  # 配电房下建回路的个数
switchNum = 2  # 配电房下建开关的个数
transformerNum = 1  # 配电房下建变压器的个数
generatrixNum = 1  # 配电房下建母线的个数
generatorNum = 1   # 配电房下建发电机的个数
switchgearNum = 1  # 配电房下建开关柜的个数

# 打开后台页面并登录
login(driver).login()

# 建服务商，输入必填字段
# customer(driver).create_Customer_inputRequired(customerName=customerName, customerShortName=customerShortName)

# 建一个人员并创建平台账号
# employee(driver).click_employeeButton()     # 点击人员管理Tab
# employee(driver).createEmployeeAndAccount(
#     employeeName=employeeName, employeeCellphone=employeeCellphone, accountUsername=accountUsername)
# print('平台账号：' + accountUsername)

# 建企业，输入必填字段
# customer(driver).click_customerManagementButton()   # 点击客户信息管理按钮
# customer(driver).create_company_inputRequired(
#     companyName=companyName, companyShortName=companyShortName, companyServiceProvider=customerName)    # companyServiceProvider字段是企业所属服务商可以修改

# 进入企业详情（没有建企业时使用）
customer(driver).query_customer(customerShortname=companyShortName1)

# 建用电客户，输入必填字段

powerclient(driver).click_powerclientButton()   # 点击用电客户信息按钮
powerclient(driver).create_powerclient_inputRequired(
    powerclientName=powerclientName, powerClientShortName=powerClientShortName, powerclientCode=randnum)

# 建一次设备台账
deviceManagement(driver).click_primaryDevice(powerClientName=powerclientName)   # 进入一次设备
primaryDevice(driver).createChildSubstation(powerclientName=powerclientName)    # 在之前的用电客户下,点击添加下级-配电房
substation(driver).create_substation_inputRequired(substationName)   # 填写配电房页面信息
primaryDevice(driver).submitCreate()  # 提交

for i in range(1, circuitNum+1):       # 在配电房下建N个回路，N=circuitNum
    circuitName1 = str(i) + '#' + circuitName   # 回路名称命名
    primaryDevice(driver).createChildDevice(parentDevice=substationName, childDeviceType='回路')   # 点击添加下级-回路，修改parentDevice可修改上级设备
    circuit(driver).create_circuit_inputRequired(circuitName=circuitName1)    # 填写回路页面信息
    primaryDevice(driver).submitCreate()     # 提交
    if i <= switchNum:  # 给每个回路建一个开关
        switchName1 = str(i) + '#' + switchName   # 开关名称命名
        primaryDevice(driver).createChildDevice(parentDevice=circuitName1, childDeviceType='开关')   # 点击添加下级-开关
        switch(driver).create_switch_inputRequired(switchName=switchName1)       # 填写开关页面信息
        primaryDevice(driver).submitCreate()     # 提交
    if i <= transformerNum:     # 建变压器
        transformerName1 = str(i) + '#' + transformerName  # 变压器名称命名
        primaryDevice(driver).createChildDevice(parentDevice=substationName, childDeviceType='变压器')  # 点击添加下级-变压器
        transformer(driver).create_transformer_inputRequired(transformerName=transformerName1,
                                                             transformerNextCircuit=circuitName1)  # 填写变压器页面信息
        primaryDevice(driver).submitCreate()  # 提交
for i in range(1, generatrixNum+1):     # 建母线
    generatrixName1 = str(i) + '#' + generatrixName   # 母线名称命名
    primaryDevice(driver).createChildDevice(parentDevice=substationName, childDeviceType='母线')  # 点击添加下级-母线
    generatrix(driver).create_generatrix_inputRequired(generatrixName=generatrixName1)  # 填写变压器页面信息
    primaryDevice(driver).submitCreate()  # 提交
for i in range(1, generatorNum + 1):    # 建发电机
    generatorName1 = str(i) + '#' + generatorName   # 发电机名称命名
    primaryDevice(driver).createChildDevice(parentDevice=substationName, childDeviceType='自备发电机')  # 点击添加下级-发电机
    generator(driver).create_generator_inputRequired(generatorName=generatorName1)  # 填写发电机页面信息
    primaryDevice(driver).submitCreate()  # 提交
for i in range(1, switchgearNum + 1):   # 建开关柜
    switchgearName1 = str(i) + '#' + switchgearName  # 开关柜名称命名
    primaryDevice(driver).createChildDevice(parentDevice=substationName, childDeviceType='开关柜')  # 点击添加下级-开关柜
    switchgear(driver).create_switchgear_inputRequired(switchgearName=switchgearName1)  # 填写开关柜页面信息
    primaryDevice(driver).submitCreate()  # 提交

    circuitName1 = circuitName  # 回路名称初始化
    switchName1 = switchName    # 开关名称初始化
    transformerName1 = transformerName  # 变压器名称初始化
    generatrixName1 = generatrixName    # 母线名称初始化
    generatorName1 = generatorName  # 发电机名称初始化
    switchgearName1 = switchgearName    # 开关柜名称初始化

# 挂接二次设备
primaryDevice(driver).click_GoToSecondaryDeviceButton()     # 从一次设备右上角的二次设备维护按钮进入二次设备
# deviceManagement(driver).click_secondaryDeviceButton(powerClientName=powerclientName)       # 从首页根据用电客户名称进入二次设备，用于已有用电客户，只建设备台账
imu(driver).create_imu_inputRequired(imuCode=imuCode, imuName=imuName, imuProductCode=imuProductCode)    # 创建imu
sensor(driver).click_sensor()   # 进入传感器配置页面

sensorNum = 1    # 测量点号&通信地址，每次循环+1

for i in range(1, circuitNum+1):    # 给回路建传感器
    circuitName1 = str(i) + '#' + circuitName  # 回路的传感器名称命名
    sensor(driver).create_sensor_inputRequired(
        sensorName=circuitName1, sensorDtuCode=imuCode, sensorChannelName=sensorChannelName,
        monitoredObject=circuitName1, sensorMeasuringPointSequence=sensorNum, sensorAddress=sensorNum, sensorModel='所有数据项')  # 创建传感器，如需变更传感器型号，需修改sensorModel的值
    circuitName1 = circuitName  # 回路的传感器名称初始化
    sensorNum += 1

for i in range(1, switchNum+1):     # 给开关建传感器
    switchName1 = str(i) + '#' + switchName     # 开关的传感器名称命名
    sensor(driver).create_sensor_inputRequired(
        sensorName=switchName1, sensorDtuCode=imuCode, sensorChannelName=sensorChannelName, monitoredObject=switchName1,
        monitoredObjectType='开关', sensorMeasuringPointSequence=sensorNum, sensorAddress=sensorNum, sensorModel='所有数据项')
    switchName1 = switchName    # 开关的传感器名称初始化
    sensorNum += 1

for i in range(1, generatrixNum+1):     # 给母线建传感器
    generatrixName1 = str(i) + '#' + generatrixName     # 母线的传感器名称命名
    sensor(driver).create_sensor_inputRequired(
        sensorName=generatrixName1, sensorDtuCode=imuCode, sensorChannelName=sensorChannelName, monitoredObject=generatrixName1,
        monitoredObjectType='母线', sensorMeasuringPointSequence=sensorNum, sensorAddress=sensorNum, sensorModel='所有数据项')
    generatrixName1 = generatrixName    # 母线的传感器名称初始化
    sensorNum += 1

for i in range(1, generatorNum+1):     # 给发电机建传感器
    generatorName1 = str(i) + '#' + generatorName     # 发电机的传感器名称命名
    sensor(driver).create_sensor_inputRequired(
        sensorName=generatorName1, sensorDtuCode=imuCode, sensorChannelName=sensorChannelName, monitoredObject=generatorName1,
        monitoredObjectType='发电机', sensorMeasuringPointSequence=sensorNum, sensorAddress=sensorNum, sensorModel='所有数据项')
    generatorName1 = generatorName    # 发电机的传感器名称初始化
    sensorNum += 1

driver.quit()
