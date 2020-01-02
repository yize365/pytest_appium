# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 8:56
# @Author  : yize365
# @Email   : 1558570566@qq.com
# @File    : search_page.py
# @Software: PyCharm
from Base.BasePage import BasePage
import Page
class Search_Page(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_search_btn(self):
        # 点击搜索按钮
        self.click_element_base(Page.search_btn_sp)
    def search_input(self, text):
        # 输入
        self.input_msg_base(Page.search_text_sp, text)
    def search_return(self):
        # 点击返回
        self.click_element_base(Page.search_return_sp)
