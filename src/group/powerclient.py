# coding:utf-8
__author__ = 'luws'
from src.pages.powerclient_page import powerclient_page
from time import sleep

'''
用电客户信息页面组合方法
'''


class powerclient(powerclient_page):
    # 在添加页面，选择行业
    def input_powerclientIndustry(self, powerclientIndustry):
        self.click_powerclientIndustryButton()
        self.search_powerclientIndustry(powerclientIndustry)
        sleep(0.5)
        self.click_powerclientIndustry(powerclientIndustry)
        self.click_submitPowerclientIndustryButton()

    # 创建一个用电客户，输入必填字段（从点击添加按钮开始,不修改用电地址）
    def create_powerclient_inputRequired(self, powerclientName,  # 用电客户名称
                                         powerClientShortName,  # 用电客户简称
                                         powerclientCode,  # 电力户号
                                         powerClientElectricCategory='大工业用电',  # 用电类别
                                         powerClientContractCapacity='10000',  # 合同容量
                                         powerclientIndustry='食品制造业',  # 行业
                                         powerClientProjectAccessStage='试运行阶段',  # 工程接入阶段
                                         ):
        self.click_createPowerclientButton()
        self.input_powerclientName(powerclientName)
        self.click_powerclientQueryLatitudeAndLongitudeButton()     # 早点点查询，因为查询以后还需要等待
        self.input_powerClientShortName(powerClientShortName)
        self.input_powerClientElectricCategory(powerClientElectricCategory)
        self.input_powerClientContractCapacity(powerClientContractCapacity)
        self.input_powerclientIndustry(powerclientIndustry)
        self.input_powerclientCode(powerclientCode)
        self.input_powerClientProjectAccessStage(powerClientProjectAccessStage)
        self.click_submitCreatePowerclientButton()
        msg = ''
        try:
            msg = self.get_employeeInfo()
        except Exception:
            self.click_submitCreatePowerclientButton()
        self.click_closePowerclientInfo()
        return msg

    # 创建一个用电客户，输入所有字段（从点击添加按钮开始）
    def create_powerclient_inputAll(self, powerclientName,  # 用电客户名称
                                    powerClientShortName,  # 用电客户简称
                                    powerclientCode,  # 电力户号
                                    powerClientElectricCategory='大工业用电',  # 用电类别
                                    powerclientSupplyVoltage='交流110V',  # 供电电压
                                    powerClientPowerNumber='双电源',  # 进线数目
                                    powerClientContractCapacity='10000',  # 合同容量
                                    powerclientIndustry='食品制造业',  # 行业
                                    powerClientProjectAccessStage='现场安装阶段',  # 工程接入阶段
                                    powerclientVideoUrl='',  # 视频地址
                                    powerclientProvince='安徽省',  # 用电客户所在省
                                    powerclientCity='宣城市',  # 用电客户所在市
                                    powerclientCounty='广德县',  # 用电客户所在区
                                    powerclientStreetCode='',  # 街道
                                    powerclientMeterReadingDay='15',  # 抄表结算日
                                    powerclientMonitoringLevel='关口',  # 接入监测级别
                                    powerclientIsPowerGenerator='是',  # 是否发电上网用户
                                    powerclientIsValid='有效',  # 商务有效性
                                    powerclientIsWholeGatewayMonitored='是',  # 关口是否全监测
                                    ):
        self.click_createPowerclientButton()
        self.input_powerclientName(powerclientName)
        self.input_powerClientShortName(powerClientShortName)
        self.input_powerClientElectricCategory(powerClientElectricCategory)
        self.input_powerclientSupplyVoltage(powerclientSupplyVoltage)
        self.input_powerClientPowerNumber(powerClientPowerNumber)
        self.input_powerClientContractCapacity(powerClientContractCapacity)
        self.input_powerclientIndustry(powerclientIndustry)
        self.input_powerclientCode(powerclientCode)
        self.input_powerClientProjectAccessStage(powerClientProjectAccessStage)
        self.input_powerclientVideoUrl(powerclientVideoUrl)
        self.input_powerclientProvince(powerclientProvince)
        self.input_powerclientCity(powerclientCity)
        self.input_powerclientCounty(powerclientCounty)
        self.input_powerclientStreetCode(powerclientStreetCode)
        self.click_powerclientQueryLatitudeAndLongitudeButton()
        self.input_powerclientMeterReadingDay(powerclientMeterReadingDay)
        self.input_powerclientMonitoringLevel(powerclientMonitoringLevel)
        self.input_powerclientIsPowerGenerator(powerclientIsPowerGenerator)
        self.input_powerclientIsValid(powerclientIsValid)
        self.input_powerclientIsWholeGatewayMonitored(powerclientIsWholeGatewayMonitored)
        # 点击保存按钮
        self.click_submitCreatePowerclientButton()
        msg = self.get_employeeInfo()
        self.click_closePowerclientInfo()
        return msg

    # 删除一个用电客户
    def delete_powerclient(self, powerclientName):
        self.click_deletePowerclientButton(powerclientName)
        self.click_click_submitDeletePowerclientButton()
