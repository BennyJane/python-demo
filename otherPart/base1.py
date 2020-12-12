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