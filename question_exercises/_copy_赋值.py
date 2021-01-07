# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
================================================================
Q-1: 描述错误的是？

A a ==  [1,2, 3, 4, ['a', 'b', 'c'], 5]
B b ==  [1,2, 3, 4, ['a', 'b', 'c'], 5]
C c ==  [1,2, 3, 4, ['a', 'b', 'c']]
D d ==  [1,2, 3, 4, ['a', 'b', ‘c’]]
"""
import copy

a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
# 这里操作b，结果仍不变
a.append(5)
a[4].append('c')
print("a", a)
print("b", b)
print("c", c)
print("d", d)

"""
================================================================
Q-2: 下列代码执行结果是什么?
x = 1
def change(a):
    x += 1
    print(x)
change(x)

A 1
B 2
C 3
D 报错

# 报错
"""

"""
================================================================
Q-3: 下列代码执行结果是什么?
name = "benny"
def f1():
    print(name)
def f2():
    name = "jane"

f1()
f1()
f2()


"""

name = "benny"


def f1():
    print(name)


name = "jane"


def f2():
    name = "jane"


f1()
f1()
f2()

"""
================================================================
Q-4: 下列代码执行结果是什么?
name = "benny"
def f1():
    print(name)
name = "jane"
def f2():
    name = "tom"

f1()
f1()
f2()
"""
