# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from time import sleep
from src.common.log import log

'''
设备管理基本方法
'''


class deviceManagement_page(BasePage):
    """ 定位器 """
    model_loc = (By.CSS_SELECTOR, '.tt2 > ul > li:nth-child(3)')     # 设备管理按钮

    searchInput_loc = (By.CSS_SELECTOR, "input[data-ng-model='keyword']")      # 搜索框
    searchButton_loc = (By.CSS_SELECTOR, "button[type='submit']")        # 搜索按钮
    filterProvince_loc = (By.CSS_SELECTOR, "a[data-ng-click='showList(1,$event)']")        # 筛选省
    filterCity_loc = (By.CSS_SELECTOR, "a[data-ng-click='showList(2,$event)']")        # 筛选市
    filterCounty_loc = (By.CSS_SELECTOR, "a[data-ng-click='showList(3,$event)']")        # 筛选区
    powerClientNameList_loc = (By.CSS_SELECTOR, "td[my-title='item.powerClientName ']")     # 用电客户名称列
    secondaryDeviceButtonList_loc = (By.CLASS_NAME, 'mg-lf6p')      # 二次设备按钮列

    # 点击设备管理按钮
    def click_model(self):
        self.click(*self.model_loc)

    # 输入搜索关键字
    def input_search(self, key):
        self.find_element(*self.searchInput_loc).send_keys(key)

    # 点击搜索按钮
    def click_search(self):
        self.click(*self.searchButton_loc)
        sleep(1)

    # 点击筛选省按钮
    def click_filterProvince(self):
        self.click(*self.filterProvince_loc)

    # 点击筛选市按钮
    def click_filterCity(self):
        self.click(*self.filterCity_loc)

    # 点击筛选区按钮
    def click_filterCounty(self):
        self.click(*self.filterCounty_loc)

    # 点击一次设备按钮
    def click_primaryDeviceButton(self,
                                  powerClientName       # 要点击的用电客户，str
                                  ):
        # 此处由于默认进入的客户信息管理页面也有同样的定位，原有的元素定位加强不可用，只能另外写循环
        for i in range(21):
            try:
                n = self.get_elementNum(str(powerClientName), *self.powerClientNameList_loc)
                self.click(By.CSS_SELECTOR, 'tbody > tr:nth-child(%s) > td:nth-child(8) > div > a' % n)
                break
            except Exception:
                sleep(0.5)
            if i == 20:
                log().error('点击一次设备按钮失败')

    # 点击二次设备按钮
    def click_secondaryDeviceButton(self,
                                    powerClientName       # 要点击的用电客户，str
                                    ):
        # 此处由于默认进入的客户信息管理页面也有同样的定位，原有的元素定位加强不可用，只能另外写循环
        for i in range(21):
            try:
                n = self.get_elementNum(str(powerClientName), *self.powerClientNameList_loc)
                sleep(1)
                self.click(By.CSS_SELECTOR, 'tbody > tr:nth-child(%s) > td:nth-child(8) > div > a:nth-child(2)' % n)
                break
            except Exception:
                sleep(0.5)
            if i == 20:
                log().error('点击二次设备按钮失败')
        self.switch_to_window()

