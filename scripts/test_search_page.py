# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 9:02
# @Author  : yize365
# @Email   : 1558570566@qq.com
# @File    : test_search_page.py
# @Software: PyCharm
import sys,os
sys.path.append(os.getcwd())
from Base.init_driver import init_driver
from Page.Page_Test_All import Page_Test_All
from Base.read_data import Read_Data
import pytest
import time
def yaml_data():
    data_list=[]
    data=Read_Data("search_data.yml").ret_yaml_data().get("Search_Data")
    # data=return_data("search_data.yml").get("Search_Data")
    for i in data.keys():
        data_list.append((i, data.get(i).get("test"), data.get(i).get("expect_data")))
    return data_list

#注意事项:这里执行pytest 如果appium是客户端情况下可以正常二次执行,如果是命令行下的appium则不能二次执行.

class Test_search_page:
    def setup_class(self):
        self.driver = init_driver()
        self.All = Page_Test_All(self.driver).search_page_o()
        self.All.click_search_btn()
        print("开始")
    def teardown_class(self):
        self.All.search_return()
        # self.driver.quit()
        self.driver.close_app()
        print("结束")

    @pytest.mark.parametrize("test_num,text,expect_data", yaml_data())
    def test_input_text(self,test_num, text, expect_data):
        print("用例编号",test_num)
        self.All.search_input(text)
        time.sleep(2)
        self.driver.get_screenshot_as_file("D:\pytest_appium\screen\%s.png" % test_num)
        time.sleep(2)
        assert expect_data == 456

# print(yaml_data())
# [('search_001', 1, 456), ('search_002', '中文', 123), ('search_003', '¥……&', 456)]