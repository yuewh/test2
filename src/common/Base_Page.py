# coding:utf-8
__author__ = 'luws'
from src.common import log
from config.globalparameter import img_path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time

'''
project:封装页面公用方法
'''


class BasePage(object):
    def __init__(self, selenium_driver, page_title='云运营--后台', base_url='http://10.1.170.76:16002'):
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title
        self.mylog = log.log()

    # 打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.implicitly_wait(10)
            self.driver.get(url)
            # self.mylog.info('打开页面：' + self.driver.title)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, '打开页面失败：%s' % url
        except Exception as e:
            self.mylog.error('未能正确打开页面:' + url)
            raise e

    # 重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            self.mylog.error('找不到元素:' + str(loc))
            raise e

    # 重写find_elements方法，增加定位元素的健壮性
    def find_elements(self, *loc):
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            self.mylog.error('找不到元素:' + str(loc))
            raise e

    # 重写send_keys方法
    def send_keys(self, value, *loc, clear=True):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).clear()     # clear存在bug，有时会失败且不报错
                self.find_element(*loc).send_keys(str(value))
        except AttributeError:
            self.mylog.error('输入失败：loc=' + str(loc) + ';value=' + value)

    # 重写click方法，避免一些元素不可点击的错误
    def click(self, *loc):
        try:
            clickobject = self.find_element(*loc)
        except Exception as e:
            self.mylog.error('找不到元素:' + str(loc))
            raise e
        for i in range(21):
            try:
                clickobject.click()
                break
            except Exception:
                sleep(1)
            if i == 20:
                self.mylog.error('元素点击失败:' + str(loc))

    # 截图
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path + img_name + '.png')
        except:
            self.mylog.error('截图失败：' + img_name)

    # 定位到当前页面
    def switch_to_window(self):
        windows1 = self.driver.current_window_handle
        windows = self.driver.window_handles
        for window in windows:
            if window != windows1:
                self.driver.switch_to.window(window)

    # 下拉框选择,适用于二次设备的页面，下拉框逻辑为：点击下拉框后最下面出现一个装有选项list的div标签
    def select_in_LastDiv(self, value):
        sleep(0.5)
        selectList_loc = (By.CSS_SELECTOR, 'body > div:last-child > div > div > div > ul > li')  # 下拉框的选项列表
        selectList = self.find_elements(*selectList_loc)
        num = 0
        correctList = []
        for i in range(12):
            if selectList[0].text == '':
                selectList = self.find_elements(*selectList_loc)  # 如果为空，重新获取列表内容
            elif i == 11:
                self.mylog.error('找不到下拉选项的内容')
            else:
                break
        for n in selectList:
            num += 1
            _value = n.text
            correctList.append(_value)
            if num == len(selectList):
                try:
                    assert str(value) == _value, '输入参数错误：' + value + '，请输入：' + str(correctList)
                    n.click()
                except Exception as e:
                    self.mylog.error('输入参数错误：' + value + '，请输入：' + str(correctList))
                    raise e
            else:
                if str(value) == _value:
                    n.click()
                    break

    # 重写selenium中的select方法
    def select_by_option(self, value,  # 要选择的值(下拉框中显示的值)
                         *loc  # select标签的定位
                         ):
        loc = self.find_element(*loc)
        try:
            select = Select(loc)
            return select.select_by_visible_text(str(value))
        except NoSuchElementException:
            self.mylog.error('参数错误：下拉选项中找不到"%s"' % str(value))
            self.driver.quit()

    # 下拉框选择（输入elements的定位，根据value找到其中一个element，并点击）
    def click_valueFromList(self, value,  # 要选择的值
                            valueListLoc  # 含有选项文本的elements的定位
                            ):
        n = self.get_elementNum(value, *valueListLoc)
        SelectList = self.find_elements(*valueListLoc)
        for i in range(11):
            try:
                SelectList[n - 1].click()
                break
            except Exception:
                sleep(0.5)
            if i == 10:
                self.mylog.error('元素点击失败:' + str(value))
                raise TimeoutError

    # 校验日期参数格式是否为YYYY-MM-DD
    def check_dataFormat(self, value, format="%Y-%m-%d"):
        try:
            assert time.strptime(str(value), format), '参数错误：%s不符合%s的格式' % (str(value), format)
        except ValueError:
            self.mylog.error('参数错误：%s不符合YYYY-MM-DD的格式' % str(value))

    # 校验参数类型
    def check_parameterType(self, parameter, parameterType):
        if type(parameter) != parameterType:
            self.mylog.warning('参数错误：%s的类型应为%s' % (str(parameter), str(parameterType)))

    # 根据给定字段轮询,返回轮询次数,用于指定字段所在行的其他字段的定位
    def get_elementNum(self, value, *loc):
        elementNum = 1
        elements = self.find_elements(*loc)
        # 排除StaleElementReferenceException（页面已刷新，获取的还是原来的定位，此时去点击就会报错，所以当报错时，重新更新elements，获取最新的定位）
        for i in range(10):
            try:
                a = elements[0].text
                break
            except Exception:
                sleep(0.5)
                elements = self.find_elements(*loc)
        # 根据value去查到定位位置，最后一次找不到时抛出异常
        datalist = []
        for n in elements:
            datalist.append(n.text)
            if str(value) == n.text:
                return elementNum
            elementNum += 1
            try:
                assert elementNum <= len(elements), '输入参数错误：找不到' + value + '，请输入：' + str(datalist)
            except AssertionError as e:
                # 最后一次找不到时，才报错
                self.mylog.error('输入参数错误：找不到' + value + '，请输入：' + str(datalist))
                raise e

    # 获取某一列的字段文本，存储到datalist
    def get_infoList(self, *loc):
        datalist = []
        List_loc = self.find_elements(*loc)
        for n in List_loc:
            text = n.text
            datalist.append(text)
        return datalist

