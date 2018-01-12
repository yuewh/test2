# coding:utf-8
__author__ = '***'
import unittest, time, HTMLTestRunner
from config.globalparameter import test_case_path, report_name
# from src.common import send_email
'''
构建测试套件，并执行测试
'''


# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test_*.py')

# 执行测试
# if __name__ == "__main__":
report = report_name+"Report.html"
fb = open(report, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fb,
    title='自动化测试报告',
    description='*********'
)
runner.run(suite)
fb.close()
print('测试报告路径:' + report)

# 发送邮件
# time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕
# email = send_email.send_email()
# email.sendReport()