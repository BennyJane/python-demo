# -*- coding: utf-8 -*-
# @Time : 2020/9/22
# @Author : Benny Jane
# @Email : 暂无
# @File : temp.py
# @Project : Learning_Py_World


class Singleton(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = type.__new__(cls, *args, **kwargs)
        return cls._instance

    def __str__(self):
        return self.name + ":" + str(self.age)


s1 = Singleton('wtt', 25)
s2 = Singleton('zmy', 30)
print(s1)
print(s2)
