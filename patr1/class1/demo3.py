# -*- coding: utf-8 -*-
# @file: demo3.py
# @time: 2024 
# @user: Nemo

# def make_bold(func):
#     def wrapper(text):
#         return "<b>" + func(text)+'23' + "</b>"
#     return wrapper
#
#
# @make_bold
# def greet(name):
#     return f"Hello, {name}!"
#
#
# print(greet("World"))  # 输出：<b>Hello, World!</b>


class MyTest(object):
    @classmethod
    def add(cls):  # cls 代表类本身
        print('add')
        print(cls)

    def sub(self):  # self 代表实例本身
        print('sub',self)


t = MyTest()
t.add()
t.sub()
"""
结果
add
<class '__main__.MyTest'>    类
sub <__main__.MyTest object at 0x000002082E61E990>  实例对象

"""
