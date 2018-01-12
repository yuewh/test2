# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from time import sleep

'''
异常规则设置基本方法
'''


class alarmRuleManager_page(BasePage):
    """定位器"""
    alarmRuleManagementButton_loc = (
        By.CSS_SELECTOR, "body > div.body.ng-scope > div > div.ng-scope > div > div > div.left-bj.top-bottom > div > "
                         "div > div > div.tt2 > ul > li:nth-child(7)")    # 后台管理中的异常规则管理按钮
    alarmRuleManagerButton_loc = (By.CSS_SELECTOR, "li[title='异常规则设置'] > a")   # 左侧异常规则设置TAB按钮
    # 主页面
    # 查询区域
    powerclientNameInput_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='btnGroup'] > "
                         "div:nth-child(2) > div > div")  # 站点名称选择栏
    ruleTypeInput_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='btnGroup'] > "
                         "div:nth-child(4) > div > div")  # 规则类型选择栏
    alarmTypeInput_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='btnGroup'] > "
                         "div:nth-child(6) > div > div")  # 异常类型选择栏
    alarmRuleSearchButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='btnGroup'] > "
                         "div[class^='btnStyle'] > button")  # 查询按钮
    # 按钮区域
    settingRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='toolkit'] > "
                         "a:nth-child(1) > div > button")  # 异常设置按钮
    settingPushRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='toolkit'] > "
                         "a:nth-child(2) > div > button")  # 推送设置按钮
    deleteRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='normal'] > div[class^='toolkit'] > "
                         "div > button")  # 批量删除按钮
    # 列表区域
    selectAllRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='table'] > div > div > div > div > "
                         "div > div > div > div.ant-table-header > table > thead > tr > th.ant-table-selection-column "
                         "> span > div > label > span")  # 站点全选按钮
    selectOneRuleButtonList_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='table'] > div > div > div > div > "
                         "div > div > div > div.ant-table-body > table > tbody > tr > td.ant-table-selection-column > "
                         "span > label > span")  # 单个站点的选择框所在列elements
    powerclientNameOfRuleList_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='table'] > div > div > div > div > "
                         "div > div > div > div.ant-table-body > table > tbody > tr > td:nth-child(4)")  # 单个站点的站点名称所在列elements

    # 异常设置页面
    powerclientNameSelect_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='stationGroup'] > "
                         "div[class^='wrapper'] > div > div")  # 选择站点选择框
    powerclientNameSelectInput_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='stationGroup'] > "
                         "div[class^='wrapper'] > div > div > div > div.ant-select-search.ant-select-search--inline > "
                         "div > input")  # 选择站点选择框的输入栏
    selectAllMoniterObjectButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > "
                         "div > div > div > div[class^='wrapInner'] > div > div[class^='tableGroup'] > "
                         "div[class^='tableContainer'] > div[class^='header'] > span[class^='treeHeader'] > "
                         "span:nth-child(2) > div > label > span.ant-checkbox")  # 设备层级树全选按钮
    bindAllRuleToMoniterObjectButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='tableGroup'] > "
                         "div[class^='ruleList'] > div[class^='content'] > div:nth-child(1)")  # 选择规则中的全部按钮
    submitBindRuleButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='footGroup'] > div[class^='btnStyle'] "
                         "> button")  # 保存按钮
    bindInfo_loc = (By.CSS_SELECTOR, "body > div:last-child > div > span > div > div > div > span")  # 保存提示
    goBackButton_loc = (
        By.CSS_SELECTOR, "#root > div > div > div > div[class^='section'] > div[class^='content'] > div > div > div > "
                         "div > div > div[class^='wrapInner'] > div > div[class^='returnGroup'] > a > div > button")  # 返回按钮

    # action

    # 点击后台管理中的异常规则管理按钮
    def click_alarmRuleManagementButton(self):
        self.click(*self.alarmRuleManagementButton_loc)
        self.switch_to_window()

    # 点击左侧异常规则设置TAB按钮
    def click_alarmRuleManagerButton(self):
        self.click(*self.alarmRuleManagerButton_loc)

    # 点击异常设置按钮
    def click_settingRuleButton(self):
        self.click(*self.settingRuleButton_loc)

    # 点击推送设置按钮
    def click_settingPushRuleButton(self):
        self.click(*self.settingPushRuleButton_loc)

    # 在异常设置和推送设置页面， 选择站点
    def input_stationName(self, powerclientName):
        self.click(*self.powerclientNameSelect_loc)
        self.find_element(*self.powerclientNameSelectInput_loc).send_keys(str(powerclientName))
        sleep(1)
        self.select_in_LastDiv(powerclientName)

    # 在异常设置和推送设置页面，点击选择站点中的全选按钮
    def click_selectAllMoniterObjectButton(self):
        self.click(*self.selectAllMoniterObjectButton_loc)

    # 在异常设置和推送设置页面，点击选择规则中的全部按钮
    def click_bindAllRuleToMoniterObjectButton(self):
        self.click(*self.bindAllRuleToMoniterObjectButton_loc)

    # 在异常设置和推送设置页面，点击保存按钮
    def click_submitBindRuleButton(self):
        self.click(*self.submitBindRuleButton_loc)

    # 在异常设置和推送设置页面，获取页面信息
    def get_bindInfo(self):
        return self.find_element(*self.bindInfo_loc).text

    # 在异常设置和推送设置页面，点击返回按钮
    def click_goBackButton(self):
        self.click(*self.goBackButton_loc)
