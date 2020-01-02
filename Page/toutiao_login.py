# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 13:34
# @Author  : yize365
# @Email   : 1558570566@qq.com
# @File    : toutiao_login.py
# @Software: PyCharm
from Base.BasePage import BasePage
import Page
class Toutiao_Login(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self, driver)

    #点击我的
    def cli_my_btn(self):
        self.click_element_base(Page.cli_my_tt)
    #点击登录
    def cli_login_btn(self):
        self.click_element_base(Page.cli_in_tt)
    #点击密码登录
    def cli_eml_btn(self):
        self.click_element_base(Page.clo_em_tt)
    #输入账号
    def input_eml_txt(self,phone):
        self.input_msg_base(Page.input_em_tt,phone)
    #输入密码
    def input_pwd_txt(self,password):
        self.input_msg_base(Page.inpwd_em_tt,password)
    #点击登录
    def cli_log_btn(self):
        self.click_element_base(Page.cli_login_tt)