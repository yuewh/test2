# coding:utf-8
__author__ = 'luws'
from src.pages.primaryDevice_page import primaryDevice_page
from src.pages.circuit_page import circuit_page
from src.pages.switch_page import switch_page
from src.pages.generatrix_page import generatrix_page
from src.pages.generator_page import generator_page
from src.pages.switchgear_page import switchgear_page
from src.pages.transformer_page import transformer_page
from src.pages.substation_page import substation_page
from time import sleep

'''
一次设备页面公用方法
'''


class primaryDevice(primaryDevice_page):
    # 添加非配电房的设备
    # 给parentDevice添加类型为childDeviceType的下级设备,相当于点击添加按钮，填写页面信息的方法在对应设备层级的类中
    def createChildDevice(self, parentDevice, childDeviceType):
        for i in range(10):
            try:
                self.click_primaryDeviceName(parentDevice)
                break
            except Exception:
                sleep(0.5)
        sleep(0.5)
        self.click_createChildDevice()
        # try:
        self.click_createChildDeviceType(childDeviceType)
        # except AssertionError:
        #     sleep(0.5)
        #     self.click_createChildDevice()
        #     self.click_createChildDevice()
        #     self.click_createChildDeviceType(childDeviceType)

    # 添加配电房
    def createChildSubstation(self, powerclientName):
        self.click_primaryDeviceName(powerclientName)
        self.click_createChildDevice()

    # 删除设备层级
    def deletePrimaryDevice(self, primaryDeviceName):
        self.click_primaryDeviceName(primaryDeviceName)
        self.click_deletePrimaryDeviceButton()
        self.click_submitdeletePrimaryDeviceButton()
        msg = self.get_primaryDeviceInfo()
        self.click_closePrimaryDeviceInfo()
        return msg

    # 编辑一个设备层级
    def updatePrimaryDevice(self, primaryDeviceName):
        self.click_primaryDeviceName(primaryDeviceName)
        self.click_updatePrimaryDeviceButton()

    # 非配电房的层级，新增设备层级，点击确认按钮，并返回页面提示
    def submitCreate(self):
        self.click_submitCreatePrimaryDeviceButton()
        msg = self.get_primaryDeviceInfo()
        self.click_closePrimaryDeviceInfo()
        sleep(1)
        return msg


'''
回路页面方法
'''


class circuit(circuit_page):
    # 新增回路，输入必填项
    def create_circuit_inputRequired(self, circuitName,  # 回路名称
                                     circuitIsContactCircuit='否',  # 是否联络回路
                                     circleRatedVoltage='交流220V'  # 额定电压
                                     ):
        self.input_circuitName(circuitName)
        self.input_circuitIsContactCircuit(circuitIsContactCircuit)
        self.input_circleRatedVoltage(circleRatedVoltage)

    # 新增回路，输入所有项（是否联络回路选否）
    def create_circuit_inputAll(self, circuitName,  # 回路名称
                                circuitPurpose='其他',  # 负荷用途
                                circuitIsContactCircuit='否',  # 是否联络回路
                                circleRatedVoltage='交流220V'  # 额定电压
                                ):
        self.input_circuitName(circuitName)
        self.input_circuitPurpose(circuitPurpose)
        self.input_circuitIsContactCircuit(circuitIsContactCircuit)
        self.input_circleRatedVoltage(circleRatedVoltage)


'''
开关页面方法
'''


class switch(switch_page):
    def create_switch_inputRequired(self, switchName,  # 开关名称
                                    switchType='负荷开关',  # 开关类型
                                    ):
        self.input_switchName(switchName)
        self.input_switchType(switchType)

    def create_switch_inputAll(self, switchName,  # 开关名称
                               switchType='负荷开关',  # 开关类型
                               switchStandbyType='进线',  # 开关作用
                               switchModel='',  # 开关型号
                               switchRatedVoltage='',  # 开关额定电压
                               switchRatedCurrent='',  # 开关额定电流
                               switchRemark='',  # 开关备注
                               ):
        self.input_switchName(switchName)
        self.input_switchType(switchType)
        self.input_switchStandbyType(switchStandbyType)
        self.input_switchModel(switchModel)
        self.input_switchRatedVoltage(switchRatedVoltage)
        self.input_switchRatedCurrent(switchRatedCurrent)
        self.input_switchRemark(switchRemark)


'''
母线页面方法
'''


class generatrix(generatrix_page):
    def create_generatrix_inputRequired(self, generatrixName  # 母线名称
                                        ):
        self.input_generatrixName(generatrixName)

    def create_generatrix_inputAll(self, generatrixName,  # 母线名称
                                   generatrixRatedVoltage='',  # 额定电压
                                   generatrixSpecifications='',  # 规格
                                   generatrixModel='',  # 型号
                                   generatrixRatedLoadFlow='',  # 额定载流量
                                   generatrixRemark='',  # 备注
                                   ):
        self.input_generatrixName(generatrixName)
        self.input_generatrixRatedVoltage(generatrixRatedVoltage)
        self.input_generatrixSpecifications(generatrixSpecifications)
        self.input_generatrixModel(generatrixModel)
        self.input_generatrixRatedLoadFlow(generatrixRatedLoadFlow)
        self.input_generatrixRemark(generatrixRemark)


