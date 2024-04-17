# -*- coding: utf-8 -*-
# @file: class5_gevent.py
# @time: 2024 
# @user: Nemo
"""

协程：gevent
协程存在于线程之中，线程默认

spawn:开启协程
join:让线程等待协程执行
协程之间切换的条件：
    gevent.sleep()   耗时等待的情况下才会切换到别的协程

    gevent的程序补丁monkey :只要牵扯到耗时的操作，都能触发

#  首先考虑协程 》 线程 》进程


"""
import time

import gevent
import requests
from gevent import monkey
import queue
monkey.patch_all()


q = queue.Queue()
for i in range(1000):
    q.put('http://127.0.0.1:5000')

# def work1():
#     for i in range(10):
#         print('---work1---'.format(i))
#         time.sleep(0.1)
#
#
# def work2():
#     for i in range(10):
#         print('---work2---'.format(i))
#         time.sleep(0.1)

def work():
    while q.qsize()>0:
        url = q.get()
        time.sleep(0.01)


st = time.time()
g1 = gevent.spawn(work)
g2 = gevent.spawn(work)
g3 = gevent.spawn(work)
g4 = gevent.spawn(work)
g5 = gevent.spawn(work)

g1.join()
g2.join()
g3.join()
g4.join()
g5.join()
et = time.time()
print('时间', et-st)







