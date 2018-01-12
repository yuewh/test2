# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from time import sleep

'''
一次设备页面基本方法
'''


class primaryDevice_page(BasePage):
    """定位器"""
    primaryDeviceName_loc = (By.CSS_SELECTOR, "span[data-ng-click='select(item,$event)']")      # 设备层级树
    createChildDevice_loc = (                                                                    # 添加下级按钮
        By.CSS_SELECTOR, '#powerStrategy-left > div.padding-l0p > span.text-left > a')
    createChildDeviceTypeList_loc = (                                                            # 添加下级中的设备种类list
        By.CSS_SELECTOR, '#powerStrategy-left > div.padding-l0p > div > div > a')
    deletePrimaryDeviceButton_loc = (                                                           # 删除按钮
        By.CSS_SELECTOR, '#powerStrategy-left > div.padding-l0p > span.fl-right.glyphicon.glyphicon-trash')
    submitdeletePrimaryDeviceButton_loc = (                                                     # 删除设备的二次确认弹窗中的确认按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button:nth-child(2)')
    canceldeletePrimaryDeviceButton_loc = (                                                     # 删除设备的二次确认弹窗中的取消按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button:nth-child(1)')
    closePrimaryDeviceInfo_loc = (                                                              # 操作完成的弹窗中的立即关闭按钮
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer.text-center > '
                         'button')
    primaryDeviceInfo_loc = (                                                                   # 操作完成的弹窗中的文字
        By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body > '
                         'div.text-center.modal-msg > span')
    primaryDeviceMoniteringSite_loc = (                                                         # 非配电房层级的监测点Tab页
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.powerStrategy-right.dataZn.th.mg-lf10p.top-15p > div:nth-child(1) > div > '
                         'div:nth-child(2)')
    GoToSecondaryDeviceButton_loc = (                                                           # 二次设备维护按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.powerStrategy-right.dataZn.th.mg-lf10p.top-15p > div:nth-child(1) > div > '
                         'div.fl-right > button.no-btnstyle')
    BackToDeviceManagementButton_loc = (                                                        # 返回用电客户列表按钮
        By.CSS_SELECTOR, 'body > div.body.ng-scope > div > div.ng-scope > div > div > div.right-bj.top-bottom > div > '
                         'div > div > div.powerStrategy-right.dataZn.th.mg-lf10p.top-15p > div:nth-child(1) > div > '
                         'div.fl-right > button.btn.btn-sty.mg-lf10p.no-radius')
    updatePrimaryDeviceButton_loc = (                                                           # 编辑按钮
        By.CSS_SELECTOR, "button[data-ng-click='edit(model)']")
    submitCreatePrimaryDeviceButton_loc = (                                                      # 添加设备的确定按钮
        By.CSS_SELECTOR, "button[data-ng-click='commit()']")
    cancelCreatePrimaryDeviceButton_loc = (                                                      # 添加设备的取消按钮
        By.CSS_SELECTOR, "button[data-ng-click='cancel()']")

    # 点击设备层级
    def click_primaryDeviceName(self, primaryDeviceName):
        self.click_valueFromList(primaryDeviceName, self.primaryDeviceName_loc)

    # 点击添加下级
    def click_createChildDevice(self):
        self.click(*self.createChildDevice_loc)

    # 点击添加下级种类
    def click_createChildDeviceType(self, primaryAddChildType):
        self.click_valueFromList(primaryAddChildType, self.createChildDeviceTypeList_loc)
        sleep(0.5)

    # 点击删除按钮
    def click_deletePrimaryDeviceButton(self):
        self.click(*self.deletePrimaryDeviceButton_loc)

    # 点击删除按钮后二次确认弹窗中的确认按钮
    def click_submitdeletePrimaryDeviceButton(self):
        self.click(*self.submitdeletePrimaryDeviceButton_loc)

    # 点击删除按钮后二次确认弹窗中的取消按钮
    def click_canceldeletePrimaryDeviceButton(self):
        self.click(*self.canceldeletePrimaryDeviceButton_loc)

    # 获取弹窗提示
    def get_primaryDeviceInfo(self):
        info_loc = self.find_element(*self.primaryDeviceInfo_loc)
        return info_loc.text

    # 点击弹窗提示中的立即关闭按钮
    def click_closePrimaryDeviceInfo(self):
        self.click(*self.closePrimaryDeviceInfo_loc)

    # 点击非配电房层级的监测点TAB页
    def click_primaryDeviceMoniteringSiteButton(self):
        self.click(*self.primaryDeviceMoniteringSite_loc)

    # 点击二次设备维护按钮
    def click_GoToSecondaryDeviceButton(self):
        self.click(*self.GoToSecondaryDeviceButton_loc)
        self.switch_to_window()

    # 点击返回用电客户按钮
    def click_BackToDeviceManagementButton(self):
        self.click(*self.BackToDeviceManagementButton_loc)

    # 点击编辑按钮
    def click_updatePrimaryDeviceButton(self):
        self.click(*self.updatePrimaryDeviceButton_loc)

    # 在添加设备页面，点击确定按钮
    def click_submitCreatePrimaryDeviceButton(self):
        self.click(*self.submitCreatePrimaryDeviceButton_loc)

    # 在添加设备页面，点击取消按钮
    def click_cancelCreatePrimaryDeviceButton(self):
        self.click(*self.cancelCreatePrimaryDeviceButton_loc)
