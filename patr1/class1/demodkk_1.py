# -*- coding: utf-8 -*-
# @file: demodkk_1.py
# @time: 2024 
# @user: Nemo
# class MyClass:
#     def __init__(self):
#         self.x = 10  # 初始化一个属性
#
#     def __getattr__(self, name):
#         # 当访问不存在的属性时，会触发该方法
#         print(f"Accessing attribute {name} which does not exist")
#         # 返回一个默认值
#         return "default"
#
# # 创建一个 MyClass 对象
# obj = MyClass()
#
# # 访问已存在的属性
# print(obj.x)  # 输出：10
#
# # 访问不存在的属性
# print(obj.y)  # 输出：Accessing attribute y which does not exist
#               #      default


class MyClass:
    def __init__(self):
        self.x = 10

    def __getattribute__(self, name):
        print(f"__getattribute__ is called for {name}")
        # 尝试获取属性，如果失败，则引发 AttributeError
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            # 如果无法获取属性，则继续执行 __getattr__
            return self.__getattr__(name)

    def __getattr__(self, name):
        print(f"__getattr__ is called for {name}")
        return "default"

# 创建一个 MyClass 对象
obj = MyClass()

# 访问已存在的属性
print(obj.x)  # 输出：__getattribute__ is called for x
              #      10
print('-------------------------------------------------------------------')
# 访问不存在的属性
print(obj.y)  # 输出：__getattribute__ is called for y
              #      __getattr__ is called for y
              #      default
