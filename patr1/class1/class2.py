# -*- coding: utf-8 -*-
# @file: class2.py
# @time: 2024 
# @user: Nemo
"""
python 进阶 --数据类型

>一,元组和列表
>二,字典和集合的原理和应用
>三、推到式
>四、选代器和生成器


"""
# import timeit
# from collections import namedtuple
#
# code_too = """
# lo = list[1,2,3]
# """
# print(timeit.timeit(stmt=code_too))
# code_to = """
# int_tuple = (1,2,3)
# """
# print(timeit.timeit(stmt=code_to))

"""
创建一个元组的 
本机电脑环境，元组运行速度比列表快7倍
实际使用列表比元组情况多，列表灵活，可随意增删改数据
固定的数据可以元组存储      n 

"""
"""
命名元组
导包
from collections import namedtuple


"""
# student_info = namedtuple('info_tuple',['name','age','gender'])
# tu = student_info(1,2,3)
# print(tu)
# tutu = student_info('san',18,'nan')
# print(tutu)
#
# print(tutu.name)
# print(type(tutu))
# print(type(student_info))


"""
二,字典和集合的原理和应用
dict与set实现原理是一样的,都是将实际的值放到list中,唯一不同的在于hash函数操作的对象,对于dict,hash
函数操作的是其key,而对于set是直接操作的它的元素,假设操作内容容为x,其作为因变量,放入hash函数,通过
运算后取list的余数,转化为一个list的下标,此下标位置对于set而言用来放其本身,而对于dict则是创建了两个
list,一个list该下表放此key,另一个list中该下标方对应的value。其中中,我们把实现set的方式叫做Hash Set,实
现dict的方式叫做Hash"Map/Table注:map指的就是通过key来寻找value的过程

字典在3.7之前都是无序的，3.7之后按添加的顺序存储，是有序的


数值：
序列：字符串 列表 元组
散列：字典 集合 特征：内部元素是无序的



"""

"""
三、推到式
1、列表推到式
需求:如何快速生成一个0-100的列表?
方式一:通过之前学过的循环来做
#while循环
listl = []
i = 0
whilei<100:
    list1.append(i)
    1+=1
print('listl的值为:',listl)

#for循环
1ist2=[]
for i in range(100):
    list2.append(i)
print('list2的值为:",list2)


更简单的方式:列表推倒式
list3=[i for i in range(10)]
print('list3的值为:",list3)

带条件的推导式
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  
# 输出: [2, 4]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)  
# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]        



#宁典推导式
dic1 = {i:i+1 for i in range(10)}
print(dic1)


"""
# list3 = [i for i in range(10)]
# print("list3的值为:",list3)
#
# dic1 = {i:i+1 for i in range(10)}
# print(dic1)
"""
#使用字典推倒是将下面字符串格式的数据,改成字典类型的数据
cook_str="BIDUPSID=D0727533D7147B7 :PSTM=1530348042:BAIDUID=B1005C9BC2EB28"
#使用字典推到式解决
cook_dict = {item.split('=')[0]:item.split('=')[1] for item in cook_str.split(':')}
print(cook_dict)

"""
"""
生成器表达式

tuu = (i for i in range(10))
print(tuu)
-------------------------
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
for value in gen:
    print(value)
---------------------------



"""
# tuu1 = (i for i in range(10))
# print(next(tuu1))
# print(next(tuu1))
#
#
# def get_fun():
#     yield 100
#     print("hail")
#     yield 1000
#
# res = get_fun()
#
# print(next(res))
# print(next(res))


"""
1、迭代协议
1.1、选代协议:一种是包含iter方法的,另一种是包含getitem方法的(比如str对象就没有iter方法,但是
一样能够迭代),只要对象中包含了这两种方法的任意一种,那么这个对象就可以进行迭代操作,也就是实现了选
代协议。
1.2、选代器协议:
:实现了选代器协议的对象(实现方式:对象内部定义了一个iter()方法)
·对象实现了_next__方法
_next_方法返回了某个数值(当然一般情况下,我们需要的是返回这个对象的特定的数字,并且按照一定
的顺序进行依次返回
_next_方法需要在值取完的时候,抛出Stopiteration的错误信息。
1.3.可选代对象:只要内部实现了选代协议的就是一个可选代对象(可迭代对象可以进行相关的迭代操作,比如
for循环,map函数等等)
所有的迭代器都是是可选代对象



"""

