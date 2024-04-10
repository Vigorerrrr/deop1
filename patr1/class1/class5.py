# -*- coding: utf-8 -*-
# @file: class5.py
# @time: 2024 
# @user: Nemo
"""


"""


"""
二、多态
2.1、面向对象三大特征
面向对象编程的三大特征:封装,继承,多态

封装:将数据和方法放在一个类中就构成了封装,

继承:python中一个类可以继承于一个类也可以继承多个类,被继承的的类叫父类(或者叫基类,base
class),继承的类叫子类。

多态(Polymorphism):指的是一类事物有多种形态,一个抽象类有多个子类(因而多态的概念依赖于
继承),不同的子类对象调用相同的方法,产生不同的执行结果,多态可以增加代码的灵活度


2.2、多态
实现多态的步骤:
1、定义一个父类(Base),实现某个方法(比如:run)
2、定义多个子类,在子类中重写父类的方法(run),每个子类run方法实现不同的功能
3、假设我们定义了一个函数,需要一个Base类型的对象的参数,那么调用函数函数的时候,传入Base
类不同的子类对象,那么这个函数就会执行不同的功能,这就是多态的体现
还是不懂多态?没关系看一段代码就明白了。

class Base(object):
    def run(self):
        print('_____base__run____:慢慢走路')
        
class Cat(Base):
    def run(self):
        print('___cat___run___:会爬树')
        
class Dog(Base):
    def run(self):
        print('___cat___ruh____:会爬树')

------------------------------------------------


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# 多态性示例
def make_animal_speak(animal):
    animal.speak()

# 创建不同类型的动物对象
animal1 = Animal()
animal2 = Dog()
animal3 = Cat()

# 调用统一的方法，产生不同的行为
make_animal_speak(animal1)  # Output: Animal speaks
make_animal_speak(animal2)  # Output: Dog barks
make_animal_speak(animal3)  # Output: Cat meows


注意点:Python中函数的参数是没有类型限制的,所有多态在python中的体现并不是很严谨,多态的概念
是应用于Java和C#这一类强类型语言中,而Python崇尚"鸭子类型"



2.3、鸭子类型
鸭子类型概念:它并不要求严格的继承体系,关注的不是对象的类型本身,而是它是如何使用的,一个对象只
要"看起来像鸭子,走起路来像鸭子",那它就可以被看做是鸭子···

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

class Duck:
    def speak(self):
        print("Duck quacks")

# 函数接受任何具有 speak 方法的对象
def make_speak(animal):
    animal.speak()

# 不同类型的动物对象
dog = Dog()
cat = Cat()
duck = Duck()

# 调用函数，产生不同的行为
make_speak(dog)   # Output: Dog barks
make_speak(cat)   # Output: Cat meows
make_speak(duck)  # Output: Duck quacks


鸭子类型的体现:
静态语言:对于静态语言(java,C#)来讲上面传入的对象必须是Basc类型或者它的子类,否则,将无法
调用run()方法。

动态语言:对于动态语言python来讲,上面传入的并不一定要是Base类型,也可以是其他类型,只要再
内部实现一个run()方法就行了,这就是鸭子类型的体现,




多态的意义:开放封闭原则
对于一个变量,我们只需要知道它是Base类型,无需确切地知道它的子类型,就可以放心地调用run()方
法,(调用方只管调用,不管细节)
。当需要新增功能,只需要新增一个Base的子类实现run()方法,就可以在原来的基础上进行功能扩展,这
就是著名的"开放封闭"原则:
。对扩展开放:允许新增Base子类;
。对修改封闭:不需要修改依赖Base类型的run()等函数;


"""
"""
三、数据和自省
3.1、私有属性
类里面定义的变量叫类属性,那么类属性有两种,分为:公有属性和私有属性.

私有属性定义:
。单下滑线开头:attr
。双下划线开头:attr


class Test(object):
    _attr = 100         #在外部可以直接访问
    __attr2 = 200       #在外部不能直接访问,被改名了,所有在外部访问不了,改成了_Test__attr2

t = Test()
#查看该类的所有属性和方法
print(Test.__dict__)

双下划线开头的私有属性，对外都是改了名字


Python并没有真正的私有化支持,但可用下划线得到伪私有,有一项大多数Python代码都遵循的习惯:带
有下划线,前缀的名称应被视为非公开的API的一部分(无论是函数、方法还是数据成员)。它应被视为实
现细节,如有更改,恕不另行通知。

双下划线的私有属性也是能够继承的


3.2、__dict__
类调用__dict__属性,返s类属性和方法的字典。
实列调用__dict__属性,返回的值实列相关的属性和方法



3.3、内置属性__slots__
默认情况下,类的实例有一个字典用于存储属性。这对于具有很少实例变量的对象会浪费空间,当创建大量实例
时,空间消耗可能会变得尖锐。
可以通过在类定义中定义__slots__来覆盖默认__dict__行为。__slots__声明接受一个实例变量序列,并在每个
实例中只保留足够保存每个变量值的空间,因为没有为每个实例创建__dict__所以节省空间


在 Python 中，`__slots__` 是一个特殊的属性，用于限制类实例可以拥有的属性。通过定义 `__slots__`，你可以控制类实例的内部属性字典的大小，从而优化内存使用和属性访问速度。

使用 `__slots__` 的主要优点包括：

1. **减少内存消耗**：默认情况下，Python 类的实例会使用一个字典来存储实例的属性。这种灵活性意味着你可以动态地添加新的属性。但是，这也意味着每个实例都要消耗额外的内存来存储字典。通过使用 `__slots__`，你可以在类级别上预先分配固定数量的内存来存储属性，从而减少了额外的内存消耗。

2. **提高属性访问速度**：由于实例属性的存储方式由字典转变为元组，使用 `__slots__` 可以加快属性的访问速度。因为在元组中，属性的访问是通过索引来实现的，而不是通过哈希表查找。

使用 `__slots__` 的示例：

```python
class MyClass:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(10, 20)
print(obj.x)  # Output: 10
print(obj.y)  # Output: 20

# 试图添加未定义在 __slots__ 中的属性会引发 AttributeError
obj.z = 30  # AttributeError: 'MyClass' object has no attribute 'z'
```

在上面的示例中，`MyClass` 使用 `__slots__` 来限制实例只能拥有 `x` 和 `y` 两个属性。因此，尝试添加 `z` 属性会导致 `AttributeError`。


import pymysql


class DB:

    def __init_(self,data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor=self.con.cursor()
        
    def __enter__(self):
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


DATABASES_CONF = dict(
host='localhost',
user='root',
password="mysql",
database='test',
port=3306,
charset='utf8')

with DB(DATABASES_CONF) as cur:
    cur.execute('SELECT * FROM students')
    print(cur.fetchone())




slots 属性限制对象属性，节约内存



"""






























