# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 9:02
# Warning    ：The Hard Way Is Easier
import functools
import collections
import builtins
d = {"a": 1, "b": 2, "c": 3, 20: 4, (10, 2): 5}


def Test1():
    print(d.pop("a"))
    print(d.pop((10, 2)))

    del d[20]

    print(d.popitem())

    print(d)
    d.setdefault("b", 100)
    d.setdefault("f", 100)
    print(d)

if __name__ == '__main__':
    Test1()
    print("[test1 end...]===================")