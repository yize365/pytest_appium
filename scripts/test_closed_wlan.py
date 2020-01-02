# @File  : test_closed_wlan.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:
import sys,os
sys.path.append(os.getcwd())
from Base.init_driver import init_driver
from Page.Page_Test_All import Page_Test_All
import pytest,allure

@allure.feature("关闭WLAN测试")
class Test_close_wlan:
    def setup_class(self):
        self.driver=init_driver()
        self.All=Page_Test_All(self.driver).closed_wlan_o()
        print("开始")

    def teardown_class(self):
        self.driver.quit()
        print("结束")

    @allure.story("我是测试步骤01")
    @allure.description('描述我是测试步骤001的描述～～～')
    @allure.step("测试关闭或者开启成功")
    @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
    def test_close_wlan_001(self):
        with allure.step('1.点击WLAN 2.点击开关'.format()):
            #点击WLAN
            self.All.click_wlan_btn()
            #关闭WLAN
            self.All.closed_wlan()

    @pytest.mark.parametrize("a",[1,2,3])
    @allure.story("这是测试步骤02")
    @allure.description('描述我是测试步骤002的描述～～～')
    @allure.testcase('http://www.baidu.com') #添加测试用例
    @allure.severity(allure.severity_level.CRITICAL) #严重级别
    def test_abc(self,a):
        print("你好哈!")
        assert a != 2

    #执行转化为html报告allure generate report/ -o reports