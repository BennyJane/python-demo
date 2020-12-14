# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/12 22:19
# Warning    ：The Hard Way Is Easier
a = 1
print(id(a))


def func(a=a):
    print(a)
    print(id(a))
    a = 2
    print(id(a))


func(a)
print(a)

l = [1, 2, 3, 4]
sl = l

# l、sl均指向相同的内存id，具有相同的引用对象
# 修改任一个变量，因为两个变量的引用指向没有变化，所以另一个也会受到影响、
l.append(5)

print(sl)

a = []


def fun(a):
    a.append(1)


fun(a)
print(a)  # [1]

# 修改
a = []
func(a=list(a))
print(a)
from copy import deepcopy

func(a=deepcopy(a))
print(a)


class A(object):
    def foo(self, x):  # 实例方法
        print("executing foo(%s,%s)" % (self, x))

    @classmethod  # 类方法
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):  # 静态方法
        print("executing static_foo(%s)" % x)


a = A()

a.class_foo(10)

name = (1, 2, 3)
# print("hi there %s" % name)
"hi there %s" % (name,)  # supply the single argument as a single-item tuple
print("hi there %s" % (name,))


class Overloading(object):
    def __init__(self, x):
        self.x = x

    @classmethod
    def NewInit(cls, x, y):
        b = cls(x * y)
        b.z = x - y
        return b


a = Overloading(4)
b = Overloading.NewInit(4, 5)

print(b.z)