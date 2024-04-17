"""
@Author:
@Filename:class3.py
@SoftWare: PyCharm

"""
import multiprocessing
from multiprocessing import Process,Queue

import requests

"""
多进程间的通讯

4、进程间通信-Queue
Pythonmultiprocessing.Queue()和queue.Queue 区别
    queue.Queue是进程内非阻塞队列。 （进程内是线程，线程间通信队列）
    multiprocess.Queue是跨进程通信队列。
    多进程前者是各自私有,后者是各子进程共有。
    Process之间有时需要通信,操作系统提供了很多机制来实现进程间的通信。
    
1.进程中Queue的使用
可以使用multiprocessing模块的Queue实现多进程之间的数据传递,Quleue本身是一个消息列队程序,首
先用一个小实例来演示一下Queue的工作原理:在父进程中则建两个子进程,一个往Queue里写数据,一个
从Queue里读数据:

注意点进程之间的queue要当做参数传进去(不共享全局变量)。


"""

# from queue import Queue
import time


# q = Queue()

a = 0


def work1(q):
    while q.qsize()>0:
        global a
        url = q.get()
        requests.get(url)
        print('work1正在执行任务',a)
        a += 1


def work2(q):
    while q.qsize()>0:
        global a
        url = q.get()
        requests.get(url)
        print('work2正在执行任务',a)
        a += 1


if __name__ == '__main__':
    q = multiprocessing.Queue()
    for i in range(10):
        q.put('https://www.cnblogs.com/xachary/p/18139413')
    p1 = Process(target=work1,args=(q,))
    p2 = Process(target=work2,args=(q,))


    p1.start()
    p2.start()
 
