# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/19 22:31
# Warning    ：The Hard Way Is Easier


class Str:
    # def __str__(self):
    #     print("__str__")
    #     return "__str__ called"

    def __repr__(self):
        print("__repr__")
        return "__repr__ called"


class A:
    def __init__(self, name, site):
        self.name = name
        self.site = site

    def f(self):
        print(self.__dict__)

    def __getattr__(self, name):
        print("__getattr__")

    def __getattribute__(self, name):
        print("__getattribute_")
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print("__setattr__")
        self.__dict__[name] = value


if __name__ == '__main__':
    s = Str()
    # str(s)
    # print(s)
    # print(str(s))

    print(A.__dict__)
    is_getattribute = hasattr(A, "__getattribute__")
    print(is_getattribute)
    a = A("benny", "wuhan")
    # print(a.__dict__)
    # print(vars(a))
    print("hasattr ...")
    hasattr(a, 'name')
    print("getattr ...")
    getattr(a, "name")
    print("a,f() ...")
    a.f()