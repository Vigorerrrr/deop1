# -*- coding: utf-8 -*-
# @file: class1.py
# @time: 2024 
# @user: Nemo
"""
内存管理


"""

"""
一、对象引用
在python中我们来看一个最简单的赋值语句
 a = 10
首先这个10他是一个数值类型的对象,那么这个a呢?他只是一个个对10这个对象引用的变量,如果在下面我们再
 b=a
那么此时的打印b,返回的结果也是10这个对象,b也是对10这个变量的引用。

变量,通过变量指针引用对象
    变量指针指向具体对象的内存空间,取对象的值。

对象,类型已知,每个对象都包含一个头部信息(头部信息:类型标识符和引用计数器)


-5 256 都是提前创建好的，放在小整数池中







intern机制
在Python中，intern机制是一种优化技术，用于在解释器内部管理字符串对象，以提高内存使用效率和运行时性能。intern机制的核心思想是共享相同值的字符串对象，而不是创建多个相同值的副本。

具体来说，当解释器遇到一个新的字符串字面值时，它首先会检查该字符串是否已经存在于interned字符串池中。如果是，则直接返回指向该字符串对象的引用；如果不是，则将该字符串对象添加到interned字符串池中，并返回指向该字符串对象的引用。这样，相同值的字符串字面值在interned字符串池中只会存在一份，多个变量引用相同的字符串对象。

使用intern机制可以节省内存，并且在比较字符串时可以通过比较对象的引用来进行，而不必比较字符串的内容，从而提高了比较的速度。

需要注意的是，并非所有的字符串都会被intern，只有在一些特定情况下才会触发intern机制，例如：

1. 字符串字面值在模块级别被赋值。
2. 字符串字面值在函数的全局作用域中被赋值。
3. 字符串字面值在函数的默认参数中被赋值。

对于在运行时动态创建的字符串，通常不会被intern，因为这可能导致interned字符串池不断增长，影响性能。


只储存包含标准字符(数字、字母、下划线)的字符串
包含特殊字符的字符串不会被添加到大整数池中

54 
"""