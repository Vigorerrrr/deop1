# -*- coding: utf-8 -*-
# @file: class2.py
# @time: 2024 
# @user: Nemo
"""
垃圾回收是一种自动管理计算机程序中内存的机制，目的是识别并释放不再被程序使用的内存，以便程序能够继续有效地使用内存。在Python中，垃圾回收由解释器自动处理，不需要程序员手动管理。

Python中的垃圾回收主要依靠引用计数和循环引用检测来实现。

1. **引用计数**：Python中的每个对象都会维护一个引用计数，表示指向该对象的引用数量。当引用计数为0时，说明没有任何引用指向该对象，该对象就可以被销毁。Python通过增加和减少引用计数来管理内存。

2. **循环引用检测**：有时候两个或多个对象之间存在循环引用，即彼此引用对方，导致它们的引用计数永远不会变为0。为了解决这个问题，Python引入了循环引用检测机制。通过检测和处理循环引用，Python可以正确地释放循环引用对象所占用的内存。

除了引用计数和循环引用检测外，Python还使用了一种称为"分代回收"的策略来提高垃圾回收的效率。分代回收将对象分为不同的代，每个代对应不同的对象存活时间。通常情况下，新创建的对象会被放入年轻代，经过几次垃圾回收后仍然存活的对象会被移到老年代。由于大部分对象的生命周期很短，因此年轻代的垃圾回收频率比老年代高，这样可以提高垃圾回收的效率。

总的来说，Python的垃圾回收机制通过引用计数、循环引用检测和分代回收等方式来管理内存，使得程序员可以更加方便地进行内存管理，避免内存泄漏和其他与内存相关的问题。

"""
import queue
import random
import threading
import time
from multiprocessing import Process

import requests

"""
Python的垃圾回收机制是一种自动管理内存的机制，旨在识别和清理不再被程序使用的内存，从而释放资源并减少内存泄漏的可能性。Python的垃圾回收主要依赖于两种策略：

1. **引用计数**：Python中的每个对象都有一个引用计数，用于跟踪有多少引用指向该对象。当引用计数变为零时，意味着没有任何引用指向该对象，Python会将其标记为可回收，并在适当的时候将其释放。引用计数的优点是简单高效，但它无法处理循环引用的情况。

2. **循环垃圾收集**：Python的垃圾回收器也包含一个循环垃圾收集器，用于处理循环引用的情况。循环引用是指两个或多个对象之间形成的环状引用关系，导致它们的引用计数永远不会降为零。Python的垃圾回收器通过检测和清理这种循环引用，来释放这些对象占用的内存。

Python的垃圾回收器使用了分代收集的策略，将对象分为不同的代，每个代拥有不同的存活周期。新创建的对象被放入年轻代，而经过多次垃圾回收仍然存活的对象则会被提升到下一个代。这种分代收集策略可以提高垃圾回收的效率，因为大部分对象的生命周期较短，而只有少数对象会存活较长时间。

总体来说，Python的垃圾回收机制通过引用计数、循环垃圾收集和分代收集等策略来管理内存，从而确保程序能够高效地使用内存资源，减少内存泄漏的可能性。

"""

"""
python进阶(五):并发和性能
一、并发和并行
1、多任务
cup与多任务的天系:
单核CPU可不可以执行多任务?
也可以执行多任务,由于CPU执行代码都是顺序执行的,那么,单核CPU是怎么执行多任务的呢?答案就
是操作系统轮流让各个任务交替执行,任务1执行0.01秒,切换到任务2,任务2执行0.01秒,再切换到任
务3,执行0.01秒......这样反复执行下去,表面上看,每个任务都是交替执行的,但是,由于CPU的执行
速度实在是太快了,我们感觉就像所有任务都在同时执行一样。
真正的并行执行多任务只能在多核CPU上实现,但是,由于任务数量远远多于CPU的核心数量,所以,操作系
统也会自动把很多任务轮流调度到每个核心上执行。


2、并发和并行:
并发:指的是任务数多余cpu核数,通过操作系统的各种任务调度算法,实现用多个任务"一起"执行(实际上
总有一些任务不在执行,因为切换任务的速度相当快,看上去一起执行而已
并行:指的是任务数小于等于cpu核数,即任务真的是一起执行的


总结
真正的并行执行多任务只能在多核CPU上实现,但是,由于任务数量远远多于CPU的核心数量,所以,操
作系统也会自动把很多任务轮流调度到每个核心上执行。

并发:指的是任务数多余cpu核数,通过操作系统的各种任务调度算法,实现用多个任务"一起"执行(实
际上总有一些任务不在执行,因为切换任务的速度相当快,看上去一起执行而已
并行:指的是任务数小于等于cpu核数,即任务真的是一起执行的


"""

