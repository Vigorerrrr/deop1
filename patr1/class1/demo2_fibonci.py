# -*- coding: utf-8 -*-
# @file: demo2_fibonci.py
# @time: 2024 
# @user: Nemo
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 2
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# ss = fibonacci(5)
# print(ss)

"""


"""


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 打印前十项斐波那契数列


for i in range(100):
    print(fibonacci_iterative(i), end=" ")


