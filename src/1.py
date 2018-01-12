from src.group.alarmRuleBank import alarmRuleBank
from src.group.alarmRuleManager import alarmRuleManager
from src.group.login import login
from selenium import webdriver
from time import sleep


formulaListA = 5  # 有几个因子
formulaListB = 25  # 每个因子有几个公式

driver = webdriver.Chrome()     # 浏览器驱动
login(driver, base_url='http://10.1.170.76:16012').login(username='yny1')
alarmRuleManager(driver).click_alarmRuleManagementButton()
alarmRuleBank(driver).click_alarmRuleBankButton()
alarmRuleBank(driver).createAlarmRule(formulaListB=formulaListB, formulaListA=formulaListA, alarmRuleName='test1', alarmRuleCategory='电压谐波含有率越限', alarmRuleMetricCode='B相电压2次谐波含有率(%)')

# sleep(5)
# driver.quit()

