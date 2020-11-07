# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class A:
    name = 'A'

    def base(self):
        return self.name

    def __getattr__(self, item):
        print("__getattr__ ...")


if __name__ == '__main__':
    a = A()
    # print(a.name)
    # print(a.base)
    # print(a.c)
    # A.__mro__
    # print(A.__mro__)
    # print(a.__mro__)
    # print(dir(a))
    # print(dir(A))
    print(A.c)