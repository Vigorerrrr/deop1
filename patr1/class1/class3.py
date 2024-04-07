# -*- coding: utf-8 -*-
# @file: class3.py
# @time: 2024 
# @user: Nemo
"""
函数
"""
"""
一、递归函数
问题一:函数内部可以调用自身这个函数吗?

递归函数:在函数中调用函数自身,我们把这样的函数叫做递归函拍数

递归边界:退出递归的终止条件

案列需求一:通过递归函数实现的任意数的阶乘通过递归函数实现的任意数的阶乘
def jie_func(n):
#判断n是否等于1,如果等于则返回1,
    if n==1:
        return n
    else:
        #不等于则继续调用自身函数进行判断
        return n * jie_func(n - 1)
        
res = jie_func(5)

递归函数一定要写终止条件


二、纯函数
2.1、纯函数的概念
简单来说,一个函数的返回结果只依赖于它的参数,并且在执行过程里面没有副作用,我们就把这个函数叫做纯函
数。

2.2、纯函数的3个原则
变量都只在函数作用域内获取,作为的函数的参数传入
不会产生副作用(side effects),不会改变被传入的数据或者其他数据(全局变量)
相同的输入保证相同的输

2.3、函数的副作用
副作用是指函数被调用,完成了函数既定的计算任务,但同时因为访问了外部数据,尤其是因为对外部数据进
行了写操作,从而一定程度地改变了系统环境


2.2、python中的内置函数
内置函数都是纯函数

内置函数:https://docs.python.org/zh-cn/3.7/library/functions.html
常用的内置函数
map函数:会根据提供的函数对指定序列做映射。 map(function, iterable1, iterable2, ...)
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

filter函数:函数用于过滤序列. filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

zip函数:函数用于将可选代的对象作为参数,将对象中对应的元素打包成一个个元组 zip(iterable1, iterable2, ...)
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)

for item in zipped:
    print(item)

三、匿名函数
python中有一种特殊的函数,不需要使用def去事定义,也不用给勇数起名字,用过lamda表达来定义,这种函
数叫匿名函数

匿名函数格式
lambda参数:表达式(返回值)
问题需求:将以下函数改成匿名函数
#普通函数
def funl(varl):
    return var1 * 2
#匿名函数写法
lambda var1 : var1 * 2

匿名函数使用的场景，只有一个表达式



四、偏函数
问题一:什么是偏函数?
在Python的内置模块functools提供了很多有用的功能,其中一个就是偏函数(partial)

问题二:偏函数有什么用?
当函数的参数个数太多,需要简化时,使用functools.partial可以创建一个新的函数,这个新函数可以固定住
原函数的部分参数,从而在调用时更简单。

偏函数应用案列
在我们之前学到的内置函数中filter中,调用的时候需要传入两个参数,第一个是函数,第二个是我们需要过滤的可选
代类型的数据,
from functools import partial

# 定义一个简单的函数
def power(base, exponent):
    return base ** exponent

# 创建一个偏函数，固定 base 参数为2
square = partial(power, 2)

# 调用偏函数，只需传入 exponent 参数
result = square(3)
print(result)  # 输出：8，因为2的立方是8


partial(filter,lambda x:x>5)




通过递归函数实现斐波那契数列
一:实现斐波那契数列数列,输入一个数列的位置数,返回斐波那契教列相应位置的值
皮波那契数列【1,2,3,5,8,13,21,34......],第一个数是1,后面的数等于前两个数相力的结束

二、古典问题:第三个月起每个月都生一对兔子,小兔子长到第三个月后每个月又生一对兔子,假如免子都不死,问每个月
的兔子总数为多少?(意味着生长期为2

三、小明有100元钱打算买100本书,A类书籍5元一本,B类书籍3元一本C类书籍1元两本,请用程序算出小明一共够多
少种买法?(面试笔试题)


"""

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# ss = fibonacci(5)
# print(ss)

# 定义一个将输入参数加倍的 Lambda 函数
double = lambda x: x * 2

# 使用 Lambda 函数
result = double(5)
print(result)  # 输出结果为 10

"""
lambda 使用场景

"""
li = [1, 2, 122, 331, 11, 22, 33, 4, 6, 7, 2, 88, 7, 2, 88, 31]
res2 = filter(lambda x: x < 10, li)
print(list(res2))


"""

12
"""