# coding:utf-8
__author__ = 'luws'
from src.pages.alarmRuleManager_page import alarmRuleManager_page
from time import sleep
'''
异常规则管理-异常规则设置-组合方法
'''


class alarmRuleManager(alarmRuleManager_page):
    # 将所有告警规则绑定到所有设备层级上
    def bindAllAlarmRuleToAllMoniterObject(self, powerclientName):
        self.input_stationName(powerclientName)
        sleep(1)    # 等待页面元素加载，否则无法被全选中
        self.click_selectAllMoniterObjectButton()
        self.click_bindAllRuleToMoniterObjectButton()
        # sleep(1)
        self.click_submitBindRuleButton()
        return self.get_bindInfo()
