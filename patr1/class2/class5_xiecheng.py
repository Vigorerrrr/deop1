# -*- coding: utf-8 -*-
# @file: class5_xiecheng.py
# @time: 2024 
# @user: Nemo
"""

五、协程
内容回顾
什么是生成器?
生成器怎么定义?
利用yield机制实现多任务?



"""


# def work1():
#     for i in range(10):
#         print('---work1---'.format(i))
#         yield
#
#
# def work2():
#     for i in range(10):
#         print('---work2---'.format(i))
#         yield
#
#
# # 通过生成器实现多任务
# g1 = work1()
# g2 = work2()
#
#
# while True:
#     try:
#         next(g1)
#         next(g2)
#     except StopIteration:
#         break

# 协程：微线程
"""


协程的本质上是单任务，
协程依赖于线程

协程相对与线程来讲占用的资源更少（几乎不要占用什么资源）




1、什么是协程?
协程是python个中另外一种实现多任务的方式,只不过比线程更小占用更小执行单元(理解为需要的资
源)。为啥说它是一个执行单元,因为它自带CPU上下文,这样只要在合适gr的时机,我们可以把一个协程
切换到另一个协程。只要这个过程中保存或恢复CPU上下文那么程序还是可以运行的。

通俗的理解:在一个线程中的某个函数,可以在任何地方保存存当前函数的一些临时变量等信息,然后切换到另
外一个函数中执行,注意不是通过调用函数的方式做到的,并且切换的次数以及什么时候再切换到原来的函数
都由开发者自己确定

2、协程和线程差异
在实现多任务时,线程切换从系统层面远不止保存和恢复CPU上下文这么简单。操作系统为了程序运行的高效
性每个线程都有自己缓存Cache等等数据,操作系统还会帮你做这些数据的恢复操作。所以线程的切换比较
耗性能,但是协程的切换只是单纯的操作CPU的上下文,所以一秒钟中切换个上百万次系统都抗的住,

3、greenlet
为了更好使用协程来完成多任务,python中的greenlet模块时其封装,从而使得切换任务变的更加简单



"""


from greenlet import greenlet


def work1():
    for i in range(10):
        print('---work1---'.format(i))
        g2.switch()


def work2():
    for i in range(10):
        print('---work2---'.format(i))
        g1.switch()


g1 = greenlet(work1)
g2 = greenlet(work2)

g1.switch()
g2.switch()



