# coding:utf-8
__author__ = 'luws'
from src.pages.customer_page import customer_page

'''
客户信息管理页面组合方法
'''


class customer(customer_page):
    # 根据客户简称，删除单个客户
    def delete_customer(self, customerShortname):
        self.search_customer(customerShortname)
        a = int(self.get_customerTotalSize())
        # 若搜索后总条数在10-20之间，只需要每页显示20条就可以点击到
        if 10 < a <= 20:
            self.click_customerPageSizeButton_20()
            self.click_deleteCustomerButton(customerShortname)
        # 若搜索后总条数在小于10，直接就可以点击到
        elif a <= 10:
            self.click_deleteCustomerButton(customerShortname)
        # 若搜索后总条数在大于，先每页显示20条，找不到再点下一页
        elif a > 20:
            self.click_customerPageSizeButton_20()
            for i in range((a // 20)+2):
                shortNameList = self.get_CustomerNameList()
                if customerShortname in shortNameList:
                    self.click_deleteCustomerButton(customerShortname)
                    break
                # 最后一次循环若还是找不到，就报错
                else:
                    if i < (a // 20)+1:
                        self.click_customerGoDownButton()
                    else:
                        self.mylog.error('参数错误：找不到%s' % customerShortname)
        self.click_submitDeleteCustomerButton()
        print(self.get_customerInfo())

    # 根据客户简称，编辑单个客户
    def update_customer(self, customerShortname):
        self.search_customer(customerShortname)
        a = int(self.get_customerTotalSize())
        if 10 < a <= 20:
            self.click_customerPageSizeButton_20()
            self.click_updateCustomerButton(customerShortname)
        elif a <= 10:
            self.click_updateCustomerButton(customerShortname)
        elif a > 20:
            self.click_customerPageSizeButton_20()
            # 每页轮询，找到简称后，再去点击
            for i in range((a // 20) + 2):
                shortNameList = self.get_CustomerNameList()
                if customerShortname in shortNameList:
                    self.click_updateCustomerButton(customerShortname)
                    break
                # 最后一次循环若还是找不到，就报错
                else:
                    if i < (a // 20) + 1:
                        self.click_customerGoDownButton()
                    else:
                        self.mylog.error('参数错误：找不到%s' % customerShortname)

    # 根据客户简称，查看单个客户详情
    def query_customer(self, customerShortname):
        self.search_customer(customerShortname)
        a = int(self.get_customerTotalSize())
        if 10 < a <= 20:
            self.click_customerPageSizeButton_20()
            self.click_customerDetailButton(customerShortname)
        elif a <= 10:
            self.click_customerDetailButton(customerShortname)
        elif a > 20:
            self.click_customerPageSizeButton_20()
            for i in range((a // 20) + 2):
                shortNameList = self.get_CustomerNameList()
                if customerShortname in shortNameList:
                    self.click_customerDetailButton(customerShortname)
                    break
                # 最后一次循环若还是找不到，就报错
                else:
                    if i < (a // 20) + 1:
                        self.click_customerGoDownButton()
                    else:
                        self.mylog.error('参数错误：找不到%s' % customerShortname)

    # 选择上级客户组合方法
    def input_parentCustomer(self, parentCustomer):
        self.click_parentCustomerButton()
        self.click_parentCustomer(parentCustomer)
        self.click_submitParentCustomer()

    # 选择服务商组合方法
    def input_customerServiceProvider(self, customerServiceProvider):
        self.click_customerServiceProviderButton()
        self.click_parentCustomer(customerServiceProvider)
        self.click_submitParentCustomer()

    # 创建一个服务商，输入必填字段
    def create_Customer_inputRequired(self, customerName,  # 客户名称
                                      customerShortName,  # 客户简称
                                      customerType='国有企业',  # 企业性质
                                      customeProvince='浙江省',  # 所在省
                                      customerCity='杭州市',  # 所在市
                                      customerCounty='西湖区',  # 所在区
                                      customerIdentityType='安装运维商',  # 客户类型，str，逗号分隔，例如：'用能企业,安装运维商'
                                      customerDistributor='直销',  # 渠道类型， 默认选直销，也可选网上订阅，不用输入渠道名称
                                      ):
        # 校验参数
        assert '用能企业' not in customerIdentityType.split(','), '参数错误：创建服务商时，客户类型不可选用能企业'
        assert customerDistributor == '直销' or customerDistributor == '网上订阅', '参数错误：渠道类型字段在本方法中只能选择直销或网上订阅'
        # action
        self.click_createCudtomerButton()
        self.input_customerName(customerName)
        self.input_customerShortName(customerShortName)
        self.input_customerType(customerType)
        self.input_customeProvince(customeProvince)
        self.input_customerCity(customerCity)
        self.input_customerCounty(customerCounty)
        self.input_customerIdentityType(customerIdentityType)
        self.input_customerDistributor(customerDistributor)
        self.click_submitCreateCustomerButton()
        msg = self.get_customerInfo()
        self.click_closeCustomerInfo()
        return msg

    # 创建一个服务商，输入所有字段
    def create_Customer_inputAll(self,
                                 customerName,  # 客户名称
                                 customerShortName,  # 客户简称
                                 customerType='国有企业',  # 企业性质
                                 customeCompanyScale='1~49人',  # 企业规模
                                 customerIntroduction='',  # 企业简介
                                 customerRegisteredCapital='',  # 注册资本金
                                 customerArtificialPerson='',  # 法人代表
                                 customerMainBusinesses='',  # 主营业务
                                 customerBusinessScopes='',  # 经营范围
                                 customerMainProducts='',  # 主要产品
                                 customerWebsite='',  # 企业网址
                                 customerEmail='',  # 电子邮箱
                                 customerTelphone='',  # 企业总机
                                 customerFax='',  # 传真号码
                                 parentCustomer='平台测试',  # 上级客户
                                 customeProvince='浙江省',  # 所在省
                                 customerCity='杭州市',  # 所在市
                                 customerCounty='西湖区',  # 所在区
                                 customerStreet='',  # 街道
                                 customerAddress='',  # 详细地址
                                 customerPostcode='',  # 邮编
                                 customerIdentityType='安装运维商',  # 客户类型，str，逗号分隔，例如：'用能企业,安装运维商'
                                 customerDistributor='代理',  # 渠道类型， 默认选代理
                                 customerDistributorName='平台测试',  # 渠道名称，渠道类型为代理或推荐时必填
                                 customerSaleRepresentative='',  # 销售代表
                                 customerMonitoringType='水,电',  # 接入监测类型
                                 customerIfSign='是',  # 是否签约
                                 ):
        # 校验参数
        assert '用能企业' not in customerIdentityType.split(','), '参数错误：创建服务商时，客户类型不可选用能企业'
        # action
        self.click_createCudtomerButton()
        self.input_customerName(customerName)
        self.input_customerShortName(customerShortName)
        self.input_customerType(customerType)
        self.input_customeCompanyScale(customeCompanyScale)
        self.input_customerIntroduction(customerIntroduction)
        self.input_customerRegisteredCapital(customerRegisteredCapital)
        self.input_customerArtificialPerson(customerArtificialPerson)
        self.input_customerMainBusinesses(customerMainBusinesses)
        self.input_customerBusinessScopes(customerBusinessScopes)
        self.input_customerMainProducts(customerMainProducts)
        self.input_customerWebsite(customerWebsite)
        self.input_customerEmail(customerEmail)
        self.input_customerTelphone(customerTelphone)
        self.input_customerFax(customerFax)
        self.input_parentCustomer(parentCustomer)
        self.input_customeProvince(customeProvince)
        self.input_customerCity(customerCity)
        self.input_customerCounty(customerCounty)
        self.input_customerStreet(customerStreet)
        self.input_customerAddress(customerAddress)
        self.input_customerPostcode(customerPostcode)
        self.input_customerIdentityType(customerIdentityType)
        self.input_customerDistributor(customerDistributor)
        if customerDistributor == '代理' or customerDistributor == '推荐':
            self.input_customerDistributorName(customerDistributorName)
        self.input_customerSaleRepresentative(customerSaleRepresentative)
        self.input_customerMonitoringType(customerMonitoringType)
        self.input_customerIfSign(customerIfSign)
        self.click_submitCreateCustomerButton()
        msg = self.get_customerInfo()
        self.click_closeCustomerInfo()
        return msg

    # 创建一个企业，输入必填字段
    def create_company_inputRequired(self, companyName,  # 客户名称
                                     companyShortName,  # 客户简称
                                     companyType='国有企业',  # 企业性质
                                     companyProvince='浙江省',  # 所在省
                                     companyCity='杭州市',  # 所在市
                                     companyCounty='西湖区',  # 所在区
                                     companyIdentityType='用能企业',  # 客户类型，str，逗号分隔，例如：'用能企业,安装运维商'
                                     companyDistributor='直销',  # 渠道类型， 默认选直销，也可选网上订阅，不用输入渠道名称
                                     companyServiceProvider='平台测试'  # 服务商
                                     ):
        # 校验参数
        assert '用能企业' in companyIdentityType.split(','), '参数错误：创建企业时，客户类型必须要选用能企业'
        assert companyDistributor == '直销' or companyDistributor == '网上订阅', '参数错误：渠道类型字段在本方法中只能选择直销或网上订阅'
        # action
        self.click_createCudtomerButton()
        self.input_customerName(companyName)
        self.input_customerShortName(companyShortName)
        self.input_customerType(companyType)
        self.input_customeProvince(companyProvince)
        self.input_customerCity(companyCity)
        self.input_customerCounty(companyCounty)
        self.input_customerIdentityType(companyIdentityType)
        self.input_customerDistributor(companyDistributor)
        self.input_customerServiceProvider(companyServiceProvider)
        self.click_submitCreateCustomerButton()
        msg = self.get_customerInfo()
        self.click_closeCustomerInfo()
        return msg

    # 创建一个企业，输入所有字段
    def create_company_inputAll(self, companyName,  # 客户名称
                                companyShortName,  # 客户简称
                                companyType='国有企业',  # 企业性质
                                companyCompanyScale='1~49人',  # 企业规模
                                companyIntroduction='',  # 企业简介
                                companyRegisteredCapital='',  # 注册资本金
                                companyArtificialPerson='',  # 法人代表
                                companyMainBusinesses='',  # 主营业务
                                companyBusinessScopes='',  # 经营范围
                                companyMainProducts='',  # 主要产品
                                companyWebsite='',  # 企业网址
                                companyEmail='',  # 电子邮箱
                                companyTelphone='',  # 企业总机
                                companyFax='',  # 传真号码
                                parentCompany='平台测试',  # 上级客户
                                companyProvince='浙江省',  # 所在省
                                companyCity='杭州市',  # 所在市
                                companyCounty='西湖区',  # 所在区
                                customerStreet='',  # 街道
                                companyAddress='',  # 详细地址
                                companyPostcode='',  # 邮编
                                companyIdentityType='用能企业',  # 客户类型，str，逗号分隔，例如：'用能企业,安装运维商'
                                companyDistributor='代理',  # 渠道类型， 默认选代理
                                companyDistributorName='平台测试',  # 渠道名称，渠道类型为代理或推荐时必填
                                companyServiceProvider='平台测试',  # 服务商
                                companySaleRepresentative='',  # 销售代表
                                companyMonitoringType='水,电',  # 接入监测类型
                                companyIfSign='是',  # 是否签约
                                ):
        # 校验参数
        assert '用能企业' in companyIdentityType.split(','), '参数错误：创建企业时，客户类型必须要选用能企业'
        # action
        self.click_createCudtomerButton()
        self.input_customerName(companyName)
        self.input_customerShortName(companyShortName)
        self.input_customerType(companyType)
        self.input_customeCompanyScale(companyCompanyScale)
        self.input_customerIntroduction(companyIntroduction)
        self.input_customerRegisteredCapital(companyRegisteredCapital)
        self.input_customerArtificialPerson(companyArtificialPerson)
        self.input_customerMainBusinesses(companyMainBusinesses)
        self.input_customerBusinessScopes(companyBusinessScopes)
        self.input_customerMainProducts(companyMainProducts)
        self.input_customerWebsite(companyWebsite)
        self.input_customerEmail(companyEmail)
        self.input_customerTelphone(companyTelphone)
        self.input_customerFax(companyFax)
        self.input_parentCustomer(parentCompany)
        self.input_customeProvince(companyProvince)
        self.input_customerCity(companyCity)
        self.input_customerCounty(companyCounty)
        self.input_customerStreet(customerStreet)
        self.input_customerAddress(companyAddress)
        self.input_customerPostcode(companyPostcode)
        self.input_customerIdentityType(companyIdentityType)
        self.input_customerDistributor(companyDistributor)
        if companyDistributor == '代理' or companyDistributor == '推荐':
            self.input_customerDistributorName(companyDistributorName)
        self.input_customerServiceProvider(companyServiceProvider)
        self.input_customerSaleRepresentative(companySaleRepresentative)
        self.input_customerMonitoringType(companyMonitoringType)
        self.input_customerIfSign(companyIfSign)
        self.click_submitCreateCustomerButton()
        msg = self.get_customerInfo()
        self.click_closeCustomerInfo()
        return msg
