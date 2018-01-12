# coding:utf-8
__author__ = 'luws'

from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

'''
登录页面基本方法
'''


class login_page(BasePage):
    # 定位器-后台
    username_loc = (By.ID, 'username')      # 用户名
    password_loc = (By.ID, 'pwd')       # 密码
    rememberPwd_loc = (By.CSS_SELECTOR, "label[for='www']")        # 记住密码
    login_loc = (By.CSS_SELECTOR, "button[data-ng-click='loginIn()']")      # 登录按钮
    getUsername_loc = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")        # 登录后首页右上角的用户名
    loginInfo_loc = (By.CSS_SELECTOR, "span[data-ng-show='msgShow']")       # 登录页面点击登录后的错误提示
    # 定位器-前台
    username1_loc = (
        By.CSS_SELECTOR, "#root > div > div > div[class^='loginBody'] > div[class^='bodyContent'] > "
                         "div[class^='bodyInput'] > div:nth-child(3) > div[class^='inputField'] > p:nth-child(1) > "
                         "input[type='text']")  # 用户名
    password1_loc = (
        By.CSS_SELECTOR, "#root > div > div > div[class^='loginBody'] > div[class^='bodyContent'] > "
                         "div[class^='bodyInput'] > div:nth-child(3) > div[class^='inputField'] > p:nth-child(2) > "
                         "input[type='password']")  # 密码
    login1_loc = (By.CSS_SELECTOR, "div[class^='loginBtn']")  # 登录按钮

    # 打开后台登录页面
    def open(self):
        self._open(self.url, self.title)

    # 在后台页面，输入用户名
    def input_username(self,
                       username     # 登录用户名，str
                       ):
        self.find_element(*self.username_loc).send_keys(str(username))

    # 在后台页面，输入密码
    def input_password(self,
                       password     # 登录密码，str
                       ):
        self.find_element(*self.password_loc).send_keys(str(password))

    # 在后台页面，点击记住密码
    def click_rememberPwd(self):
        self.click(*self.rememberPwd_loc)

    # 在后台页面，点击登录按钮
    def click_login(self):
        self.click(*self.login_loc)

    # 在后台页面，获取登录后页面右上角的账号
    def get_username(self):
        return self.find_element(*self.getUsername_loc).text

    # 在后台页面，获取登录页面的登录错误提示
    def get_loginInfo(self):
        return self.find_element(*self.loginInfo_loc).text

    # 在前台页面，输入用户名
    def input_username1(self, username):
        self.find_element(*self.username1_loc).send_keys(str(username))

    # 在前台页面，输入密码
    def input_password1(self, password):
        self.find_element(*self.password1_loc).send_keys(str(password))

    # 在前台页面，点击登录按钮
    def click_login1(self):
        self.click(*self.login1_loc)
