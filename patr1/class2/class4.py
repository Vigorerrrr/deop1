# -*- coding: utf-8 -*-
# @file: class4.py
# @time: 2024 
# @user: Nemo



"""
进程池

"""
import multiprocessing
import os
import time

import requests

"""
5、进程池Pool
当需要创建的子进程数量不多时,可以直接利用multiprocessing中的Process动态成生多个进程,但如果是
上百甚至上千个目标,手动的去创建进程的工作量巨大,此时就可以用到multiprocessing模块提供的Pool
方法。

初始化Pool时,可以指定一个最大进程数,当有新的请求提交到Pool中时,如果池还没有满,那么就会创建
一个新的进程用来执行该请求;但如果池中的进程数已经达到指定的最大值,那么该请求就会等待,直到池中
有进程结束,才会用之前的进程来执行新的任务,请看下面的实例:

Pool常用方法:
    apply_async(func[,args[,kwds]):使用非阻塞方式调用func(并行执行,堵塞方式必须等待上一个
    进程退出才能执行下一个进程),args为传递给func的参数列表,kwds为传递给func的关键字参数列
    表;
    
    close():关闭Pool,使其不再接受新的任务;
    
    terminate():不管任务是否完成,立即终止;
    
    join():主进程阻塞,等待子进程的退出,必须在close或terminate之后使用;


#-*- coding:utf-8-*-
from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg.os.getpid()))
    #random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f"%(t_stop-t_start))
po = Pool(3)
for i in range(0,10)
    po.apply_async(worker,(i,))


进程池 
进程池的队列是:q = Manager().Queue()



"""
from multiprocessing import Pool,Manager

a = 0


def work(q):
    global a
    url = q.get()
    requests.get(url)
    time.sleep(1)
    print('work1正在执行任务{}'.format(os.getpid()), a)
    a += 1


if __name__ == '__main__':
    # 进程池之间通信队列
    q = Manager().Queue()
    for i in range(100):
        q.put('https://www.cnblogs.com/xachary/p/18139413')

    pool = multiprocessing.Pool(processes=5)

    while True:
        if q.qsize()>0:
            pool.apply_async(func=work,args=(q,))
        else:
            break

    pool.close()
    pool.join()















