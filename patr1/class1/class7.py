# -*- coding: utf-8 -*-
# @file: class7.py
# @time: 2024 
# @user: Nemo

"""
四，元类

"""
"""
元类（metaclass）是面向对象编程中的一个概念，它用于创建类。在 Python 中，类是对象的模板，而元类则是类的模板。换句话说，元类是用来创建类的“类”。

在 Python 中，类是对象，因此它们必须由某种东西来创建。默认情况下，Python 中的类是由 `type` 类创建的。`type` 本身是一个元类，也是 Python 中所有类的元类。

你可以使用元类来控制类的创建过程，例如：

1. **自定义类的创建行为**：通过定义自己的元类，你可以在创建类时执行特定的操作，比如修改类的属性、添加方法等。
2. **实现单例模式**：元类可以确保一个类的实例只被创建一次，从而实现单例模式。
3. **进行类的验证和验证**：元类可以在类定义时执行验证，确保类的属性和方法符合特定的规范或约束。
4. **实现ORM框架**：许多ORM（对象关系映射）框架使用元类来创建类，并将类的属性映射到数据库表的字段。

在 Python 中，可以通过两种方式定义元类：

1. **继承 `type` 类**：创建一个类，继承自 `type` 类，并覆盖 `__new__` 方法来自定义类的创建行为。
2. **使用 `__metaclass__` 属性**：在类的定义中指定 `__metaclass__` 属性，使其指向一个元类。

以下是一个简单的示例，演示如何使用元类创建类：

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # 在创建类之前执行的操作
        print("Creating class:", name)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

# 输出：
# Creating class: MyClass
```

在这个例子中，`MyMeta` 是一个自定义的元类，继承自 `type` 类。当创建 `MyClass` 类时，会调用元类的 `__new__` 方法，输出提示信息。


什么是元类?
Python中的任何新式类以及Python3中的任何类都是type元类的一个实例,函数type实际上是一个元
类。type就是Python在背后用来创建所有类的元类

·注意区分元类和继承的基类:
otype:是元类 所有的类都是通过type所创建出来的
object:顶层的基类,所有类的继承顶层父类都是object



type创建类需要通过三个参数
类名
继承的父类
方法和属性




def func(self):
    print('---self----')





Test = type('Test',(object,), {"attr": 100, "_attr2":200,'function01':func})
print(Test.__dict__)
t = Test()
t.function01()

# class Test1(object):
#     attr = 100
#     __attr2 = 200
#
#
# print(Test1.__dict__)



"""

"""


自己继承元类

class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        print('creat class',*args,**kwargs)
        return super().__new__(cls,*args,**kwargs)


class MyClass(metaclass=MyMeta):
    pass



"""
"""
利用元类实现模型类

"""

from django.db import models


models.Model()

"""
元类1 58

"""






