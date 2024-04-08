# -*- coding: utf-8 -*-
# @file: demo4.py
# @time: 2024 
# @user: Nemo


class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("Value must be non-negative")


# 创建实例
obj = MyClass()

# 访问属性
print(obj.value)  # 输出：0

# 修改属性值
obj.value = 10
print(obj.value)  # 输出：10

# 尝试设置负值
try:
    obj.value = -5
except ValueError as e:
    print(e)  # 输出：Value must be non-negative
