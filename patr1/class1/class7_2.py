# -*- coding: utf-8 -*-
# @file: class7_2.py
# @time: 2024 
# @user: Nemo


"""
字典在遍历的时候不能添加或者修改元素  pep 234


"""
dic={"a":11,"b":22}

data = dic.items()
print(list(data))
print(type(data))

for k,v in list(data):
    print(k)
    dic.pop(k)
    dic[k+'1'] =v
    # print(k,v)