"""
迭代器（iterator）和可迭代对象（iterable）是 Python 中用于支持迭代的两个重要概念，它们之间有着密切的关系。理解它们之间的关系对于正确地使用迭代在 Python 中非常重要。

可迭代对象（Iterable）：
可迭代对象是指可以返回一个迭代器的对象。在 Python 中，包括但不限于以下对象都属于可迭代对象：

列表（List）
元组（Tuple）
字符串（String）
字典（Dictionary）
集合（Set）
生成器（Generator）等
当你使用for循环来遍历上述对象中的元素时，实际上是通过获取这些对象的迭代器来实现的。这就是因为这些对象本身是可迭代的。

迭代器（Iterator）：
迭代器是可迭代对象背后的工具，它负责追踪可迭代对象中所处位置，并能够返回当前位置的元素。迭代器必须实现__iter__()和__next__()方法，其中__iter__()返回迭代器自身，__next__()返回下一个元素。

当你调用内置函数iter()并传入一个可迭代对象时，它会返回该可迭代对象对应的迭代器。通过调用迭代器的__next__()方法，你可以逐个获取可迭代对象中的元素。

总结来说，迭代器是用于提供对可迭代对象元素逐个访问的工具，而可迭代对象则是提供迭代器的对象。

在 Python 中，通常情况下你不会直接操作迭代器，而是通过循环或其他迭代工具来隐式地使用迭代器。这种设计使得迭代在 Python 中变得非常方便和强大。   
"""
# 列表
# 可迭代对象 ：可以for 循环遍历的都是可迭代对象
# li = [1, 2, 3, 4, 5]
# li1 = iter(li)
# print(next(li1))

# 生成器是迭代器的一种

# 生成器相比迭代器多了几种方法 send()方法
"""
4、生成器和迭代器的区别:
生成器属于迭代器的一种,如何区分迭代器和生成器?
1、生成器相比选代器多了三种方法:send(),close(),throw()
send()方法,发送数据
close方法:关闭生成器
throw方法:
gen.throw(Exception,"Method throw called!")
生成器<迭代器<可迭代对象

"""


def gen():
    for i in range(1,5):
        se = yield i
        print('se的值:',se)


g = gen()
print(next(g))
print(g.send(100))
print(next(g))


"""
具体应用场景
生成器在许多场景下都有广泛的应用。以下是一些常见的使用场景和相应的示例代码：

迭代处理大型文件： 在需要处理大型文件时，生成器可以逐行读取文件内容，而不必一次性加载整个文件到内存中。
python
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# 使用生成器逐行读取大型文件
for line in read_large_file('large_file.txt'):
    # 处理每一行数据
    print(line)
惰性计算： 当需要进行惰性计算时，生成器可以按需生成计算结果，而不必提前计算所有可能的值。
python
def generate_numbers(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# 使用生成器按需生成数字
for num in generate_numbers(1, 10):
    # 处理每一个生成的数字
    print(num)
处理无限序列： 生成器非常适合表示无限序列，例如 Fibonacci 数列或素数序列。
python
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器生成 Fibonacci 数列
fib_generator = fibonacci_sequence()
for _ in range(10):
    print(next(fib_generator))
流式处理数据： 生成器可用于流式处理数据，例如从网络流或传感器流中读取数据。
python
def process_sensor_data(sensor):
    while True:
        data = sensor.read_data()
        if data is None:
            break
        yield process(data)

# 使用生成器处理传感器数据
sensor = Sensor()
for processed_data in process_sensor_data(sensor):
    # 处理每一条处理后的数据
    print(processed_data)

9 00:00
"""