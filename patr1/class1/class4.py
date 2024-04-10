# -*- coding: utf-8 -*-
# @file: class4.py
# @time: 2024 
# @user: Nemo
"""
面向对象之魔术方法



"""

"""
一、魔术方法
(魔法方法、特殊方法)
问题一:_init_有什么作用?
在创建对象的时候,自动调用对创建的对象进行初始化设置的的,

问题二:什么是魔术方法?
在python中像_init_这类双下划线开头和结尾的方法,我们把它统称为魔术方法。

注意点:
魔术方法都是python内部定义的,自己不要去定义_init_这中双下划线先开头的方法

问题三:创建一个对象的时候,调用的第一个方法是什么?
创建对象，第一个调用的方法是new 方法



"""


# class MyClass(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         print('new方法')
#         # return super().__new__(cls)
#         return object.__new__(cls)
#
#
# m = MyClass('MuSen')
# print(m.name)



"""
单例模式

单例模式是一种设计模式，用于确保类只有一个实例，并提供一个全局访问点。

在单例模式中，类的构造函数是私有的，这意味着外部无法直接实例化该类。而是通过类的静态方法或者静态属性来获取该类的唯一实例。如果该类的实例不存在，则静态方法或属性会创建一个新的实例；如果实例已存在，则返回该实例。

单例模式的实现方式有多种，其中最常见的方式是使用静态属性或者静态方法来保存类的唯一实例。在多线程环境下，需要考虑线程安全性，确保多个线程同时访问时不会创建多个实例。

单例模式通常用于需要全局访问点的场景，例如数据库连接、日志记录器、配置管理等。

以下是一个简单的单例模式示例（使用静态属性实现）：

用new 实现单例模式

```python
class Singleton:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

# 示例用法
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # 输出：True，说明两个变量引用的是同一个实例
```

在这个示例中，`Singleton` 类的构造函数是私有的，通过 `__new__` 方法控制实例的创建，如果 `_instance` 属性为 `None`，则创建一个新的实例并赋值给 `_instance`，否则返回已存在的实例。


单例模式适用于以下场景：

1. **全局资源访问**：当需要在程序的多个部分共享同一个资源时，可以使用单例模式确保只有一个实例存在，避免资源的重复创建和浪费。

2. **配置信息管理**：单例模式可以用于管理全局的配置信息，确保在程序中的任何地方都能访问到相同的配置信息，避免不同部分的配置信息不一致。

3. **日志记录器**：在多个组件或者线程中共享同一个日志记录器时，可以使用单例模式来确保只有一个日志记录器实例存在，避免日志信息的混乱和重复。

4. **数据库连接池**：在需要频繁进行数据库操作的应用中，可以使用单例模式来管理数据库连接池，确保只有一个连接池实例存在，避免资源的浪费和连接数过多。

5. **线程池**：在需要并发处理任务的应用中，可以使用单例模式管理线程池，确保只有一个线程池实例存在，避免创建过多线程和资源的浪费。

需要注意的是，单例模式可能导致全局状态的存在，使得代码的维护和测试变得困难。因此，在使用单例模式时需要权衡利弊，并确保合理使用和设计。


装饰器实现单例模式

def singleton(cls, *args, **kw):    
    instances = {}    
    def wrapper():    
        if cls not in instances:    
            instances[cls] = cls(*args, **kw)    
        return instances[cls]    
    return wrapper  

@singleton
class Animal(object):
    def __init__(self):
        pass
    
animal1 = Animal()
animal2 = Animal()
print(id(animal1))
print(id(animal2))




"""


# class Singleton:
#     _instance = None
#     print(_instance)
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#
#         return cls._instance
#
#
# # 示例用法
# singleton1 = Singleton()
# print(singleton1._instance)
# print(id(singleton1))


