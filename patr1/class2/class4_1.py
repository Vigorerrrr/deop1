# -*- coding: utf-8 -*-
# @file: class4_1.py
# @time: 2024 
# @user: Nemo
"""

比较1000个任务
分别使用3个进程或线程来完成,那个更快
#进程快?
任务数量少于cup数量:并行
#线程:全局解释器锁GIL的存在,并发(不可能同时执行三个任务)


"""
import multiprocessing
import queue
import os
import threading
import time
from multiprocessing import Pool,Manager,Queue
import requests


# 线程的队列（只能在一个进程中使用）
# q = queue.Queue()
# for i in range(1000):
#     q.put('http://127.0.0.1:5000')

# # 进程间通信队列
# q2 = Queue()


# 进程池中的队列(给进程池中的各个进程之间通信使用)
# q3 = Manager().Queue()
# for i in range(10):
#     q3.put('http://127.0.0.1:5000')

# i = 0
# def work():
#     while q.qsize()>0:
#         # global i
#         url = q.get()
#         requests.get(url=url)
#         # i += 1
#         # print(i)
#
#
# def main():
#     st = time.time()
#     t1 = threading.Thread(target=work)
#     t2 = threading.Thread(target=work)
#     t3 = threading.Thread(target=work)
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#     et = time.time()
#     print('耗时{}'.format(et-st))
#
#
# if __name__ == '__main__':
#     main()
    # 线程耗时1.777

i= 0
def work(q):
    while q.qsize() > 0:
        try:
            url = q3.get_nowait()
        except:
            break
        else:
            url = q3.get()  # 获取数据
            requests.get(url=url)
            global i
            i += 1

            print("该进程运{}".format(i))


if __name__ == '__main__':
    st = time.time()
    q3 = Manager().Queue()
    for i in range(1000):
        q3.put('http://127.0.0.1:5000')

    pool = Pool(3)

    for i in range(q3.qsize()):
        pool.apply_async(work,args=(q3,))

    # 关闭进程池
    pool.close()
    # 主进程等待进程池中所有的进程执行结束之后往下执行
    pool.join()
    et = time.time()
    print('耗时{}'.format(et - st))

    # 进程耗时1.46



