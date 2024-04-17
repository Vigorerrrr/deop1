"""
@Author:
@Filename:class6_1.py
@SoftWare: PyCharm

"""
import time
from threading import Thread
from multiprocessing import Process,Queue
import gevent
import requests


"""
10000 个请求，使用开启2个进程，进程中开启3线程，线程中开启5个协程来处理
"""

def green_work(q,gname):
    count = 0
    while not q.empty():
        url = q.get(timeout=0.01)
        requests.get(url)
        gevent.sleep(0.001)
        count += 1
    print('-------协程{}执行了{}个任务----------'.format(gname, count))


def thread_work(q,tname):

    g_list = []
    for i in range(5):
        gname = "{} - th - {}".format(tname, i)
        print('创建协程{}'.format(gname))
        g = gevent.spawn(green_work, q, gname)
        g_list.append(g)
    gevent.joinall(g_list)


def process_work(q,pname):
    """
    每个进程执行的任务函数, 在该进程中开启3个线程
    创建三个线程
    :paramq: 进程同通讯的任务队列
    :return:
    # print('{}该进程的任务为{}'.format(pname,tq.qsize())))
    # 创建三个进程,并执行
    """
    thread_list = []
    for i in range(3):
        tname = "{} - th - {}".format(pname,i)
        print('创建线程{}'.format(tname))
        t = Thread(target=thread_work, args=(q,tname))
        thread_list.append(t)
        t.start()
    # 让主线程堵塞,等待于线程
    for t in thread_list:
        t.join()


#计算时间的装饰器
def count_time(func):
#计算函数运行时间的装饰器""
    def wrapper(*args, **kwargs):
        print('开始执行')
        st = time.time()
        func(*args,**kwargs)
        et = time.time()
        print('执行结束')
        print('总耗时:{}'.format(et-st))
    return wrapper


#创建一个main函数来控制程序的运行
@count_time
def main():
    #创建10000个请求的队列
    q = Queue()
    for i in range(10000):
        q.put('http://127.0.0.1:5000')
    #开启两个进程处理
    print('队列创建完成,数量{}'.format(q.qsize()))
    pro_list = []
    for i in range(2):
        pname ='pro-{}'.format(i)
        print('创建进程{}'.format(pname))
        p = Process(target=process_work, args=(q,pname))
        p.start()
        pro_list.append(p)

    for p in pro_list:
        p.join()


if __name__ == '__main__':
    main()


"""
https://www.jb51.net/python/293454lnx.htm

"""