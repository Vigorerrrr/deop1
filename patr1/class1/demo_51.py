# -*- coding: utf-8 -*-
# @file: demo_51.py
# @time: 2024 
# @user: Nemo
import threading


class ToolUtilV3(object):
    _lock = threading.RLock()  # 加锁，提供线程安全
    _instance = None

    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name

    def __new__(cls, *args, **kwargs):
        # 创建类对象时不需要args和kwargs参数
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__new__(cls)
        return cls._instance


tool1 = ToolUtilV3("工具集1")
print(id(tool1), tool1.name)

tool2 = ToolUtilV3("工具集2")
print(id(tool2), tool2.name)

tool3 = ToolUtilV3("工具集3")
print(id(tool3), tool3.name)


