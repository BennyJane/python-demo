# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/12 17:13
# Warning    ：The Hard Way Is Easier
import keyword
from pprint import pprint

print(keyword.iskeyword)
count = 0
# with open('./target.txt', 'r') as f:
# f.read() 获取文本中所有数据，但按照行划分
# print(f.readlines())
# print(f.readline())
# print(f.read())
# print(type(f.read()))
# for word in f.read():
#     print(word)
#     if word.isupper():
#         count += 1
# print(count)


mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8]

res = mylist[1:6:2]
print(res)

name = "benny"

print(name.capitalize())
print(name.count('e'))
print(name.isdigit())
print(name.lower())
print(name.upper())
# pprint(dir(name))

print(name.rsplit('n', maxsplit=2))
print('1,2,3,4,5'.rsplit(',', maxsplit=1))
print('1,2,3,4,5'.rsplit(','))

d = {"a": 1, "b": 2, "c": 3, "d": 4}

c = d.fromkeys(["name", "age"], 10)
print(c)
d.update()
print(d)

from test import *
from test import _private_name
from test import __name

print(_private_name)

print(__name)

mytuple = 3, 4, 5
# 解包
x, y, z = mytuple
a, *arg = mytuple
print(arg)

s = {1, 2, 3, 6, 4, 5}
print(s.pop())
print(s.pop())
print(s.add(12))
# print(s.clear())


sf = frozenset([1, 2, 3])
print(sf)
print(type(sf))
print(s.update([10]))
print(s)

zl = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(zl)

print(open('./target.txt'))
for line in reversed(list(open('./target.txt'))):
    print(line.rstrip())


def decorator_a(func):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)

    return inner_a


def decorator_b(func):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)

    return inner_b


# @decorator_b
# @decorator_a
def f(x):
    print('Get in f')
    return x * 2

# f(10)

func = decorator_b(decorator_a(f))
print(func.__name__)

func(20)