"""
进程 线程 协程


threading 模块
创建线程:threading.Thread(target=func)

Thread类提供了以下方法:
run()       用以表示线程活动的方法
start()     启动线程活动
join([time])        设置主线程会等待time秒后再往下执行,time默认为子线程结束,多个子线程之间设置的值会叠加
isAlive()       返回线程是否活动的
getName()       返回线程名
setName()       设置线程名。



"""
# import threading
# import time
#
#
# # 定义一个函数，作为线程要执行的任务
# def task(name, delay):
#     print(f"Thread {name} is starting...")
#     time.sleep(delay)  # 模拟任务执行时间
#     print(f"Thread {name} is done.")
#
#
# # 创建线程对象，并传入要执行的任务
# thread1 = threading.Thread(target=task, args=("Thread 1", 2))  # 任务名为Thread 1，延迟2秒执行
# thread2 = threading.Thread(target=task, args=("Thread 2", 3))  # 任务名为Thread 2，延迟3秒执行
#
# # 启动线程
# thread1.start()
# print('\n',thread1.name)
# thread2.start()
#
# # 主线程等待所有子线程执行完成
# thread1.join()
# thread2.join()
#
# print("All threads are done.")
#
#
#
"""
class RequestThread(threading.Thread):
    # 发送requests请求

    def __init__(self, url):
        self.url = url
        super().__init__()

    def run(self):
        for i in range(10):
            res = requests.get(self.url)
            print('线程:{}--返回的状态码-{}--'.format(threading.current_thread(), res.status_code))


# 创建五个线程,发起请求
s_time = time.time()
for i in range(5):
    t = RequestThread(url='www.dd.com')
    t.start()
e_time=time.time()
print('耗时:',e_time-s_time)

传参数则需要重写_init_方法(注意重写之后要调用父类)的init方法)


"""


"""
3、多线程-共享全局变量
多线程之间修改全局变量
线程之间是共用同一块内存的,那么线程可以共享全局变量
案例:当前有一个全局变量a=100,再线程a中修改,线程b中是否会生效,
列表当做实参传递到线程中,线程中修改会有说明影响

总结
在一个进程内的所有线程共享全局变量,很方便在多个线程间共享数据
缺点就是,线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱(即线程非安全)


#多线程全局变量的问题
#全局变量
a = 100


def func1():
    global a
    for i in range(200000000):
        meta.acquire()
        a += 1
        meta.release()
    print('线程1修改完',a)


def func2():
    global a
    for i in range(200000000):
        meta.acquire()
        a += 1
        meta.release()
    print('线程2修改完',a)


t1 = threading.Thread(target=func1)

t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()

print(a)

"""



"""
同步
同步就是协同步调,按预定的先后次序进行运行。"同"字从字面上容易理解为一起动作,其实不
是,"同"字应是指协同、协助、互相配合,如进程、线程同步,可理解为进程或线程A和B一块配合,A执
行到一定程度时要依靠B的某个结果,于是停下来,示意B运行;B执行再将结果给A:A再继续操作。


·互斥锁
线程同步能够保证多个线程安全访问竞争资源,最简单的同步机制是引入互斥锁。
。互斥锁为资源引入一个状态:锁定/非锁定。
。某个线程要更改共享数据时,先将其锁定,此时资源的状态为"锁定",其他线程不能更改直到该线程释放
资源,将资源的状态变成"非锁定",其他的线程才能再次锁定该资源
。互斥锁保证了每次只有一个线程进行写入操作,从而保证了多线程情况下数据的正确性
threading模块中定义了Lock类,可以方便的处理锁定:


meta = threading.Lock()





a = 100


def func1():
    global a
    for i in range(20000000):
        meta.acquire()
        a += 1
        meta.release()
    print('线程1修改完',a)


def func2():
    global a
    for i in range(20000000):
        meta.acquire()
        a += 1
        meta.release()
    print('线程2修改完',a)


meta = threading.Lock()
t1 = threading.Thread(target=func1)

t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()

print(a)


"""

