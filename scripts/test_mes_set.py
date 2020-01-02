# @File  : test_mes_set.py
# @Author: yize365
# @Date  :  2019/12/29
# @Function:
# @Remarks:
import sys,os
sys.path.append(os.getcwd())
from Base.init_driver import init_driver
from Page.Page_Test_All import Page_Test_All
import pytest
class Test_mes_set:
    def setup_class(self):
        self.driver = init_driver()
        self.All = Page_Test_All(self.driver).send_msg_o()
        print("开始")
    def teardown_class(self):
        self.driver.quit()
        print("结束")
    def test_mes_set_001(self):
        self.All.add_msg_btn()
        self.All.accept_user_input("13888889999")
        self.All.send_msg_input("你好中国移动通知您中奖5000万")