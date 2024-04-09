# -*- coding: utf-8 -*-
# @file: demo5.py
# @time: 2024 
# @user: Nemo

# 通过类实现装饰器call方法
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


@Decorator
def my_function():
    print("Inside the function")


# 调用被装饰的函数
my_function()