"""
3、_str_方法和_repr_方法
环境:交互环境代码演示
>>> a = "abc'
>>> print(a)
abc
abc
问题思考:交互环境下print打印的内容和和直接输入变量,返回的内容不一样这是为什么?
python的问直函数str和repr,format
。内置函数str转换一个对象时,触发对象对应__str__的方法,
。内置函数format处理对象是,触发对象对应__str__的方法。
。内置函数repr函数,触发对象的__repr__的方法



使用print打印的时候触发的是__str__方法,
交互环境直接输入变量的时候触发的是__repr__方法。

注意点:

重写__str__和__repr__方法时,必须要记得写return,
重写__str__和__repr__方法时,return返回的必须是一个字符串对象,

__str__ 方法不存在的话会执行__repr__方法

str方法给用户看，repr给程序员看的


总结:
使用str函数或者print打印对象时会先优先触发str方法,没定义str方法的情况下,会再去找repr方法,如果
都没有,那么就会去找父类的str方法。

使用repr方法或者交互环境下输入变量,会先找自身的repr方法,自身没有repr方法,会再去找父类的repr
方法。


"""


# class Myt(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         print('--str---触发了--')
#         return self.name
#
#     def __repr__(self):
#         print('__reper__被触发了')
#         return '<MyClass.object-{}>'.format(self.name)
#
#
# m = Myt('MUSEN')
#
# cc = repr(m)
# print(cc)
#
#

"""
4、__call__方法
问题一:在python中万物皆对象,函数也是对象,为什么函数可以调用,而其他的对象不行?

问题二:如果想让类创建出来的对象,可以像函数一样被调用可以实现吗?


class Test(object):
    def __call__(self):
        print(触发了ca11方法')
        
t = Test()
t()



用类实现装饰器
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在被装饰的函数执行前的逻辑
        print("Before function execution")

        # 调用被装饰的函数
        result = self.func(*args, **kwargs)

        # 在被装饰的函数执行后的逻辑
        print("After function execution")

        return result

# 使用装饰器类
@Decorator     # my_function = Decorator(my_function)
def my_function():
    print("Inside the function")

# 调用被装饰的函数
my_function()


"""

"""





其他算术运算符对应的魔术方法:
_add_(self,other)   定义加法的行为:+
_sub_(self,other)   定义减法的行为:-
_mul_(self,other)   定义乘法的行为:*
_truediv_(self,other)   定义真除法的行为:/
_floordiv_(self,other)  定义整数除法的行为://
_mod_(self,other)   定义取余算法的行为:%
更多的魔术方法参考地址:https://www.cnblogs.com/nmb-musen/p/10861536.html



5、上下文管理器
问题思考:with打开文件为何会自动关闭?

上下文管理器的概念:上下文管理器是一个Python对象,为操作提供了额外的上下文信息。这种额外的信息,在
使用with语句初始化上下文,以及完成with块中的所有代码时,采用可调用的形式。

with open("example.txt", "w") as file:
    file.write("数据分析机制")
    



上下文管理器是一种 Python 对象，它定义了在进入和退出某个代码块时需要执行的操作。通常情况下，上下文管理器会使用 `with` 语句进行管理。在 `with` 语句块中，会自动获取和释放资源，无论代码块是否出现异常。

你可以通过两种方式来实现上下文管理器：

1. 使用类：你可以定义一个类，并实现 `__enter__` 和 `__exit__` 方法来创建一个上下文管理器。
2. 使用 `contextlib` 模块：你也可以使用 `contextlib` 模块中的装饰器 `contextmanager` 来创建一个上下文管理器。



下面是两种方式的示例：

**使用类实现上下文管理器：**

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        # 返回需要管理的资源
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # 在退出上下文时进行清理工作

# 使用上下文管理器
with MyContextManager() as cm:
    # 在 with 语句块中执行操作
    print("Inside the context")
```

**使用 `contextlib` 模块实现上下文管理器：**

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    # 在 yield 之前相当于 __enter__ 方法
    yield
    # 在 yield 之后相当于 __exit__ 方法
    print("Exiting the context")

# 使用上下文管理器
with my_context_manager():
    # 在 with 语句块中执行操作
    print("Inside the context")
```

无论你选择哪种方式，都可以使用 `with` 语句来管理资源，确保资源在退出代码块时被正确释放，即使在代码块中发生异常时也会被释放。





"""
with open('12') as f:
    f.write("123")

"""
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")

# 使用上下文管理器计时代码执行时间
with Timer():
    # 模拟一些耗时操作
    time.sleep(2)


"""


