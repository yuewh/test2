# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from time import sleep

'''
客户信息管理页面基本方法
'''


class customer_page(BasePage):

    """定位器"""
    """客户信息管理页面"""
    createCustomerButton_loc = (By.CSS_SELECTOR, 'button.btn-sty.fl-left')                   # 添加按钮
    searchInput_loc = (By.CSS_SELECTOR, "input[data-ng-model='keyword']")                   # 搜索输入栏
    searchButton_loc = (By.CSS_SELECTOR, "button[type='submit']")                           # 搜索按钮
    customerNameList_loc = (By.CSS_SELECTOR, 'span.link.ng-binding')                        # 客户名称列
    submitDeleteCustomerButton_loc = (By.CSS_SELECTOR, "button[data-ng-click='ok()']")      # 删除客户的二次确认中的确认按钮
    cancelDeleteCustomerButton_loc = (By.CSS_SELECTOR, "button[data-ng-click='exit()']")    # 删除客户的二次确认中的取消按钮
    customerPageSizeButton_20_loc = (                                                       # 每页显示20条的按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div.dataZn.mg-rt15p > div.list-bottom > div > div > ol > li:nth-child(3) > a')
    customerTotalSize_loc = (                                                               # 共有几条的数字所在位置
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div.dataZn.mg-rt15p > div.list-bottom > div > div > span > span')
    customerGoDownButton_loc = (                                                            # 下一页按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div.dataZn.mg-rt15p > div.list-bottom > div > div > ul > li:nth-child(6) > a')
    customerButton_loc = (                                                                  # 基本信息按钮，与人员管理、用电客户信息并列
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.row.search-pan > div > div:nth-child(1)')
    customerManagementButton_loc = (By.CSS_SELECTOR, '.tt2 > ul > li:nth-child(1)')         # 客户信息管理按钮
    """详情页面"""
    updateCustomerButton_loc = (                                                            # 详情页面的编辑按钮
        By.CSS_SELECTOR, 'div.col-sm-7.col-md-6.col-lg-5.mg-top30p > button:nth-child(3)')
    goBackButton_inCustomerDetail_loc = (                                                   # 详情页面的返回按钮
        By.CSS_SELECTOR, 'div.col-sm-7.col-md-6.col-lg-5.mg-top30p > button:nth-child(3)')

    """添加页面"""
    customerName_loc = (By.ID, 'name')                                                      # 客户名称
    customerShortName_lod = (By.ID, 'shortName')                                            # 企业简称
    customerType_loc = (By.CSS_SELECTOR, "select[name='type']")                             # 企业性质
    customeCompanyScale_loc = (By.CSS_SELECTOR, "select[name='companyScale']")              # 企业规模
    customerIntroduction_loc = (By.CSS_SELECTOR, "textarea[name='introduction']")           # 企业简介
    customerRegisteredCapital_loc = (By.CSS_SELECTOR, "input[name='registeredCapital']")    # 注册资本金
    customerArtificialPerson_loc = (By.CSS_SELECTOR, "input[name='artificialPerson']")      # 法人代表
    customerMainBusinesses_loc = (By.CSS_SELECTOR, "textarea[name='mainBusinesses']")       # 主营业务
    customerBusinessScopes_loc = (By.CSS_SELECTOR, "textarea[name='businessScopes']")       # 经营范围
    customerMainProducts_loc = (By.CSS_SELECTOR, "textarea[name='mainProducts']")           # 主要产品
    customerWebsite_loc = (By.CSS_SELECTOR, "input[name='website']")                        # 企业网址
    customerGoWebsite_loc = (                                                               # 前往企业网址
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(1) > div:nth-child(12) > '
                         'div.col-lg-2.col-md-2 > a')
    customerEmail_loc = (By.CSS_SELECTOR, "input[name='email']")                            # 电子邮箱
    customerTelphone_loc = (By.CSS_SELECTOR, "input[name='telphone']")                      # 企业总机
    customerFax_loc = (By.CSS_SELECTOR, "input[name='fax']")                                # 传真号码
    customerParentButton_loc = (                                                            # 选择上级客户按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(1) > div:nth-child(16) > '
                         'div.col-sm-7.col-md-6.col-lg-5.ng-isolate-scope.ellipsis > div')
    customerParentNameList_loc = (                                                          # 上级客户弹窗中的客户名称列
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.row > div > '
                         'div:nth-child(2) > div > div.fl-left.mg-top7p.ng-isolate-scope.ellipsis > label')
    submitParentCustomerButton_loc = (                                                      # 上级客户弹窗中的确认按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button')
    cancelParentCustomerButton_loc = (                                                      # 上级客户弹窗中的确认按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button:nth-child(2)')
    searchCustomerParentKey_loc = (                                                         # 上级客户弹窗中的搜索输入栏
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.row > form > '
                         'input')
    searchCustomerParentButton_loc = (                                                      # 上级客户弹窗中的搜索按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.row > form > '
                         'button')
    clearParentCustomerButton_loc = (                                                       # 选择上级客户按钮旁边的清空按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(1) > div:nth-child(16) > '
                         'div.col-lg-2.col-md-2 > a')
    customerProvince_loc = (By.CSS_SELECTOR, "select[data-ng-model='model.provinceCode']")  # 省
    customerCity_loc = (By.CSS_SELECTOR, "select[data-ng-model='model.cityCode']")          # 市
    customerCounty_loc = (By.CSS_SELECTOR, "select[data-ng-model='model.countyCode']")      # 区
    customerStreet_loc = (By.CSS_SELECTOR, "input[name='streetCode']")                      # 街道
    customerAddress_loc = (By.CSS_SELECTOR, "input[name='address']")                        # 详细地址
    customerPostcode_loc = (By.CSS_SELECTOR, "input[name='postcode']")                      # 邮编
    customerIdentityTypeNameList_loc = (                                                    # 客户类型名字所在列
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div:nth-child(2) > div > '
                         'div > label')
    customerDistributor_loc = (By.CSS_SELECTOR, "select[name='distributor']")               # 渠道类型
    customerDistributorName_loc = (By.CSS_SELECTOR, "input[name='distributorName']")        # 渠道名称
    customerServiceProviderButton_loc = (                                                   # 选择服务商按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div.form-group > '
                         'div.col-sm-7.col-md-6.col-lg-5.ng-isolate-scope.ellipsis > div')
    clearServiceProviderButton_loc = (                                                      # 选择服务商按钮旁边的清空按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div.form-group > '
                         'div.col-lg-2.col-md-2 > a')
    customerSaleRepresentative_loc = (By.CSS_SELECTOR, "input[name='saleRepresentative']")  # 销售代表
    customerMonitoringType_loc = (                                                          # 接入监测类型文字所在列
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div.form-group > '
                         'div.col-sm-7.col-md-6.col-lg-5.mg-top6p > div.col-sm-3.col-md-3.col-lg-2.ng-scope > label')
    customerIfSign_loc = (                                                                  # 是否签约的文字所在列
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div:nth-child(3) > div.form-group > '
                         'div.col-sm-7.col-md-6.col-lg-5.control-div > div > div.fl-left.mg-lf4p > label')
    submitCreateCustomerButton_loc = (                                                       # 保存按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div.form-group > div > button:nth-child(1)')
    cancelCreateCustomerButton_loc = (                                                       # 取消按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.ng-scope > div > div > form > div.form-group > div > button:nth-child(2)')
    customerInfo_loc = (                                                                    # 提交后的页面弹窗提示文字
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body > '
                         'div.text-center.modal-msg > span')
    closeCustomerInfo_loc = (                                                               # 提交后的页面弹窗的立即关闭按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button')

    # 点击客户信息管理按钮
    def click_customerManagementButton(self):
        self.click(*self.customerManagementButton_loc)

    # 点击添加按钮
    def click_createCudtomerButton(self):
        self.click(*self.createCustomerButton_loc)

    # 搜索关键字
    def search_customer(self, value):
        self.find_element(*self.searchInput_loc).send_keys(str(value))
        self.click(*self.searchButton_loc)
        sleep(1)

    # 获取总条数
    def get_customerTotalSize(self):
        n = self.find_element(*self.customerTotalSize_loc)
        return n.text

    # 点击每页显示20条
    def click_customerPageSizeButton_20(self):
        self.click(*self.customerPageSizeButton_20_loc)
        sleep(0.5)  # 避免页面刷新元素位置过期

    # 点击下一页按钮
    def click_customerGoDownButton(self):
        self.click(*self.customerGoDownButton_loc)

    # 获取当前页面上的客户名称列表
    def get_CustomerNameList(self):
        return self.get_infoList(*self.customerNameList_loc)

    # 根据客户名称，点击详情按钮
    def click_customerDetailButton(self, customerName):
        n = self.get_elementNum(customerName, *self.customerNameList_loc)
        self.click(
            By.CSS_SELECTOR, "body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > "
                             "div > div > div.dataZn.mg-rt15p > div.info-zone > div:nth-child(2) > div:nth-child(%s) > "
                             "div.wid-20.flex-div.text-center.mg-top30p > div.mg-lf10p > button" % n)

    # 点击基本信息，可从人员管理、用电客户信息处跳转回来
    def click_customerButton(self):
        self.click(*self.customerButton_loc)

    # 根据客户名称，点击编辑按钮
    def click_updateCustomerButton(self, customerName):
        n = self.get_elementNum(customerName, *self.customerNameList_loc)
        self.click(
            By.CSS_SELECTOR, "body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > "
                             "div > div > div.dataZn.mg-rt15p > div.info-zone > div:nth-child(2) > div:nth-child(%s) > "
                             "div.wid-20.flex-div.text-center.mg-top30p > div.mg-lf15p > button" % n)

    # 根据客户名称，点击删除按钮
    def click_deleteCustomerButton(self, customerName):
        n = self.get_elementNum(customerName, *self.customerNameList_loc)
        self.click(
            By.CSS_SELECTOR, "body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > "
                             "div > div > div.dataZn.mg-rt15p > div.info-zone > div:nth-child(2) > div:nth-child(%s) > "
                             "div.wid-20.flex-div.text-center.mg-top30p > div:nth-child(3) > button" % n)

    # 点击删除按钮后二次确认的确认按钮
    def click_submitDeleteCustomerButton(self):
        self.click(*self.submitDeleteCustomerButton_loc)

    # 点击删除按钮后二次确认的取消按钮
    def click_cancelDeleteCustomerButton(self):
        self.click(*self.cancelDeleteCustomerButton_loc)

    # 在添加页面，输入客户名称
    def input_customerName(self, customerName):
        self.find_element(*self.customerName_loc).send_keys(str(customerName))

    # 在添加页面，输入企业简称
    def input_customerShortName(self, customerShortName):
        self.find_element(*self.customerShortName_lod).send_keys(str(customerShortName))

    # 在添加页面，选择企业性质
    def input_customerType(self, customerType):
        self.select_by_option(str(customerType), *self.customerType_loc)

    # 在添加页面，选择企业规模
    def input_customeCompanyScale(self, customeCompanyScale):
        self.select_by_option(str(customeCompanyScale), *self.customeCompanyScale_loc)

    # 在添加页面，输入企业简介
    def input_customerIntroduction(self, customerIntroduction):
        self.find_element(*self.customerIntroduction_loc).send_keys(str(customerIntroduction))

    # 在添加页面，输入注册资本金
    def input_customerRegisteredCapital(self, customerRegisteredCapital):
        self.find_element(*self.customerRegisteredCapital_loc).send_keys(str(customerRegisteredCapital))

    # 在添加页面，输入法人代表
    def input_customerArtificialPerson(self, customerArtificialPerson):
        self.find_element(*self.customerArtificialPerson_loc).send_keys(str(customerArtificialPerson))

    # 在添加页面，输入主营业务
    def input_customerMainBusinesses(self, customerMainBusinesses):
        self.find_element(*self.customerMainBusinesses_loc).send_keys(str(customerMainBusinesses))

    # 在添加页面，输入经营范围
    def input_customerBusinessScopes(self, customerBusinessScopes):
        self.find_element(*self.customerBusinessScopes_loc).send_keys(str(customerBusinessScopes))

    # 在添加页面，输入主要产品
    def input_customerMainProducts(self, customerMainProducts):
        self.find_element(*self.customerMainProducts_loc).send_keys(str(customerMainProducts))

    # 在添加页面，输入企业网址
    def input_customerWebsite(self, customerWebsite):
        self.find_element(*self.customerWebsite_loc).send_keys(str(customerWebsite))

    # 在添加页面，点击企业网址旁边的前往按钮
    def click_GoWebsite(self):
        self.click(*self.customerGoWebsite_loc)

    # 在添加页面，输入电子邮箱
    def input_customerEmail(self, customerEmail):
        self.find_element(*self.customerEmail_loc).send_keys(str(customerEmail))

    # 在添加页面，输入企业总机
    def input_customerTelphone(self, customerTelphone):
        self.find_element(*self.customerTelphone_loc).send_keys(str(customerTelphone))

    # 在添加页面，输入传真号码
    def input_customerFax(self, customerFax):
        self.find_element(*self.customerFax_loc).send_keys(str(customerFax))

    # 在添加页面，点击“选择上级客户”按钮
    def click_parentCustomerButton(self):
        self.click(*self.customerParentButton_loc)

    # 在添加页面，在选择上级客户弹窗中，点击要选择的上级客户
    # 选择上级客户的组合方法在group 中
    def click_parentCustomer(self, parentCustomer):
        n = self.get_elementNum(str(parentCustomer), *self.customerParentNameList_loc)
        self.click(
            By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.row > div > '
                             'div:nth-child(2) > div:nth-child(%s) > div.fl-left.mg-rt4p.mg-top10p > label > '
                             'span.toggle-radio' % n)

    # 在添加页面，在选择上级客户弹窗中，点击确定按钮
    def click_submitParentCustomer(self):
        self.click(*self.submitParentCustomerButton_loc)

    # 在添加页面，在选择上级客户弹窗中，点击取消按钮
    def click_cancelParentCustomer(self):
        self.click(*self.cancelParentCustomerButton_loc)

    # 在添加页面，在选择上级客户弹窗中，输入搜索关键字
    def input_searchParentCustomerKey(self, key):
        self.find_element(*self.searchCustomerParentKey_loc).send_keys(str(key), clear=False)

    # 在添加页面，在选择上级客户弹窗中，点击搜索按钮
    def click_searchParentCustomerButton(self):
        self.click(*self.searchCustomerParentButton_loc)

    # 在添加页面，点击选择上级客户按钮旁边的清空按钮
    def click_clearParentCustomerButton(self):
        self.click(self.clearParentCustomerButton_loc)

    # 在添加页面，选择省
    def input_customeProvince(self, customeProvince):
        self.select_by_option(str(customeProvince), *self.customerProvince_loc)

    # 在添加页面，选择市
    def input_customerCity(self, customerCity):
        self.select_by_option(str(customerCity), *self.customerCity_loc)

    # 在添加页面，选择区
    def input_customerCounty(self, customerCounty):
        self.select_by_option(str(customerCounty), *self.customerCounty_loc)

    # 在添加页面，输入所在街道
    def input_customerStreet(self, customerStreet):
        self.send_keys(customerStreet, *self.customerStreet_loc, clear=False)

    # 在添加页面，输入详细地址
    def input_customerAddress(self, customerAddress):
        self.send_keys(customerAddress, *self.customerAddress_loc)

    # 在添加页面，输入邮编
    def input_customerPostcode(self, customerPostcode):
        self.find_element(*self.customerPostcode_loc).send_keys(str(customerPostcode))

    # 在添加页面，选择一个或多个客户类型
    def input_customerIdentityType(self,
                                   customerIdentityTypeList         # 客户类型，str，逗号分隔，例如：'用能企业,安装运维商'
                                   ):
        datalist = str(customerIdentityTypeList).split(',')
        # 验证传入的客户类型list长度是否大于1，否则报错
        try:
            assert len(datalist) >= 1, '参数错误：customerIdentityTypeList长度不足'
        except AssertionError as e:
            self.mylog.error('参数错误：customerIdentityTypeList长度不足')
            raise e
        # 循环选择
        for n in datalist:
            m = self.get_elementNum(n, *self.customerIdentityTypeNameList_loc)
            self.click(
                By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom '
                                 '> div > div > div > div.ng-scope > div > div > form > div:nth-child(3) > '
                                 'div:nth-child(2) > div > div:nth-child(%s) > div > div' % m)

    # 在添加页面，选择渠道类型
    def input_customerDistributor(self, customerDistributor):
        self.select_by_option(str(customerDistributor), *self.customerDistributor_loc)

    # 在添加页面，输入渠道名称（渠道类型为推荐或代理的必填）
    def input_customerDistributorName(self, customerDistributorName):
        self.send_keys(customerDistributorName, *self.customerDistributorName_loc)

    # 在添加页面，点击选择服务商按钮,(在选择服务商弹窗中的操作与在上级客户弹窗中的一致，直接调用上级客户的方法即可)
    # 选择运维商的组合方法在group 中
    def click_customerServiceProviderButton(self):
        self.click(*self.customerServiceProviderButton_loc)

    # 在添加页面，点击选择服务商按钮旁边的清空按钮
    def click_clearServiceProviderButton(self):
        self.click(self.clearServiceProviderButton_loc)

    # 在添加页面，输入销售代表
    def input_customerSaleRepresentative(self, customerSaleRepresentative):
        self.send_keys(customerSaleRepresentative, *self.customerSaleRepresentative_loc)

    # 在添加页面，选择一个或多个接入监测类型
    def input_customerMonitoringType(self,
                                     customerMonitoringTypeList         # 客户类型，str，逗号分隔，例如：'电,水'
                                     ):
        datalist = str(customerMonitoringTypeList).split(',')
        # 验证传入的接入监测类型list长度是否大于1，否则报错
        try:
            assert len(datalist) >= 1, '参数错误：customerMonitoringTypeList长度不足'
        except AssertionError as e:
            self.mylog.error('参数错误：customerMonitoringTypeList长度不足')
            raise e
        # 循环选择
        for m in datalist:
            n = self.get_elementNum(m, *self.customerMonitoringType_loc)
            self.click(
                By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom '
                                 '> div > div > div > div.ng-scope > div > div > form > div:nth-child(3) > '
                                 'div.form-group > div.col-sm-7.col-md-6.col-lg-5.mg-top6p > div:nth-child(%s) > '
                                 'div.checkboxFive.ng-isolate-scope > div' % n)

    # 选择是否签约
    def input_customerIfSign(self, ifSign):
        n = self.get_elementNum(str(ifSign), *self.customerIfSign_loc)
        self.click(
            By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > '
                             'div > div > div > div.ng-scope > div > div > form > div:nth-child(3) > div.form-group '
                             '> div.col-sm-7.col-md-6.col-lg-5.control-div > div:nth-child(%s) > '
                             'div.fl-left.mg-rt4p.mg-top3p > label > span.toggle-radio' % n)

    # 点击保存按钮
    def click_submitCreateCustomerButton(self):
        self.click(*self.submitCreateCustomerButton_loc)

    # 点击取消按钮
    def click_cancelCreateCustomerButton(self):
        self.click(*self.cancelCreateCustomerButton_loc)

    # 获取提示消息
    def get_customerInfo(self):
        info_loc = self.find_element(*self.customerInfo_loc)
        return info_loc.text

    # 点击提示消息弹窗中的立即关闭按钮
    def click_closeCustomerInfo(self):
        self.click(*self.closeCustomerInfo_loc)

    # 在详情页面，点击返回按钮
    def click_goBackButton_inCustomerDetail(self):
        self.click(*self.goBackButton_inCustomerDetail_loc)
