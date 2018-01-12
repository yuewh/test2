# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from time import sleep

'''
异常规则库基本方法
'''


class alarmRuleBank_page(BasePage):
    """定位器"""
    alarmRuleBankButton_loc = (By.CSS_SELECTOR, "li[title='异常规则库'] > a")  # 左侧异常规则库TAB按钮
    # 主页面
    # 查询区域，与alarmRuleManager_page相同

    # 按钮区域
    createAlarmRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='toolkit'] > "
                         "div:nth-child(1) > button")  # 新增规则按钮
    deleteAlarmRUleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='toolkit'] > "
                         "div:nth-child(2) > button")  # 批量删除按钮

    # 新增规则页面(仅支持单因子)
    metricItemSelect_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > form > div:nth-child(1) > div.ant-form-item-control-wrapper.ant-col-xs-24."
                         "ant-col-sm-14 > div > div > div:nth-child(1) > label > span.ant-radio")  # 数据类型：遥信
    analogItemSelect_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > form > div:nth-child(1) > div.ant-form-item-control-wrapper.ant-col-xs-24."
                         "ant-col-sm-14 > div > div > div:nth-child(2) > label > span.ant-radio")  # 数据类型：遥测
    alarmRuleCategorySelect_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > form > div:nth-child(2) > div.ant-form-item-control-wrapper.ant-col-xs-24."
                         "ant-col-sm-14 > div > div > div > div")  # 规则类型选择栏
    alarmRuleNameInput_loc = (By.ID, "ruleName")  # 规则名称输入栏
    alarmRuleTypeSelect_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > form > div:nth-child(4) > div.ant-form-item-control-wrapper.ant-col-xs-24."
                         "ant-col-sm-14 > div > div > div > div")  # 异常类型选择栏

    alarmRuleEvaluateValueInput_loc = (By.ID, "evaluateValue")  # 持续时间输入栏
    alarmRuleReminderIntervalInput_loc = (By.ID, "reminderInterval")  # 提醒间隔输入栏

    addFormulaAButton_loc = (
        By.CSS_SELECTOR, "div[class^='tableWrapper'] > div[class^='addFactorWrapper'] > div > button")  # 新增因子按钮
    advancedSettingButton_loc = (By.CSS_SELECTOR, "div[class*='advanceBtn']")  # 高级设置按钮

    # 操作按钮
    submitCreateAlarmRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > form > div[class*='mgtop50'] > div.ant-col-14 > div > div > div > div:nth-child(1) > "
                         "button")  # 保存按钮
    cancelCreateAlarmRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > form > div[class*='mgtop50'] > div.ant-col-14 > div > div > div > div:nth-child(2) > "
                         "button")  # 取消按钮

    # action
    # 点击左侧异常规则库TAB按钮
    def click_alarmRuleBankButton(self):
        self.click(*self.alarmRuleBankButton_loc)

    # 点击新增规则按钮
    def click_createAlarmRuleButton(self):
        self.click(*self.createAlarmRuleButton_loc)

    # 选择数据类型
    def input_alarmRuleAssignedType(self, alarmRuleAssignedType):
        try:
            assert str(alarmRuleAssignedType) == '遥测' or str(alarmRuleAssignedType) == '遥信', '参数错误：assignedType应输入遥信或遥测'
        except AssertionError:
            self.mylog.error('参数错误：assignedType应输入遥信或遥测')
        if str(alarmRuleAssignedType) == '遥信':
            self.click(*self.metricItemSelect_loc)
        else:
            self.click(*self.analogItemSelect_loc)

    # 选择规则类型
    def input_alarmRuleCategory(self, alarmRuleCategory):
        self.click(*self.alarmRuleCategorySelect_loc)
        self.select_in_LastDiv(alarmRuleCategory)

    # 输入规则名称
    def input_alarmRuleName(self, alarmRuleName):
        self.send_keys(alarmRuleName, *self.alarmRuleNameInput_loc)

    # 选择异常类型
    def input_alarmRuleType(self, alarmRuleType):
        self.click(*self.alarmRuleTypeSelect_loc)
        self.select_in_LastDiv(alarmRuleType)

    # 输入规则描述
    # 输入或选择下限值-参数
    def input_alarmRuleFrontMetricCode(self, value,  # 值
                                       formulaListB,  # 当前因子中第几个公式
                                       formulaListA  # 第几个因子
                                       ):
        alarmRuleFrontMetricCodeInput_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(1) > div > div > div > "
                             "div > ul > li > div > input" % (formulaListA * 2 - 1, formulaListB))  # 下限值-参数-输入栏
        alarmRuleFrontMetricCodeSelect_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(1) > div > div > "
                             "div" % (formulaListA * 2 - 1, formulaListB))  # 下限值-参数-选择栏
        if type(value) == int or type(value) == float:
            self.send_keys(value, *alarmRuleFrontMetricCodeInput_loc)
        elif type(value) == str:
            self.click(*alarmRuleFrontMetricCodeSelect_loc)
            self.select_in_LastDiv(value)

    # 选择下限值-运算符
    def input_alarmOperator1(self, value, formulaListB,  # 当前因子中第几个公式
                             formulaListA  # 第几个因子
                             ):
        alarmOperator1Select_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(2) > div > div > "
                             "div" % (formulaListA * 2 - 1, formulaListB))  # 下限值-运算符-选择栏
        self.click(*alarmOperator1Select_loc)
        self.select_in_LastDiv(value)

    # 输入下限值-系数
    def input_alarmRuleFrontRatio(self, value, formulaListB,  # 当前因子中第几个公式
                                  formulaListA  # 第几个因子
                                  ):
        alarmRuleFrontRatioInput_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(3) > "
                             "input" % (formulaListA * 2 - 1, formulaListB))  # 下限值-系数-输入栏
        self.send_keys(value, *alarmRuleFrontRatioInput_loc)

    # 选择数据项
    def input_alarmRuleMetricCode(self, value, formulaListB,  # 当前因子中第几个公式
                                  formulaListA  # 第几个因子
                                  ):
        alarmRuleMetricCodeSelect_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(4) > div > div > "
                             "div" % (formulaListA * 2 - 1, formulaListB))  # 数据项
        self.click(*alarmRuleMetricCodeSelect_loc)
        self.select_in_LastDiv(value)

    # 输入或选择上限值-参数
    def input_alarmRuleBackMetricCode(self, value, formulaListB,  # 当前因子中第几个公式
                                      formulaListA  # 第几个因子
                                      ):
        alarmRuleBackMetricCodeInput_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(5) > div > div > div > "
                             "div > ul > li > div > input" % (formulaListA * 2 - 1, formulaListB))  # 上限值-参数-输入栏
        alarmRuleBackMetricCodeSelect_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(5) > div > div > "
                             "div" % (formulaListA * 2 - 1, formulaListB))  # 上限值-参数-选择栏
        if type(value) == int or type(value) == float:
            self.send_keys(value, *alarmRuleBackMetricCodeInput_loc)
        elif type(value) == str:
            self.click(*alarmRuleBackMetricCodeSelect_loc)
            self.select_in_LastDiv(value)

    # 选择上限值-运算符
    def input_alarmOperator2(self, value, formulaListB,  # 当前因子中第几个公式
                             formulaListA  # 第几个因子
                             ):
        alarmOperator2Select_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(6) > div > div > "
                             "div" % (formulaListA * 2 - 1, formulaListB))  # 上限值-运算符选择栏
        self.click(*alarmOperator2Select_loc)
        self.select_in_LastDiv(value)

    # 输入上限值-系数
    def input_alarmRuleBackRatio(self, value, formulaListB,  # 当前因子中第几个公式
                                 formulaListA  # 第几个因子
                                 ):
        alarmRuleBackRatioInput_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(7) > "
                             "input" % (formulaListA * 2 - 1, formulaListB))  # 上限值-系数-输入栏
        self.send_keys(value, *alarmRuleBackRatioInput_loc)

    # 选择连接关系
    def input_alarmRuleLogicalOperator1(self, value, formulaListB,  # 当前因子中第几个公式
                                       formulaListA  # 第几个因子
                                       ):
        alarmRuleLogicalOperator1Select_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(8) > div > div > "
                             "div" % (formulaListA * 2 - 1, formulaListB))  # 连接关系
        self.click(*alarmRuleLogicalOperator1Select_loc)
        self.select_in_LastDiv(value)

    # 点击操作中的增加公式按钮
    def click_addFormulaBButton(self, formulaListB,  # 当前因子中第几个公式
                               formulaListA  # 第几个因子
                               ):
        addFormulaBButton_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > div.ant-table-wrapper > div > div > "
                             "div > div > div > table > tbody > tr:nth-child(%s) > td:nth-child(9) > span > "
                             "div[class^='btnStyle'] > button" % (formulaListA * 2 - 1, formulaListB))  # 操作-增加按钮
        self.click(*addFormulaBButton_loc)

    # 选择因子关系
    def input_alarmRuleLogicalOperator2(self, value,
                                        formulaListA  # 第几个因子与下一个因子之间的关系
                                        ):
        alarmRuleLogicalOperator2Select_loc = (
            By.CSS_SELECTOR, "div[class^='tableWrapper'] > div:nth-child(%s) > span > div > div > "
                             "div" % (formulaListA * 2))  # 因子关系
        self.click(*alarmRuleLogicalOperator2Select_loc)
        self.select_in_LastDiv(value)

    # 点击新增因子按钮
    def click_addFormulaAButton(self):
        self.click(*self.addFormulaAButton_loc)

    # 点击高级设置按钮
    def click_advancedSettingButton(self):
        self.click(*self.advancedSettingButton_loc)

    # 输入持续时间
    def input_alarmRuleEvaluateValue(self, alarmRuleEvaluateValue):
        self.send_keys(alarmRuleEvaluateValue, *self.alarmRuleEvaluateValueInput_loc)

    # 输入提醒间隔
    def input_alarmRuleReminderInterval(self, alarmRuleReminderInterval):
        self.send_keys(alarmRuleReminderInterval, *self.alarmRuleReminderIntervalInput_loc)

    # 点击保存按钮
    def click_submitCreateAlarmRuleButton(self):
        self.click(*self.submitCreateAlarmRuleButton_loc)
