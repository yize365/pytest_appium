# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 13:39
# @Author  : yize365
# @Email   : 1558570566@qq.com
# @File    : test_toutiao_login.py
# @Software: PyCharm
import sys,os
sys.path.append(os.getcwd())
from Base.init_driver import init_driver
from Page.Page_Test_All import Page_Test_All
import pytest
class Test_mes_set:
    def setup_class(self):
        self.driver = init_driver()
        self.All = Page_Test_All(self.driver).toutiao_login_o()
        print("开始")
    def teardown_class(self):
        self.driver.quit()
        print("结束")

    @pytest.mark.paramtrize("phone,pwd",[("15938707946","19900102"),("15938707946",""),("","19900102")])
    def test_toutiao_login_001(self,phone,pwd):
        self.All.cli_my_btn()
        self.All.cli_login_btn()
        self.All.cli_eml_btn()
        self.All.input_eml_txt(phone)
        self.All.input_pwd_txt(pwd)
        self.All.cli_log_btn()