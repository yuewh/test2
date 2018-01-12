# coding:utf-8
__author__ = 'luws'
from src.pages.alarmRuleBank_page import alarmRuleBank_page
import time
'''
异常规则管理-异常规则设置-组合方法
'''


class alarmRuleBank(alarmRuleBank_page):
    def createAlarmRule(self, formulaListB,   # 每个因子有几个公式
                        formulaListA,  # 有几个因子
                        alarmRuleName,  # 规则名称
                        alarmRuleAssignedType='遥测',  # 数据类型
                        alarmRuleCategory='断相',  # 规则类型
                        alarmRuleType='告警',  # 异常类型
                        alarmRuleFrontMetricCode=1.23,  # 下限值-参数（输入int型为输入值，str为选择值）
                        alarmOperator1='*',  # 下限值-选择符
                        alarmRuleFrontRatioInput=0.5,  # 下限值-系数
                        alarmRuleMetricCode='A相电压(V)',  # 数据项
                        alarmRuleBackMetricCode=200,  # 上限值-参数（输入int型为输入值，str为选择值）
                        alarmOperator2='+',  # 上限值-运算符
                        alarmRuleBackRatio=2.5,  # 上限值-系数
                        alarmRuleLogicalOperator1='或',  # 单因子中的公式的连接关系
                        alarmRuleLogicalOperator2='或',  # 因子关系
                        alarmRuleEvaluateValue='0',  # 持续时间
                        alarmRuleReminderInterval='0'  # 间隔时间
                        ):
        # action
        self.click_createAlarmRuleButton()
        self.input_alarmRuleAssignedType(alarmRuleAssignedType)
        self.input_alarmRuleCategory(alarmRuleCategory)
        self.input_alarmRuleName(alarmRuleName)
        self.input_alarmRuleType(alarmRuleType)
        for i in range(1, formulaListA+1):
            for j in range(1, formulaListB+1):
                self.input_alarmRuleFrontMetricCode(alarmRuleFrontMetricCode, j, i)
                self.input_alarmOperator1(alarmOperator1, j, i)
                self.input_alarmRuleFrontRatio(alarmRuleFrontRatioInput, j, i)
                self.input_alarmRuleMetricCode(alarmRuleMetricCode, j, i)
                self.input_alarmRuleBackMetricCode(alarmRuleBackMetricCode, j, i)
                self.input_alarmOperator2(alarmOperator2, j, i)
                self.input_alarmRuleBackRatio(alarmRuleBackRatio, j, i)
                if j != formulaListB:
                    self.click_addFormulaBButton(j, i)
                    self.input_alarmRuleLogicalOperator1(alarmRuleLogicalOperator1, j, i)
                    print(str(i) + "" + str(j) + "添加成功"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            if formulaListA > 1 and i == 1:
                self.click_advancedSettingButton()
            if formulaListA > 1 and i != formulaListA:
                self.click_addFormulaAButton()
                self.input_alarmRuleLogicalOperator2(alarmRuleLogicalOperator2, i)
        self.input_alarmRuleEvaluateValue(alarmRuleEvaluateValue)
        self.input_alarmRuleReminderInterval(alarmRuleReminderInterval)
        # self.click_submitCreateAlarmRuleButton()
