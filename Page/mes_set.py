# @File  : mes_set.py
# @Author: yize365
# @Date  :  2019/12/29
# @Function:
# @Remarks:
from Base.BasePage import BasePage
import Page
class Set_Msg(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    #点击添加信息按钮
    def add_msg_btn(self):
        self.click_element_base(Page.cli_new_msg)
    #输入接受者
    def accept_user_input(self,phone):
        self.input_msg_base(Page.input_pnum,phone)
    #输入发送的信息,发送
    def send_msg_input(self,text):
        self.input_msg_base(Page.input_mse_txt,text)
        #点击发送按钮
        self.click_element_base(Page.cli_sent)