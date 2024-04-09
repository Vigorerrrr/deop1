# -*- coding: utf-8 -*-
# @file: demo_5.py
# @time: 2024 
# @user: Nemo
class ToolUtil(object):
    _instance = None  # 类属性，保存类实例

    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name

    def __new__(cls, *args, **kwargs):
        # 创建类对象时不需要args和kwargs参数
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

tool1 = ToolUtil("工具集1")

print(id(tool1), tool1.name)

tool2 = ToolUtil("工具集2")
print(id(tool2), tool2.name)

tool3 = ToolUtil("工具集3")
print(id(tool3), tool3.name)
