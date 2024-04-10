# -*- coding: utf-8 -*-
# @file: demo_771.py
# @time: 2024 
# @user: Nemo
# from demo_770 import singleton

#
#
# print(singleton)


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在被装饰的函数执行前的逻辑
        print("Before function execution")

        # 调用被装饰的函数
        result = self.func(*args, **kwargs)

        # 在被装饰的函数执行后的逻辑
        print("After function execution")

        return result

# 使用装饰器类


@Decorator
def my_function():

    print("Inside the function")
    return 2 + 3
    # return "hello"


dd = my_function() # 调用被装饰的函数


print(dd)

