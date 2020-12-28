# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 16:52
# Warning    ：The Hard Way Is Easier

import copy

# 不可变对象，只会添加指向同一个内存地址的的对象引用，不会创建新的对象
a = "benny"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print("a", id(a))
print("b", id(b))
print("c", id(c))
print("d", id(d))

#
a = "tom"
b = a
print("a", id(a))
print("b", id(b))

a = [1, 2, 3]
b = a
b.append(4)
print(a)
