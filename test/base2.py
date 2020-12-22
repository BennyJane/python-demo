# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/13 14:03
# Warning    ：The Hard Way Is Easier
import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
print('a', id(a))
b = a  #赋值，传对象的引用
print('b', id(b))
c = copy.copy(a)  #对象拷贝，浅拷贝
print('c', id(c))
d = copy.deepcopy(a)  #对象拷贝，深拷贝

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

def func(a):
    print(id(a))
    a=list(a)
    print(a)
    a.append(10)
    print(id(a))
    print(a)
func(a)
print('a = ', a)

print(dir(func))
