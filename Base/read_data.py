# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 17:52
# @Author  : yize365
# @Email   : 1558570566@qq.com
# @File    : read_data.py.py
# @Software: PyCharm
import yaml
import os
class Read_Data:
    def __init__(self, file_name):
        '''
            使用pytest运行在项目的根目录下运行，即App_Project目录
            期望路径为：项目所在目录/App_Project/Data/file_name
        '''
        #os.getcwd() ==> D:\pytest_appium\Base
        #路径=获取当前路径+
        # 注意这里填写的下面的路径方法存在问题,会导致程序报错,无法运行
        # self.file_path = os.path.abspath(os.path.dirname(os.getcwd())) + os.sep + "Data" + os.sep + file_name
        self.file_path = "D:\pytest_appium\Data"+ os.sep + file_name
        # print(self.file_path)
    def ret_yaml_data(self):
        with open(self.file_path, 'r',encoding='utf-8') as f:
            data = yaml.load(f)  # 读取文件内容
            return data


# aaa=Read_Data("search_data.yml").ret_yaml_data().get("Search_Data")
# print(aaa)