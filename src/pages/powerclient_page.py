# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.pages.employee_page import employee_page
from time import sleep

'''
客户管理-用电客户信息页面基本方法
用电客户信息页面个元素定位都和人员信息页面相同，这个页面的方法直接调用人员管理页面的，只是重新命名
'''


class powerclient_page(employee_page):
    """定位器"""
    """用电客户信息页面"""
    powerclientButton_loc = (                                                               # 用电客户信息按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.row.search-pan > div > div:nth-child(3)')
    """添加页面"""
    powerclientName_loc = (By.ID, 'powerClientName ')                                       # 用电客户名称
    powerClientShortName_loc = (By.ID, 'powerClientShortName')                              # 用电客户简称
    powerClientElectricCategory_loc = (                                                     # 用电类别
        By.CSS_SELECTOR, "select[data-ng-model='model.electricCategory']")
    powerclientSupplyVoltage_loc = (By.ID, 'powerSupplyVoltage ')                           # 供电电压
    powerclientSupplyVoltageSelectList_loc = (By.CSS_SELECTOR, 'ul.down-list.wid-98 > li')  # 供电电压选项list
    powerClientPowerNumber_loc = (                                                          # 进线数目
        By.CSS_SELECTOR, "select[data-ng-model='model.powerNumber ']")
    powerClientContractCapacity_loc = (By.CSS_SELECTOR, "input[name='contractCapacity ']")  # 合同容量
    powerclientIndustry_loc = (                                                             # 选择行业按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(9) > div > div')
    powerclientIndustrySearchInput_loc = (                                                  # 选择行业弹窗中的搜索输入栏
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.row > form > '
                         'div > input')
    powerclientIndustrySearchButton_loc = (                                                 # 选择行业弹窗中的搜索按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.row > form > '
                         'div > button')
    powerclientIndustryName_loc = (                                                         # 选择行业弹窗中的行业名称字段
        By.CSS_SELECTOR, 'div.fl-left.ng-isolate-scope.ellipsis > label')
    powerclientIndustryButtonList_loc = (                                                   # 选择行业弹窗中的单选框
        By.CSS_SELECTOR, 'div.fl-left.mg-rt6p.mg-top3p > label.radio-btn > span.toggle-radio')
    submitPowerclientIndustryButton_loc = (                                                 # 选择行业弹窗中的确定按钮
        By.CSS_SELECTOR, 'div.modal-footer.text-center > button:nth-child(1)')
    cancelPowerclientIndustryButton_loc = (                                                 # 选择行业弹窗中的取消按钮
        By.CSS_SELECTOR, 'div.modal-footer.text-center > button:nth-child(2)')
    powerclientCode_loc = (By.ID, 'powerClientCode ')                                       # 电力户号
    powerClientProjectAccessStage_loc = (                                                   # 工程接入状态
        By.CSS_SELECTOR, "select[data-ng-model='model.projectAccessStage']")
    powerclientVideoUrl_loc = (By.CSS_SELECTOR, "input[name='videoUrl']")                   # 视频地址
    powerclientProvince_loc = (By.CSS_SELECTOR, "select[name='province']")                  # 用电地址-省
    powerclientCity_loc = (By.CSS_SELECTOR, "select[name='city']")                          # 用电地址-市
    powerclientCounty_loc = (By.CSS_SELECTOR, "select[name='county']")                      # 用电地址-区
    powerclientStreetCode_loc = (By.CSS_SELECTOR, "input[name='streetCode']")               # 用电地址-街道
    powerclientAddress_loc = (By.CSS_SELECTOR, "input[name='address']")                     # 用电地址-详细地址
    powerclientQueryLatitudeAndLongitudeButton_loc = (                                      # 查询经纬度按钮
        By.CSS_SELECTOR, "input[value='查询经纬度']")
    powerclientLongitude_loc = (By.CSS_SELECTOR, "input[name='longitude']")                 # 经度
    powerclientLatitude_loc = (By.CSS_SELECTOR, "input[name='latitude']")                   # 经度
    powerclientMeterReadingDay_loc = (By.CSS_SELECTOR, "input[name='meterReadingDay ']")    # 抄表结算日
    powerclientMonitoringLevel_loc = (                                                      # 接入监测级别
        By.CSS_SELECTOR, "select[data-ng-model='model.monitoringLevel ']")
    powerclientIsPowerGenerator_is_loc = (                                                  # 是否发电上网用户-是
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(18) > div > div:nth-child(1) > '
                         'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio')
    powerclientIsPowerGenerator_not_loc = (                                                 # 是否发电上网用户-否
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(18) > div > div:nth-child(2) > '
                         'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio')
    powerclientIsValid_is_loc = (                                                           # 商务有效性-有效
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(19) > div > div:nth-child(1) > '
                         'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio')
    powerclientIsValid_not_loc = (                                                          # 商务有效性-无效
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(19) > div > div:nth-child(2) > '
                         'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio')
    powerclientIsWholeGatewayMonitored_is_loc = (                                           # 关口是否全监测-是
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(20) > div > div:nth-child(1) > '
                         'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio')
    powerclientIsWholeGatewayMonitored_not_loc = (                                          # 关口是否全监测-否
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(20) > div > div:nth-child(2) > '
                         'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio')
    submitCreatePowerclientButton_loc = (                                                    # 保存按钮
        By.CSS_SELECTOR, 'div.form-group.col-sm-7.col-md-6.col-lg-5.col-sm-push-5.col-md-push-4.col-lg-push-4.mg-top30p'
                         ' > button:nth-child(1)')
    cancelCreatePowerclientButton_loc = (                                                    # 取消按钮
        By.CSS_SELECTOR, 'div.form-group.col-sm-7.col-md-6.col-lg-5.col-sm-push-5.col-md-push-4.col-lg-push-4.mg-top30p'
                         ' > button:nth-child(2)')

    # 点击用电客户信息按钮
    def click_powerclientButton(self):
        self.click(*self.powerclientButton_loc)

    # 点击添加按钮
    def click_createPowerclientButton(self):
        self.click_createEmployeeButton()

    # 根据用电客户名称，点击列表中的编辑按钮
    def click_updatePowerclientButton_inList(self, powerclientName):
        self.click_updateEmployeeButton_inList(powerclientName)

    # 根据用电客户名称，点击列表中的删除按钮
    def click_deletePowerclientButton(self, powerclientName):
        self.click_deleteEmployeeButton(powerclientName)

    # 点击删除确认弹窗中的确定按钮
    def click_click_submitDeletePowerclientButton(self):
        self.click_submitDeleteEmployeeButton()

    # 点击删除确认弹窗中的取消按钮
    def click_cancelDeletePowerclientButton(self):
        self.click_cancelDeleteEmployeeButton()

    # 点击详情中的编辑按钮
    def click_updatePowerclientButton_inDetail(self):
        self.click_updateEmployeeButton_inDetail()

    # 根据用电客户名称，点击某一行数据，展开详情(此处点击的是用电客户名称栏)
    def click_powerclientName(self, powerclientName):
        self.click_employeeName(powerclientName)

    # 在添加页面，输入用电客户名称
    def input_powerclientName(self, powerclientName):
        self.send_keys(str(powerclientName), *self.powerclientName_loc)

    # 在添加页面，输入用电客户简称
    def input_powerClientShortName(self, powerClientShortName):
        self.send_keys(powerClientShortName, *self.powerClientShortName_loc)

    # 在添加页面，选择用电类别
    def input_powerClientElectricCategory(self, powerClientElectricCategory):
        self.select_by_option(powerClientElectricCategory, *self.powerClientElectricCategory_loc)

    # 在添加页面，输入供电电压
    def input_powerclientSupplyVoltage(self, powerclientSupplyVoltage):
        self.click(*self.powerclientSupplyVoltage_loc)
        self.click_valueFromList(powerclientSupplyVoltage, self.powerclientSupplyVoltageSelectList_loc)

    # 在添加页面，输入进线数目
    def input_powerClientPowerNumber(self, powerClientPowerNumber):
        self.select_by_option(powerClientPowerNumber, *self.powerClientPowerNumber_loc)

    # 在添加页面，输入合同容量
    def input_powerClientContractCapacity(self, powerClientContractCapacity):
        self.send_keys(powerClientContractCapacity, *self.powerClientContractCapacity_loc)

    # 在添加页面，点击选择行业按钮
    def click_powerclientIndustryButton(self):
        self.click(*self.powerclientIndustry_loc)

    # 在添加页面，选择行业弹窗，搜索关键字
    def search_powerclientIndustry(self, powerclientIndustryKey):
        self.send_keys(powerclientIndustryKey, *self.powerclientIndustrySearchInput_loc)
        self.click(*self.powerclientIndustrySearchButton_loc)
        sleep(0.5)

    # 在添加页面，选择行业弹窗，点击要选择的行业对应的单选框
    def click_powerclientIndustry(self, powerclientIndustry):
        n = self.get_elementNum(powerclientIndustry, *self.powerclientIndustryName_loc)
        powerclientIndustryButtonList_loc = self.find_elements(*self.powerclientIndustryButtonList_loc)
        powerclientIndustryButtonList_loc[n-1].click()

    # 在添加页面，选择行业弹窗，点击确定按钮
    def click_submitPowerclientIndustryButton(self):
        self.click(*self.submitPowerclientIndustryButton_loc)

    # 在添加页面，选择行业弹窗，点击取消按钮
    def click_cancelPowerclientIndustryButton(self):
        self.click(*self.cancelPowerclientIndustryButton_loc)

    # 在添加页面，输入电力户号
    def input_powerclientCode(self, powerclientCode):
        self.send_keys(powerclientCode, *self.powerclientCode_loc)

    # 在添加页面，选择工程接入阶段
    def input_powerClientProjectAccessStage(self, powerClientProjectAccessStage):
        self.select_by_option(powerClientProjectAccessStage, *self.powerClientProjectAccessStage_loc)

    # 在添加页面，输入视频地址
    def input_powerclientVideoUrl(self, powerclientVideoUrl):
        self.send_keys(powerclientVideoUrl, *self.powerclientVideoUrl_loc)

    # 在添加页面，选择用电客户所在省
    def input_powerclientProvince(self, powerclientProvince):
        self.select_by_option(powerclientProvince, *self.powerclientProvince_loc)

    # 在添加页面，选择用电客户所在市
    def input_powerclientCity(self, powerclientCity):
        self.select_by_option(powerclientCity, *self.powerclientCity_loc)

    # 在添加页面，选择用电客户所在区
    def input_powerclientCounty(self, powerclientCounty):
        self.select_by_option(powerclientCounty, *self.powerclientCounty_loc)

    # 在添加页面，输入街道
    def input_powerclientStreetCode(self, powerclientStreetCode):
        self.send_keys(powerclientStreetCode, *self.powerclientStreetCode_loc)

    # 在添加页面，输入详细地址
    def input_powerclientAddress(self, powerclientAddress):
        self.send_keys(powerclientAddress, *self.powerclientAddress_loc)

    # 在添加页面，获取详细地址
    def get_powerclientAddress(self):
        powerclientAddress = self.find_element(*self.powerclientAddress_loc)
        return powerclientAddress.text

    # 在添加页面，点击查询经纬度
    def click_powerclientQueryLatitudeAndLongitudeButton(self):
        self.click(*self.powerclientQueryLatitudeAndLongitudeButton_loc)

    # 在添加页面，输入经度
    def input_powerclientLongitude(self, powerclientLongitude):
        self.send_keys(powerclientLongitude, *self.powerclientLongitude_loc)

    # 在添加页面，输入纬度
    def input_powerclientLatitude(self, powerclientLatitude):
        self.send_keys(powerclientLatitude, *self.powerclientLatitude_loc)

    # 在添加页面，输入抄表结算日
    def input_powerclientMeterReadingDay(self, powerclientMeterReadingDay):
        self.send_keys(powerclientMeterReadingDay, *self.powerclientMeterReadingDay_loc)

    # 在添加页面，选择接入监测级别
    def input_powerclientMonitoringLevel(self, powerclientMonitoringLevel):
        self.select_by_option(powerclientMonitoringLevel, *self.powerclientMonitoringLevel_loc)

    # 在添加页面，选择是否发电上网用户
    def input_powerclientIsPowerGenerator(self, powerclientIsPowerGenerator):
        try:
            assert str(powerclientIsPowerGenerator) == '是' or str(powerclientIsPowerGenerator) == '否', \
                '参数错误：powerclientIsPowerGenerator应输入是或否'
        except AssertionError:
            self.mylog.error('参数错误：powerclientIsPowerGenerator应输入是或否')
        if str(powerclientIsPowerGenerator) == '是':
            self.click(*self.powerclientIsPowerGenerator_is_loc)
        else:
            self.click(*self.powerclientIsPowerGenerator_not_loc)

    # 在添加页面，选择商务有效性
    def input_powerclientIsValid(self, powerclientIsValid):
        try:
            assert str(powerclientIsValid) == '有效' or str(powerclientIsValid) == '无效', \
                '参数错误：powerclientIsValid应输入有效或无效'
        except AssertionError:
            self.mylog.error('参数错误：powerclientIsValid应输入有效或无效')
        if str(powerclientIsValid) == '有效':
            self.click(*self.powerclientIsValid_is_loc)
        else:
            self.click(*self.powerclientIsValid_not_loc)

    # 在添加页面，选择关口是否全监测
    def input_powerclientIsWholeGatewayMonitored(self, powerclientIsWholeGatewayMonitored):
        try:
            assert str(powerclientIsWholeGatewayMonitored) == '是' or str(powerclientIsWholeGatewayMonitored) == '否', \
                '参数错误：powerclientIsWholeGatewayMonitored应输入是或否'
        except AssertionError:
            self.mylog.error('参数错误：powerclientIsWholeGatewayMonitored应输入是或否')
        if str(powerclientIsWholeGatewayMonitored) == '是':
            self.click(*self.powerclientIsWholeGatewayMonitored_is_loc)
        else:
            self.click(*self.powerclientIsWholeGatewayMonitored_not_loc)

    # 在添加页面，点击保存按钮
    def click_submitCreatePowerclientButton(self):
        self.click(*self.submitCreatePowerclientButton_loc)

    # 在添加页面，点击取消按钮
    def click_cancelCreatePowerclientButton(self):
        self.click(*self.cancelCreatePowerclientButton_loc)

    # 获取弹窗提示
    def get_powerclientInfo(self):
        self.get_employeeInfo()

    # 点击弹窗提示中的立即关闭按钮
    def click_closePowerclientInfo(self):
        self.click_closeEmployeeInfo()