'''
发电机页面方法
'''


class generator(generator_page):
    # 创建发电机，输入必填字段
    def create_generator_inputRequired(self, generatorName,  # 发电机名称
                                       generatorRatedPower='100',  # 额定功率
                                       generatorRatedPowerFactor='0.9',  # 额定功率因数
                                       generatorRatedVoltage='220',  # 额定电压
                                       ):
        self.input_generatorName(generatorName)
        self.input_generatorRatedPower(generatorRatedPower)
        self.input_generatorRatedPowerFactor(generatorRatedPowerFactor)
        self.input_generatorRatedVoltage(generatorRatedVoltage)

    # 创建发电机，输入所有字段
    def create_generator_inputAll(self, generatorName,  # 发电机名称
                                  generatorModel='',  # 型号
                                  generatorRatedPower='100',  # 额定功率
                                  generatorRatedPowerFactor='0.9',  # 额定功率因数
                                  generatorRatedVoltage='220',  # 额定电压
                                  generatorRatedCapacity='',  # 额定容量
                                  generatorRatedSpeed='',  # 额定转速
                                  generatorRatedCurrent='',  # 额定电流
                                  generatorRemake='',  # 备注
                                  ):
        self.input_generatorName(generatorName)
        self.input_generatorModel(generatorModel)
        self.input_generatorRatedPower(generatorRatedPower)
        self.input_generatorRatedCapacity(generatorRatedCapacity)
        self.input_generatorRatedPowerFactor(generatorRatedPowerFactor)
        self.input_generatorRatedVoltage(generatorRatedVoltage)
        self.input_generatorRatedSpeed(generatorRatedSpeed)
        self.input_generatorRatedCurrent(generatorRatedCurrent)
        self.input_generatorRemark(generatorRemake)


'''
开关柜页面方法
'''


class switchgear(switchgear_page):
    # 创建开关柜，输入必填字段
    def create_switchgear_inputRequired(self, switchgearName):
        self.input_switchgearName(switchgearName)

    # 创建开关柜，输入所有字段
    def create_switchgear_inputAll(self, switchgearName,  # 开关柜名称
                                   switchgearSerialNumber='',  # 开关柜编号
                                   switchgearDeviceType=''  # 开关柜型号
                                   ):
        self.input_switchgearName(switchgearName)
        self.input_switchgearSerialNumber(switchgearSerialNumber)
        self.input_switchgearDeviceType(switchgearDeviceType)


'''
变压器页面方法
'''


