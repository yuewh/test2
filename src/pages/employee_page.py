# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
客户管理-员工管理页面（服务商和企业）基本方法
'''


class employee_page(BasePage):
    """定位器"""
    """人员管理页面"""
    employeeButton_loc = (                                                              # 人员管理Tab页按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.row.search-pan > div > div:nth-child(2)')
    createEmployeeButton_loc = (By.CSS_SELECTOR, 'button.btn-sty.mg-bottom10p')          # 添加按钮
    employeeNameList_loc = (                                                            # 姓名所在列
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > div:nth-child(1) > div > table > tbody > tr > '
                         'td:nth-child(1)')
    submitDeleteEmployeeButton_loc = (                                                  # 删除员工二次确认弹窗中的确认按钮
        By.CSS_SELECTOR, 'div.modal-footer.text-center > button:nth-child(2)')
    cancelDeleteEmployeeButton_loc = (                                                  # 删除员工二次确认弹窗中的取消按钮
        By.CSS_SELECTOR, 'div.modal-footer.text-center > button:nth-child(1)')
    updateEmployeeButton_inDetail_loc = (                                               # 员工详情中的编辑按钮
        By.CSS_SELECTOR, 'button.btn-sty.mg-rt15p.mg-top10p.fl-right')
    createAccountButton_loc = (                                                          # 创建平台账号按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > div.detailDiv.mg-top15p > div:nth-child(4) > '
                         'div:nth-child(4) > button')

    """添加员工页面"""
    employeeNameInput_loc = (By.CSS_SELECTOR, "input[name='name']")                     # 姓名
    employeeSex_male_loc = (                                                            # 性别男的单选框
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div > div > '
                         'div:nth-child(1) > label > span.toggle-radio')
    employeeSex_female_loc = (                                                          # 性别女的单选框
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div > div > '
                         'div:nth-child(3) > label > span.toggle-radio')
    employeeBirthday_loc = (By.ID, 'birthday')                                          # 出生日期
    employeePosition_loc = (By.CSS_SELECTOR, "input[name='position']")                  # 岗位
    employeePositionSelectList_loc = (                                                  # 岗位选项
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(5) > div > ul > li')
    employeeContactType_loc = (By.CSS_SELECTOR, "select[name='contactType']")           # 联系人类型
    employeeCellphone_loc = (By.CSS_SELECTOR, "input[name='cellphone']")                # 手机号码
    employeeTelphone_loc = (By.CSS_SELECTOR, "input[name='telphone']")                  # 固定电话
    employeeEmail_loc = (By.CSS_SELECTOR, "input[name='email']")                        # 电子邮箱
    employeeWeChat_loc = (By.CSS_SELECTOR, "input[name='weChat']")                      # 微信号
    employeePostcode_loc = (By.CSS_SELECTOR, "input[name='postcode']")                  # 邮编
    employeeAddress_loc = (By.CSS_SELECTOR, "input[name='address']")                    # 地址
    employeeRemark_loc = (By.CSS_SELECTOR, "textarea[name='remark']")                   # 备注
    submitCreateEmployeeButton_loc = (                                                   # 添加员工的确定按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div.form-group.mg-bottom5p.col-sm-7.col-md-6.'
                         'col-lg-5.col-sm-push-5.col-md-push-4.col-lg-push-4.mg-top25p > button.btn.btn-primary.'
                         'no-radius.input-size80')
    cancelCreateEmployeeButton_loc = (                                                   # 添加员工的取消按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div.form-group.mg-bottom5p.col-sm-7.col-md-6.'
                         'col-lg-5.col-sm-push-5.col-md-push-4.col-lg-push-4.mg-top25p > button.btn.btn-default.'
                         'no-radius.input-size80.mg-lf20p')
    employeeInfo_loc = (                                                                # 提交后的弹窗中的提示文字
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body > '
                         'div.text-center.modal-msg > span')
    closeEmployeeInfo_loc = (                                                           # 提交后的弹窗中的立即关闭按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button')
    accountInfo_loc = (                                                                 # 注册账号提交后的弹窗中的提示文字
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div.modal-body > '
                         'div.text-center.modal-msg > span')
    closeAccountInfo_loc = (                                                            # 注册账号提交后的弹窗中的立即关闭按钮
        By.CSS_SELECTOR, 'body > div:last-child > div > div > div > div.modal-footer.text-center > '
                         'button')

    """创建平台账号页面"""
    accountUsername_loc = (By.CSS_SELECTOR, "input[name='username']")                   # 账号名称
    accountPassword_loc = (By.ID, 'password1')                                          # 密码
    accountConfirmPassword_loc = (By.ID, 'tpassword1')                                  # 确认密码
    submitCreateAccountButton_loc = (                                                    # 确认按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button.btn.btn-primary.no-radius.input-size80')
    cancelCreateAccountButton_loc = (                                                    # 取消按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button.btn.btn-default.no-radius.input-size80.mg-lf20p')

    # 点击人员管理Tab页
    def click_employeeButton(self):
        self.click(*self.employeeButton_loc)

    # 点击添加按钮
    def click_createEmployeeButton(self):
        self.click(*self.createEmployeeButton_loc)

    # 根据姓名，点击列表中的编辑按钮（重名时点击第一个）
    def click_updateEmployeeButton_inList(self, employeeName):
        n = self.get_elementNum(employeeName, *self.employeeNameList_loc)
        self.click(
            By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > '
                             'div > div > div > div.ng-scope > div > div > div:nth-child(1) > div > table > tbody > '
                             'tr:nth-child(%s) > td.t1 > div > a:nth-child(1)' % n)

    # 根据姓名，点击列表中的删除按钮（重名时点击第一个）
    def click_deleteEmployeeButton(self, employeeName):
        n = self.get_elementNum(employeeName, *self.employeeNameList_loc)
        self.click(
            By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > '
                             'div > div > div > div.ng-scope > div > div > div:nth-child(1) > div > table > tbody > '
                             'tr:nth-child(%s) > td.t1 > div > a:nth-child(2)' % n)

    # 点击删除确认弹窗中的确定按钮
    def click_submitDeleteEmployeeButton(self):
        self.click(*self.submitDeleteEmployeeButton_loc)

    # 点击删除确认弹窗中的取消按钮
    def click_cancelDeleteEmployeeButton(self):
        self.click(*self.cancelDeleteEmployeeButton_loc)

    # 点击详情中的编辑按钮
    def click_updateEmployeeButton_inDetail(self):
        self.click(*self.updateEmployeeButton_inDetail_loc)

    # 根据姓名，点击某一行数据，展开详情(此处点击的是姓名栏，重名时点击第一个)
    def click_employeeName(self, employeeName):
        n = self.get_elementNum(employeeName, *self.employeeNameList_loc)
        self.click(
            By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > '
                             'div > div > div > div.ng-scope > div > div > div:nth-child(1) > div > table > tbody > '
                             'tr:nth-child(%s) > td:nth-child(1)' % n)

    # 在员工详情中，点击创建平台账号按钮(前置条件：已经点到要创建账号的那个人的详情)
    def click_createAccountButton(self):
        self.click(*self.createAccountButton_loc)

    # 在创建平台账号弹窗中，输入账号名称
    def input_accountUsername(self, accountUsername):
        self.find_element(*self.accountUsername_loc).send_keys(accountUsername)

    # 在创建平台账号弹窗中，输入密码
    def input_accountPassword(self, accountPassword):
        self.find_element(*self.accountPassword_loc).send_keys(accountPassword)

    # 在创建平台账号弹窗中，输入确认密码
    def input_accountConfirmPassword(self, accountConfirmPassword):
        self.find_element(*self.accountConfirmPassword_loc).send_keys(accountConfirmPassword)

    # 在创建平台账号弹窗中，点击确认按钮
    def click_submitCreateAccountButton(self):
        self.click(*self.submitCreateAccountButton_loc)

    # 在创建平台账号弹窗中，点击取消按钮
    def click_cancelCreateAccountButton(self):
        self.click(*self.cancelCreateAccountButton_loc)

    # 在添加员工页面，输入姓名
    def input_employeeName(self, employeeName):
        self.find_element(*self.employeeNameInput_loc).send_keys(str(employeeName))

    # 在添加员工页面，选择性别
    def input_employeeSex(self, employeeSex):
        try:
            assert str(employeeSex) == '男' or str(employeeSex) == '女', '参数错误：employeeSex应输入男或女'
        except AssertionError:
            self.mylog.error('参数错误：employeeSex应输入男或女')
        if str(employeeSex) == '男':
            self.click(*self.employeeSex_male_loc)
        else:
            self.click(*self.employeeSex_female_loc)

    # 在添加员工页面，选择出生日期
    def input_employeeBirthday(self, employeeBirthday):         # 员工出生日期，格式：YYYY-MM-DD
        self.check_dataFormat(employeeBirthday)
        self.find_element(*self.employeeBirthday_loc)
        js = "$('#birthday').attr('readonly',false)"
        self.driver.execute_script(js)
        self.find_element(*self.employeeBirthday_loc).send_keys(employeeBirthday)
        self.click(*self.employeeNameInput_loc)  # 收起日期控件

    # 在添加员工页面，选择岗位
    def input_employeePosition(self, employeePosition):
        self.click(*self.employeePosition_loc)
        self.click_valueFromList(employeePosition, self.employeePositionSelectList_loc)

    # 在添加员工页面，选择联系人类型
    def input_employeeContactType(self, employeeContactType):
        self.select_by_option(employeeContactType, *self.employeeContactType_loc)

    # 在添加员工页面，输入手机号码
    def input_employeeCellphone(self, employeeCellphone):
        self.find_element(*self.employeeCellphone_loc).send_keys(employeeCellphone)

    # 在添加员工页面，输入固定电话
    def input_employeeTelphone(self, employeeTelphone):
        self.find_element(*self.employeeTelphone_loc).send_keys(employeeTelphone)

    # 在添加员工页面，输入电子邮箱
    def input_employeeEmail(self, employeeEmail):
        self.find_element(*self.employeeEmail_loc).send_keys(employeeEmail)

    # 在添加员工页面，输入微信号
    def input_employeeWeChat(self, employeeWeChat):
        self.find_element(*self.employeeWeChat_loc).send_keys(employeeWeChat)

    # 在添加员工页面，输入邮编
    def input_employeePostcode(self, employeePostcode):
        self.find_element(*self.employeePostcode_loc).send_keys(employeePostcode)

    # 在添加员工页面，输入地址
    def input_employeeAddress(self, employeeAddress):
        self.find_element(*self.employeeAddress_loc).send_keys(employeeAddress)

    # 在添加员工页面，输入备注
    def input_employeeRemark(self, employeeRemark):
        self.find_element(*self.employeeRemark_loc).send_keys(employeeRemark)

    # 在添加员工页面，点击确定按钮
    def click_submitCreateEmployeeButton(self):
        self.click(*self.submitCreateEmployeeButton_loc)

    # 在添加员工页面，点击取消按钮
    def click_cancelCreateEmployeeButton(self):
        self.click(*self.cancelCreateEmployeeButton_loc)

    # 获取弹窗提示
    def get_employeeInfo(self):
        info_loc = self.find_element(*self.employeeInfo_loc)
        return info_loc.text

    # 点击弹窗提示中的立即关闭按钮
    def click_closeEmployeeInfo(self):
        self.click(*self.closeEmployeeInfo_loc)

    # 获取注册账号弹窗提示中的文字
    def get_accountInfo(self):
        info_loc = self.find_element(*self.accountInfo_loc)
        return info_loc.text

    # 点击注册账号提交后弹窗中的立即关闭按钮
    def click_closeAccountInfo(self):
        self.click(*self.closeAccountInfo_loc)
