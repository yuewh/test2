# coding:utf-8
__author__ = 'luws'
from src.pages.employee_page import employee_page

'''
客户信息管理-人员管理组合方法
'''


class employee(employee_page):
    # 创建平台账号
    def createAccount(self, accountUsername,  # 账号名称
                      accountPassword='123456',  # 密码
                      accountConfirmPassword='123456',  # 确认密码
                      ):
        self.click_createAccountButton()
        self.input_accountUsername(accountUsername)
        self.input_accountPassword(accountPassword)
        self.input_accountConfirmPassword(accountConfirmPassword)
        self.click_submitCreateAccountButton()
        msg = self.get_accountInfo()
        self.click_closeAccountInfo()
        return msg

    # 创建一个人员，只输入必填字段
    def createEmployee_inputRequired(self, employeeName,                    # 姓名
                                     employeeCellphone,                     # 手机号码
                                     employeePosition='系统管理岗',          # 岗位
                                     employeeContactType='用电联系人',       # 联系人类型
                                     ):
        self.click_createEmployeeButton()
        self.input_employeeName(employeeName)
        self.input_employeePosition(employeePosition)
        self.input_employeeContactType(employeeContactType)
        self.input_employeeCellphone(employeeCellphone)
        self.click_submitCreateEmployeeButton()
        msg = self.get_employeeInfo()
        self.click_closeEmployeeInfo()
        return msg

    # 创建一个人员，输入所有字段（不修改地址）
    def createEmployee_inputAll(self, employeeName,                    # 姓名
                                employeeCellphone,                     # 手机号码
                                employeeSex='男',                      # 性别
                                employeeBirthday='2000-10-10',         # 出生日期
                                employeePosition='系统管理岗',          # 岗位
                                employeeContactType='用电联系人',       # 联系人类型
                                employeeTelphone='',                   # 固定电话
                                employeeEmail='',                      # 电子邮箱
                                employeeWeChat='',                     # 微信号
                                employeePostcode='',                   # 邮编
                                employeeRemark='',                     # 备注
                                ):
        self.click_createEmployeeButton()
        self.input_employeeName(employeeName)
        self.input_employeeSex(employeeSex)
        self.input_employeeBirthday(employeeBirthday)
        self.input_employeePosition(employeePosition)
        self.input_employeeContactType(employeeContactType)
        self.input_employeeCellphone(employeeCellphone)
        self.input_employeeTelphone(employeeTelphone)
        self.input_employeeEmail(employeeEmail)
        self.input_employeeWeChat(employeeWeChat)
        self.input_employeePostcode(employeePostcode)
        self.input_employeeRemark(employeeRemark)
        self.click_submitCreateEmployeeButton()
        msg = self.get_employeeInfo()
        self.click_closeEmployeeInfo()
        return msg

    # 删除一个员工
    def deleteEmployee(self, employeeName):
        self.click_deleteEmployeeButton(employeeName)
        self.click_submitDeleteEmployeeButton()
        msg = self.get_employeeInfo()
        self.click_closeEmployeeInfo()
        return msg

    # 创建一个人员并创建平台账号
    def createEmployeeAndAccount(self, employeeName,  # 姓名
                                 employeeCellphone,  # 手机号码
                                 accountUsername,  # 账号名称
                                 employeePosition='系统管理岗',  # 岗位
                                 employeeContactType='用电联系人',  # 联系人类型
                                 accountPassword='123456',  # 密码
                                 accountConfirmPassword='123456',  # 确认密码
                                 ):
        self.createEmployee_inputRequired(employeeName=employeeName, employeeCellphone=employeeCellphone,
                                          employeePosition=employeePosition, employeeContactType=employeeContactType)
        self.click_employeeName(employeeName)
        self.createAccount(accountUsername=accountUsername, accountPassword=accountPassword,
                           accountConfirmPassword=accountConfirmPassword)
