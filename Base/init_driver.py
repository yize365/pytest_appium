# @File  : init_driver.py
# @Author: yize365
# @Date  :  2019/12/28
# @Function:
# @Remarks:
from appium import webdriver
import time
def init_driver():
    desired_caps = {}
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '5.0'
    # 设备号
    desired_caps['deviceName'] = '192.168.216.101:5555'
    #重置应用状态true不重置  flase重置
    desired_caps['noReset'] = 'true'

    # APP信息# 包名
    #获取 adb shell dumpsys window windows | findstr mFocusedApp
    #短息 com.android.mms/.ui.ConversationList
    #设置的 com.android.settings/.Settings
    #开发者头条  io.manong.developerdaily/io.toutiao.android.ui.activity.MainActivity
    desired_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desired_caps['appActivity'] = '.Settings'

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明手机驱动对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(2)
    return driver
