# @File  : click_wlan.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:
#需要的操作进行封装
#打开设置,找到Wlan,点击关闭 WLAN
#数据提取到__init__.py中,导入Page包,直接使用Page.XXX进行调用
from Base.BasePage import BasePage
import Page
class Closed_WLAN(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self, driver)

    #找到并点击wlan
    #定位方式 name id  class_name  tag_name
    #将需要的参数,统一放在文件中进行读取(由变量进行传递)
    def click_wlan_btn(self):
        self.click_element_base(Page.cli_wla)

    #找到并点击关闭
    def closed_wlan(self):
        self.click_element_base(Page.cli_clo)

