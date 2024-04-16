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


"""

"""
深拷贝（deep copy）和浅拷贝（shallow copy）是在 Python 中用于复制对象的两种不同方式。

1. **浅拷贝**：

   - 浅拷贝会创建一个新的对象，但是该对象的内容是原始对象的引用。换句话说，浅拷贝创建了一个新的对象，但是其内部的子对象（如列表、字典等）仍然是原始对象中子对象的引用。
   - 浅拷贝可以使用 `copy()` 方法来实现，或者使用切片操作符 `[:]` 进行浅拷贝。

   ```python
   import copy
   
   list1 = [1, 2, [3, 4]]
   list2 = copy.copy(list1)  # 浅拷贝
   
   list1[0] = 5
   list1[2][0] = 6
   
   print(list1)  # 输出: [5, 2, [6, 4]]
   print(list2)  # 输出: [1, 2, [6, 4]]
   ```

2. **深拷贝**：

   - 深拷贝会递归地复制对象及其所有子对象，创建一个完全独立的新对象。即使原始对象的子对象也会被复制，而不是简单地引用。
   - 深拷贝可以使用 `copy.deepcopy()` 方法来实现。

   ```python
   import copy
   
   list1 = [1, 2, [3, 4]]
   list2 = copy.deepcopy(list1)  # 深拷贝
   
   list1[0] = 5
   list1[2][0] = 6
   
   print(list1)  # 输出: [5, 2, [6, 4]]
   print(list2)  # 输出: [1, 2, [3, 4]]
   ```

总的来说，浅拷贝只复制对象本身，而深拷贝会复制对象及其所有子对象。在处理嵌套结构（如列表中包含列表）时，通常需要使用深拷贝以确保各个对象的独立性。













拷贝应用
深浅拷贝在实际编程中有许多应用场景，下面列举一些常见的应用：

1. **列表或字典的复制**：

   当需要对列表或字典进行复制，并且不想改变原始对象时，可以使用深浅拷贝。

   ```python
   import copy

   original_list = [1, 2, [3, 4]]
   
   # 浅拷贝
   shallow_copy_list = original_list.copy()
   
   # 深拷贝
   deep_copy_list = copy.deepcopy(original_list)
   ```

2. **避免共享可变对象**：

   在多个对象中共享可变对象时，可以使用深拷贝来避免共享带来的意外修改。

   ```python
   import copy

   original_list = [1, 2, [3, 4]]
   
   # 共享原始列表的引用
   shared_list = [original_list, original_list]
   
   # 对共享列表中的元素进行深拷贝
   deep_copied_shared_list = copy.deepcopy(shared_list)
   ```

3. **处理递归数据结构**：

   当处理包含自引用的数据结构时，如树或图，可以使用深拷贝来处理。

   ```python
   import copy

   class Node:
       def __init__(self, value):
           self.value = value
           self.children = []
   
   # 创建一个包含自引用的树结构
   root = Node(1)
   child1 = Node(2)
   child2 = Node(3)
   root.children = [child1, child2]
   child1.children.append(child2)
   
   # 深拷贝树结构
   copied_root = copy.deepcopy(root)
   ```

4. **备份对象状态**：

   在某些情况下，需要对对象进行状态备份，以便在需要时能够回滚到先前的状态。

   ```python
   import copy

   class MyObject:
       def __init__(self, value):
           self.value = value
   
   obj = MyObject(1)
   obj_backup = copy.deepcopy(obj)  # 备份对象状态
   
   # 对对象进行修改
   obj.value = 2
   
   # 恢复对象到先前的状态
   obj = obj_backup
   ```

这些只是深浅拷贝在实际应用中的一些示例，它们在处理对象复制和管理数据结构时非常有用。
"""




