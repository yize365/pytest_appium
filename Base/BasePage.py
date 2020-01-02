# @File  : BasePage.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:
# from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    #查找元素
    def find_element_base(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_element(*loc))
    #查找一组元素
    def find_elements_base(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_elements(*loc))

    #判断元素是否存在,作为检查操作是否成功的函数
    def if_disp(self,loc):
        try:
            self.find_element_base(loc)
            return True
        except Exception as e:
            return False

    #点击元素
    def click_element_base(self,loc):
        self.find_element_base(loc).click()

    #输入信息
    def input_msg_base(self,loc,intext):
        input=self.find_element_base(loc)
        input.clear()
        input.send_keys(intext)