"""
GIL讨论题如下
描述PythonGIL的概念,以及它对python多线程的影响?
Guido的声明:http://www.artima.com/forums/flat.jsp?foruim=106&thread=214235
参考答案:
I
1.Python语言和GIL没有半毛钱关系。仅仅是由于历史原因在Cpython虚拟机(解释器),难以移除GIL。

2.GIL:全局解释器锁,每个线程在执行的过程都需要先获取GIL,保证同一时刻只有一个线程可以执行代码.

3.线程释放GIL锁的情况:在IO操作等可能会引起阻塞的systemcall之前,可以暂时释放GIL,但在执行完毕
后,必须重新获取GILPython3.x使用计时器(执行时间达到间值后后,当前线程释放GIL)或Python2.x,tickets计数达到100

4.Python使用多进程是可以利用多核的CPU资源的。




7、GIL全局解释器锁(扩展)
·问题一:python单线程和多线程分别来完成工作,到底哪个快??

io密集型:涉及到网络、磁盘10的任务都是IO密集型任务,这类任务的特点是CPU消耗很少,任务的大部
分时间都在等待IO操作完成(因为IO的速度远低于CPU和内存的速度)

cup密集型:cup密集型也称为计算密集型,任务的特点是要进行2大量的计算,消耗CPU资源,比如计算
圆周率、对视频进行高清解码等等,全靠CPU的运算能力




"""
"""
三、队列
Python的Queue模块中提供了同步的、线程安全的队列类,包括:FIRFO(先入先出)队列 Queue LIFO(后
入先出)队列LifoQueue,优先级队列PriorityQueue,这些队列都实现了锁原语,能够在多线程中直接使
用,可以使用队列来实现线程间的同步。
初始化Queue()对象时(例如:q=Queue()),若括号中没有指定最大可接收的消息数量,或数量为负值,
那么就代表可接受的消息数量没有上限
队列的方法:
def task_done(self):...
def join(self):...
def qsize(self):...
def empty(self):...
def full(self):..
def put(self, item,block=True,timeout=None):...
def get(self,block=True,timeout=None):...
def put_nowait(self,item):...
def get_nowait(self):..


Queue.qsize():返回当前队列包含的消息数量;
Queue.empty()如果队列为空,返回True,反之False
Queue.full()如果队列里队列满了,返回True反之False
Queue.full()获取队列,timeout等待时间
    如果block表示是否等待,如果timeout表示等待时间,
    get(self,block=True,timeout=None)
Queue.put(item)写入队列
    #如果block表示是否等待,如果timeout表示等待时间,
    put(self,item,block=True,timeout=None)
Queueue.get_nowait()相当Queue.get(False)
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done()在完成一项工作之后,使用Queue.task_done()方法可以向队列发送一个信号,表
示该任务执行完毕

Queue.join()实际上意味着等到队列中所有的任务(数据)执行完毕之后,再往下,否则一直等待
    注意点:join()是判断的依据,不单指的是队列中没有数据,数据get出去之后,要使用
    task_done()向队列发送一个信号,表示该任务执行(数据使用)完毕,





"""


"""
先入先出
q = queue.Queue(3)
q.put(1)
q.put(11)
q.put(111)

print(q.get())
print(q.get())



import threading
import time
import random


# 生产者类
class Producer(threading.Thread):
    def __init__(self, q):

        self.queue = q
        super().__init__()

    def run(self):
        while True:
            
            item = random.randint(0, 100)  # 生产一个随机数
            self.queue.put(item)  # 将产品放入队列

            print(f'生产者生产了 {item}')
            time.sleep(random.random())  # 模拟生产耗时


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()  # 从队列中取出产品
            if item is None:
                break  # 如果取出的是None，表示队列已空，线程结束
            print(f'消费者消费了 {item}')
            time.sleep(random.random())  # 模拟消费耗时
            self.queue.task_done()  # 通知队列任务完成


# 主函数
def main():
    q = queue.Queue()  # 创建一个队列

    # 创建生产者线程和消费者线程
    producer = Producer(q)
    consumer = Consumer(q)

    # 启动线程
    producer.start()
    consumer.start()

    # 主线程等待消费者线程结束
    consumer.join()

    # 当消费者线程结束时，发送None信号给生产者线程，使其也结束
    q.put(None)
    producer.join()


if __name__ == '__main__':
    main()

"""

