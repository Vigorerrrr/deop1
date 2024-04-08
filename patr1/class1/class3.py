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





"""

numbers = [1, 2, 3, 4, 5]

# 使用 lambda 函数和 map 函数对列表中的每个元素进行平方操作
squared_numbers = map(lambda x: x ** 2, numbers)
for i in squared_numbers:
    print(i)
"""

一、闭包
在上面我们见过了再函数中调用函数本身,那么在函数中可不可以定义一个函数,
问题需求:如何函数外部调用函数内部定义的函数?

问题的引入:,到底什么是闭包?

闭包的概念:一个完整的闭包须满足一下三个条件:
函数中嵌套一个函数
外层函数返回内层函数的变量名
内层函数对外部作用域有一个非全局的变量进行引用

最简单的闭包案列
def funcB1():
    x=100
    def funcB2():
        C= X2
        print(c)
    return funcB2



def outer_function(x):
    # 在外部函数中定义了一个内部函数
    x = x + 1
    def inner_function(y):
        return x + y  # 内部函数可以访问外部函数的变量 x
    return inner_function  # 外部函数返回内部函数

# 创建一个闭包函数

closure = outer_function(10)

# 调用闭包函数
result = closure(5)  # 这里的 result 将会是 10 + 5 = 15
print(result)
print(outer_function(10)(5))


闭包函数在编程中有几种常见的作用和用途：

1. **封装功能**: 闭包允许您在函数内部定义另一个函数，并将其返回。这使得您可以将一些功能封装在内部函数中，然后通过外部函数的调用来访问这些功能。这有助于保持代码的模块化和可读性。

2. **保存状态**: 闭包可以捕获外部函数中的局部变量，并在外部函数执行完成后保持其状态。这意味着您可以在闭包中访问和修改外部函数的变量，而无需全局变量或实例变量。这在需要在多次调用之间保持状态时非常有用。

3. **回调函数**: 闭包经常用作回调函数，例如在事件处理或异步编程中。您可以将闭包传递给其他函数，并在特定条件下执行。这使得代码更具灵活性和可扩展性。

4. **装饰器**: 装饰器是一种特殊的闭包，它接受一个函数作为参数，并返回一个新的函数。装饰器通常用于添加额外的功能或修改函数的行为，而不需要修改函数的源代码。

5. **延迟计算**: 闭包允许您延迟执行一些计算或操作。您可以在创建闭包时设置一些参数或条件，然后在以后的某个时间点调用闭包以执行这些操作。

总的来说，闭包函数是一种强大的工具，可以增强代码的灵活性、可重用性和可维护性。它们使得代码更具表现力，并且可以帮助解决许多常见的编程问题。




二、装饰器
讲装饰器之前我们先来了解一下开放封闭原则(面向对象原则的核心)

开放封闭原则:软件实体应该是可扩展,而不可修改的。也就是说,对扩展是开放的,而对修改是封闭的。

装饰器的作用:在不更改原功能函数内部代码,并且不改变调用方法的情况下为原函数添加新的功能。

装饰器的应用场景:
1.登录验证
2.函数运行时间统计
3.执行函数之前做准备工作
4.执行函数后清理功能

例子
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()



"""

#开放封闭原则


def login(func):
    username = 'python01'
    password = 'lemonban'

    def fun():
        user = input('请输入账号:')
        pw = input('请输入密码:')
        if username == user and password == pw:
            func()
        else:
            print('账号或者密码错误')

    return fun


@login  # @login:--》index= login(index)
def index():
    print('这个是网站的首页')


index()

"""
装饰器和闭包函数的关系
装饰器（Decorator）和闭包函数（Closure）在 Python 中都是函数的高级用法，它们虽然在概念上有些不同，但在某些情况下可以结合使用。

### 装饰器（Decorator）：
- 装饰器是一个函数，它可以接受一个函数作为参数，并返回一个新的函数或可调用对象。
- 装饰器常用于修改或增强被装饰函数的行为，而不需要修改被装饰函数的定义。
- 使用装饰器可以在函数执行之前或之后执行额外的代码，或者对函数的输入或输出进行处理。

