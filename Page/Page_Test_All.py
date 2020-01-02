# @File  : Page_Test_All.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:统一出口类
from Page.closed_wlan import Closed_WLAN
from Page.long_show import Long_Show
from Page.mes_set import Set_Msg
from Page.toutiao_login import Toutiao_Login
from Page.search_page import Search_Page
class Page_Test_All:
    def __init__(self,driver):
        self.driver=driver
    #关闭WLAN功能
    def closed_wlan_o(self):
        return Closed_WLAN(self.driver)

    #设置亮屏时间
    def long_show_o(self):
        return Long_Show(self.driver)

    # 发送信息
    def send_msg_o(self):
        return Set_Msg(self.driver)

    #头条登录
    def toutiao_login_o(self):
        return Toutiao_Login(self.driver)
    #搜索页面
    def search_page_o(self):
        return Search_Page(self.driver)