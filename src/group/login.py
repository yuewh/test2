# coding:utf-8
__author__ = 'luws'

from src.pages.login_page import login_page


class login(login_page):

    # 后台页面登录
    def login(
            self,
            username='admin_yny',           # 登录用户名，str
            password='123456'):             # 登录密码，str

        # 校验参数合法性

        # action
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_rememberPwd()
        self.click_login()

    # 前台页面登录
    def login1(self, username='admin_ynyys', password='yny123'):
        # action
        self.open()
        self.input_username1(username)
        self.input_password1(password)
        self.click_login1()
