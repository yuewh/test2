# coding:utf-8
__author__ = 'luws'
from src.pages.deviceManagement_page import deviceManagement_page
from time import sleep

'''
设备管理组合方法
'''


class deviceManagement(deviceManagement_page):
    # 点击对应的一次设备按钮
    def click_primaryDevice(self, powerClientName):
        self.click_model()
        self.input_search(powerClientName)
        self.click_search()
        self.click_primaryDeviceButton(powerClientName)
        sleep(0.5)

    # 点击对应的二次设备按钮
    def click_secondaryDevice(self, powerClientName):
        self.click_model()
        self.input_search(powerClientName)
        self.click_search()
        self.click_secondaryDeviceButton(powerClientName)
