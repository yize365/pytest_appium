# @File  : land_toutiao.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:
#进入设置,找到并点击显示,找到并点击休眠,设置休眠时间
from Base.BasePage import BasePage
import Page
class Long_Show(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
    #点击显示
    def click_xs_btn(self):
        self.click_element_base(Page.cli_xs)
    #点击休眠
    def click_sleep_btn(self):
        self.click_element_base(Page.cli_xm)
    #点击设置休眠时间
    def click_sleep_time(self):
        self.click_element_base(Page.cli_thr)