class transformer(transformer_page):
    # 创建变压器，输入必填字段
    def create_transformer_inputRequired(self, transformerNextCircuit,  # 变压器下级开关回路
                                         transformerName,  # 设备名称
                                         transformerStandbyType='主供电源',  # 变压器主备性质
                                         transformerRatedCapacity='1000',  # 额定容量
                                         transformerVoltageRatio='10/0.4',  # 电压比
                                         ):
        self.input_transformerNextCircuit(transformerNextCircuit)
        self.input_transformerName(transformerName)
        self.inpue_transformerStandbyType(transformerStandbyType)
        self.input_transformerRatedCapacity(transformerRatedCapacity)
        self.input_transformerVoltageRatio(transformerVoltageRatio)

    # 创建变压器，输入所有字段
    def create_transformer_inputAll(self, transformerPreviousCircuit,  # 变压器上级开关回路
                                    transformerNextCircuit,  # 变压器下级开关回路
                                    transformerName,  # 设备名称
                                    transformerStandbyType='主供电源',  # 变压器主备性质
                                    transformerModel='',  # 型号
                                    transformerProductor='',  # 生产厂家
                                    transformerProductCode='',  # 出厂编号
                                    transformerProductDate='2017-10-10',  # 出厂日期
                                    transformerRatedCapacity='1000',  # 额定容量
                                    transformerInsulatingMedium='干式',  # 绝缘介质
                                    transformerIsAmorphous='是',  # 是否非晶变
                                    transformerNoLoadCurrent='',  # 空载电流
                                    transformerShortCircuitLoss='',  # 短路损耗
                                    transformerNoLoadLoss='',  # 空载损耗
                                    transformerLoadLoss='',  # 负载损耗
                                    transformerVoltageRatio='10/0.4',  # 电压比
                                    transformerOilNumber='10',  # 油号
                                    transformerOilWeight='',  # 油重
                                    transformerTotalWeight='',  # 总重
                                    transformerShortCircuitImpedance='',  # 短路阻抗
                                    transformerInsulationAndHeatResistanceLevel='A',  # 绝缘耐热等级
                                    transformerEarthingResistance='',  # 接地电阻
                                    transformerWiringGroup='Yz11',  # 接线组别
                                    transformerCoolingMethod='风冷',  # 冷却方式
                                    transformerIsEarthed='是',  # 低压中性点接地标志
                                    transformerLaunchDate='2017-10-11',  # 投运日期
                                    transformerInstallDate='2017-10-12',  # 安装日期
                                    transformerEnableDate='2017-10-13',  # 实际启用日期
                                    transformerDisableDate='2017-10-14',  # 实际停用日期
                                    transformerPlannedResumeDate='2017-10-15',  # 计划恢复日期
                                    transformerChangeCapacity='',  # 变动容量
                                    transformerExpireDate='2017-10-16',  # 到期日期
                                    transformerIsWholeLowerMonitored='是',  # 下级是否全监测
                                    transformerRemark='',  # 备注
                                    ):
        # 校验字段
        if transformerLaunchDate <= transformerInstallDate:
            self.mylog.info('参数错误：投运日期应大于等于安装日期')
        # action
        self.input_transformerPreviousCircuit(transformerPreviousCircuit)
        self.input_transformerNextCircuit(transformerNextCircuit)
        self.input_transformerName(transformerName)
        self.inpue_transformerStandbyType(transformerStandbyType)
        self.input_transformerModel(transformerModel)
        self.input_transformerProductor(transformerProductor)
        self.input_transformerProductCode(transformerProductCode)
        self.input_transformerProductDate(transformerProductDate)
        self.input_transformerRatedCapacity(transformerRatedCapacity)
        self.input_transformerInsulatingMedium(transformerInsulatingMedium)
        self.input_transformerIsAmorphous(transformerIsAmorphous)
        self.input_transformerNoLoadCurrent(transformerNoLoadCurrent)
        self.input_transformerShortCircuitLoss(transformerShortCircuitLoss)
        self.input_transformerNoLoadLoss(transformerNoLoadLoss)
        self.input_transformerLoadLoss(transformerLoadLoss)
        self.input_transformerVoltageRatio(transformerVoltageRatio)
        self.input_transformerOilNumber(transformerOilNumber)
        self.input_transformerOilWeight(transformerOilWeight)
        self.input_transformerTotalWeight(transformerTotalWeight)
        self.input_transformerShortCircuitImpedance(transformerShortCircuitImpedance)
        self.input_transformerInsulationAndHeatResistanceLevel(transformerInsulationAndHeatResistanceLevel)
        self.input_transformerEarthingResistance(transformerEarthingResistance)
        self.input_transformerWiringGroup(transformerWiringGroup)
        self.input_transformerCoolingMethod(transformerCoolingMethod)
        self.input_transformerIsEarthed(transformerIsEarthed)
        self.input_transformerLaunchDate(transformerLaunchDate)
        self.input_transformerInstallDate(transformerInstallDate)
        self.input_transformerEnableDate(transformerEnableDate)
        self.input_transformerDisableDate(transformerDisableDate)
        self.input_transformerPlannedResumeDate(transformerPlannedResumeDate)
        self.input_transformerChangeCapacity(transformerChangeCapacity)
        self.input_transformerExpireDate(transformerExpireDate)
        self.input_transformerIsWholeLowerMonitored(transformerIsWholeLowerMonitored)
        self.input_transformerRemark(transformerRemark)


'''
配电房页面方法
'''


class substation(substation_page):
    # 创建配电房，输入必填字段
    def create_substation_inputRequired(self, substationName,  # 配电房名称
                                        substationNetworkCondition='有线',  # 现场网络情况
                                        ):
        self.input_substationName(substationName)
        self.input_substationNetworkCondition(substationNetworkCondition)

    # 创建配电房，输入所有字段（不输入代维单位和配电房地址）
    def create_substation_inputAll(self, substationName,  # 配电房名称
                                   substationLaunchDate='2017-10-10',  # 投运日期
                                   substationReactivePowerCompensationCapacity='',  # 无功补偿容量
                                   substationInterlockingType='机械闭锁',  # 防误方式
                                   substationIsIndependentBuilding='是',  # 是否独立建筑物
                                   substationPosition='地上',  # 配电房位置
                                   substationEarthingResistance='',  # 接地电阻
                                   substationNetworkCondition='有线',  # 现场网络情况
                                   substationBandwidth='有线带宽50M',  # 信号类型
                                   substationRemark=''  # 备注
                                   ):
        self.input_substationName(substationName)
        self.input_substationLaunchDate(substationLaunchDate)
        self.input_substationReactivePowerCompensationCapacity(substationReactivePowerCompensationCapacity)
        self.input_substationInterlockingType(substationInterlockingType)
        self.input_substationIsIndependentBuilding(substationIsIndependentBuilding)
        self.input_substationPosition(substationPosition)
        self.input_substationEarthingResistance(substationEarthingResistance)
        self.input_substationNetworkCondition(substationNetworkCondition)
        self.input_substationBandwidth(substationBandwidth)
        self.input_substationRemark(substationRemark)