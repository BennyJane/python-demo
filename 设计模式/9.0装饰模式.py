# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise


class foo(object):
    def f1(self):
        print("Origin f1")

    def f2(self):
        print("Origin f2")


class foo_decorator:
    def __init__(self, decorate):
        self._decorate = decorate

    def f1(self):
        print("decorate f1")
        self._decorate.f1()

    def __getattr__(self, item):
        print("[__getattr__]", item)
        return getattr(self._decorate, item)
    # def __getattribute__(self, item):
    #     print("[__getattribute__]")
    #     return getattr(self._decorate, item)

    def __get__(self, instance, owner):
        """"""
        print("__get__")


if __name__ == '__main__':
    f = foo()
    F = foo_decorator(f)
    F.f1()
    # print(F.f2)
    # F.f2  -> F.f2()
    F.f2()
    # F.f3