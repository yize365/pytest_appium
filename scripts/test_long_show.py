# @File  : test_long_show.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:
import sys,os
sys.path.append(os.getcwd())
from Base.init_driver import init_driver
from Page.Page_Test_All import Page_Test_All
import pytest
class Test_long_show:
    def setup_class(self):
        self.driver = init_driver()
        self.All = Page_Test_All(self.driver).long_show_o()
        print("开始")
    def teardown_class(self):
        self.driver.quit()
        print("结束")
    def test_long_show_001(self):
        self.All.click_xs_btn()
        self.All.click_sleep_btn()
        self.All.click_sleep_time()