### 闭包函数（Closure）：
- 闭包函数是指可以访问其自由变量的函数，即使在函数定义之后、函数外部调用时也可以访问这些变量。
- 闭包函数通常用于保存局部状态、创建函数工厂或延迟执行等场景。
- 闭包函数由内部函数和包含该内部函数的环境（即自由变量所在的作用域）组成。

### 关系：
- 装饰器通常用于修改函数的行为，可以在不修改函数定义的情况下，通过装饰器为函数添加额外的功能或行为。装饰器本身就是一个闭包函数，它接受被装饰的函数作为参数，并返回一个新的函数。
- 在某些情况下，装饰器本身可能会使用闭包来实现某些功能。例如，在实现带参数的装饰器时，通常需要定义一个闭包函数来包裹原始的装饰器函数，以便向装饰器传递参数。

下面是一个简单的示例，演示了如何使用闭包函数和装饰器结合实现带参数的装饰器：

```python
def make_bold(func):
    def wrapper(text):
        return "<b>" + func(text) + "</b>"
    return wrapper

@make_bold
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))  # 输出：<b>Hello, World!</b>
```

在这个例子中，`make_bold` 是一个装饰器，它接受一个函数作为参数，并返回一个闭包函数 `wrapper`。在 `wrapper` 函数内部，可以访问 `func` 参数（即被装饰的函数），并在其返回值外部包裹 `<b>` 标签。最后，`@make_bold` 表示将 `greet` 函数传递给 `make_bold` 装饰器进行修饰。
"""


"""

def decorator(cls):
    # 在这里可以对类进行修改或增强
    cls.new_attribute = "Added by decorator"
    return cls

@decorator
class MyClass:
    def __init__(self):
        self.attribute = "Original attribute"

obj = MyClass()
print(obj.attribute)        # Original attribute
print(obj.new_attribute)    # Added by decorator




1,用类实现装饰器

2,多个装饰器装饰同一个函数
从下往上装饰，从上往下执行


3,python 中内置的三个装饰器



 
--------------------------------------------------------
with open('user.txt')as f:
    users=eval(f.read())


def login_check(func):
    def ado(*args,**kwargs):
        if not users['token']:  # 判断token值是否为False
            print('------登录页面------')
        username = input('账号:')
        password = input('密码:')


       # 登录校验
        if users["user"] == username and users["pwd"] == password:
            users['token'] = True
            func(*args,**kwargs)
        else:
            func(*args,**kwargs)

    return ado
---------------------------------------------------------------------


在 Python 中，有三个内置的装饰器：

1. `@staticmethod`: 用于声明静态方法。静态方法与类的实例无关，因此不会自动传递实例（`self`），只能通过类名调用。示例：

```python
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

# 调用静态方法
result = MyClass.static_method()
print(result)  # 输出："This is a static method"
```

2. `@classmethod`: 用于声明类方法。类方法与类相关联，第一个参数通常命名为 `cls`，用于表示类本身，可以通过类名或实例调用。示例：

```python
class MyClass:
    class_attr = "Class Attribute"

    @classmethod
    def class_method(cls):
        return cls.class_attr

# 调用类方法
result = MyClass.class_method()
print(result)  # 输出："Class Attribute"
```

3. `@property`: 用于创建属性，使得可以通过调用方法的方式来访问属性，而不需要使用 `()` 来调用方法。示例：

```python
class MyClass:
    def __init__(self):
        self._value = 0

    @property  # 设定只读
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("Value must be non-negative")

# 创建实例
obj = MyClass()

# 访问属性
print(obj.value)  # 输出：0

# 修改属性值
obj.value = 10
print(obj.value)  # 输出：10

# 尝试设置负值
try:
    obj.value = -5
except ValueError as e:
    print(e)  # 输出：Value must be non-negative
```

这些装饰器提供了一种便捷的方式来定义静态方法、类方法和属性，使得代码更加清晰和易于理解。

"""

