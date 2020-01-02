# @File  : __init__.py
# @Author: yize365
# @Date  :  2019/12/29
# @Function:
# @Remarks:
import time
from selenium.webdriver.common.by import By
"""
closed_wlan参数
"""
#点击wlan
cli_wla=(By.XPATH,"//*[contains(@text,'WLA')]")
#点击关闭
cli_clo=(By.ID,"com.android.settings:id/switch_widget")

"""
long_show参数
"""
#设置--显示--休眠--30分钟
cli_xs=(By.XPATH,"//*[contains(@text,'显')]")
cli_xm=(By.XPATH,"//*[contains(@text,'休')]")
cli_thr=(By.XPATH,"//*[contains(@text,'30分')]")

"""
mes_set参数
"""
#点击新建信息
cli_new_msg=(By.ID, "com.android.mms:id/action_compose_new")
#输入接受者
input_pnum=(By.ID, "com.android.mms:id/recipients_editor")
#输入信息
input_mse_txt=(By.ID, "com.android.mms:id/embedded_text_editor")
#点击发送
cli_sent=(By.ID, "com.android.mms:id/send_button_sms")

"""
toutiao_login参数
"""
#点击我的
# //*[contains(@resource-id,
cli_my_tt=(By.XPATH, "//*[contains(@text,'我的')]")
#点击登录
cli_in_tt=(By.ID, "io.manong.developerdaily:id/login_btn")
#点击密码登录
clo_em_tt=(By.XPATH, "//*[@text='密码登录']")
#输入账号
input_em_tt=(By.ID, "io.manong.developerdaily:id/edt_phone")
#输入密码
inpwd_em_tt=(By.ID, "io.manong.developerdaily:id/edt_password")
#点击登录
cli_login_tt=(By.ID, "io.manong.developerdaily:id/btn_login")
"""
Search_Page参数
"""
search_btn_sp = (By.ID, "com.android.settings:id/search")
search_text_sp = (By.ID, "android:id/search_src_text")
search_return_sp = (By.CLASS_NAME, "android.widget.ImageButton")
