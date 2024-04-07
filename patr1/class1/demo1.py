# -*- coding: utf-8 -*-
# @file: demo1.py
# @time: 2024 
# @user: Nemo
# a = []
# for i in range(100000000):
#     temp = ['你好'] * 2000
#     a.append(temp)
#
# for ele in a:
#     continue
import time


def get_list_element():
    for i in range(8400000):
        temp = ['你好'] * 2000
        yield temp


if __name__ == '__main__':
    a = get_list_element()
    t1 = time.time()
    for ele in a:
        print(ele)
        continue

    t2= time.time()
    print(t2,t1)
