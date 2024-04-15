# -*- coding: utf-8 -*-
# @file: class7_1.py
# @time: 2024 
# @user: Nemo

class BaseFiled(object):
    """
    字段的父类

    """
    pass


class CharFiled(BaseFiled):

    def __init__(self,max_length=20):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value,str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError('字符串长度超{}'.format(self.max_length))
        else:
            raise TypeError('need str')

    def __delete__(self, instance):
        self.value = None


class IntFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value,int):
            self.value = value
        else:
            raise TypeError('need a int')

    def __delete__(self, instance):
        self.value = None


class BoolFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value,bool):
            self.value = value
        else:
            raise ValueError

    def __delete__(self, instance):
        self.value = None