"""

q = queue.Queue()

class Producer(threading.Thread):
    def run(self):
    # 判断队列中的商品数是否少于50,少于50了之后就生产200个
        count=0
        while True:
            if q.qsize()<50:
                for i in range(200):
                    count +=1
                    goods='--第{}个商品---'.format(count)
                    q.put(goods)
                    print("生产:",goods)
            time.sleep(1)



class Consumer(threading.Thread):

    def run(self):
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    print('消费:{}'.format(q.get()))
            time.sleep(0.1)



p = Producer()
p.start()
for i in range(5):
    c = Consumer()
    c.start()

"""
"""

import threading
import queue
import time
import random

# 共享队列
shared_queue = queue.Queue()
# 控制生产者和消费者的运行状态
running = True
# 互斥锁，用于保护共享资源
lock = threading.Lock()

# 生产者线程函数
def producer():
    global running
    while running:
        # 随机生成数据
        data = random.randint(1, 100)
        with lock:
            # 将数据放入队列
            shared_queue.put(data)
            print("Produced:", data)
        time.sleep(random.random())  # 模拟生产过程中的耗时操作

# 消费者线程函数
def consumer():
    global running
    while running:
        with lock:
            if not shared_queue.empty():
                # 从队列中获取数据
                data = shared_queue.get()
                print("Consumed:", data)
        time.sleep(random.random())  # 模拟消费过程中的耗时操作

# 创建生产者线程和消费者线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待一段时间后停止生产者和消费者
time.sleep(10)
running = False

# 等待线程结束
producer_thread.join()
consumer_thread.join()

print("Producer and Consumer stopped.")

"""

"""
四、进程
1、进程介绍
·进程什么是进程
。程序:例如xxx.py这是程序,是一个静态的
。进程:一个程序运行起来后,代码+用到的资源称之为进程,它是操作系统分配资源的基本单元。
。不仅可以通过线程完成多任务,进程也是可以的

进程的状态
工作中,任务数往往大于cpu的核数,即一定有一些任务正在执行,而另外一些任务在等待cpu进行执
行,因此导致了有了不同的状态
就绪状态:运行的条件都已经满足了,正在等在cpu执行
执行状态:cpu正在执行其功能
等待状态:等待某些条件满足,例如一个程序sleep了,此时就处于等待态

2、进程、线程对比

功能
    进程,能够完成多任务,比如在一台电脑上能够同时运行多个软伙伴
    线程,能够完成多任务,比如一个QQ中的多个聊天窗口
    
定义的不同

    进程是系统进行资源分配和调度的一个独立单位
    
    线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己
    基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和找),但是它可与
    同属一个进程的其他的线程共享进程所拥有的全部资源.
    
区别
    。一个程序至少有一个进程,一个进程至少有一个线程
    。线程的划分尺度小于进程(资源比进程少),使得多线程程序的井>发性高。
    。进程在执行过程中拥有独立的内存单元,而多个线程共享内存,从而极大地提高了程序的运行效率
    。线程不能够独立执行,必须依存在进程中
    。可以将进程理解为工厂中的一条流水线,而其中的线程就是这个流水线上的工人


优缺点
线程和进程在使用上各有优点：线程执行开销小，但不利于资源的管理和保护，而进程正相反



3、multiprocessing模块
Process([group [, target [, name [, args]]]]]]]]]])
    target:如果传递了函数的引用,可以任务这个子进程就执行这里的代码
    args:给target指定的函数传递的参数,以元组的方式传递
    kwargs:给target指定的函数传递命名参数
    name:给进程设定一个名字,可以不设定
    group:指定进程组,大多数情况下用不到

Process创建的实例对象的常用方法:
    start():启动子进程实例(创建子进程)
    is_alive():判断进程子进程是否还在活着
    join((timeout)):是否等待子进程执行结束,或等待多少秒
    terminate():不管任务是否完成,立即终止子进程
    
Process创建的实例对象的常用属性:
    name:当前进程的别名,默认为Process-N,N为从1开始递增的整数
    pid:当前进程的pid(进程号)


"""

a_num = 100


def work1():
    for i in range(10):
        global a_num
        print('1111--------{}'.format(a_num))
        a_num += 1
        time.sleep(1)


def work2():
    for i in range(10):
        global a_num
        print('2222',a_num)
        a_num += 1
        time.sleep(1)


if __name__ == '__main__':

    p1 = Process(target=work1)
    p2 = Process(target=work2)


    p1.start()
    p2.start()

"""
进程执行的时候，不加if __name__ == '__main__': 为什么会报错？

多进程不共享全局变量
 
 
 
"""
