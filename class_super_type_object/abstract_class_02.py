# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/21 21:08
# Warning    ：The Hard Way Is Easier
import abc

import abc


class A(metaclass=abc.ABCMeta):
    # __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @name.setter
    @abc.abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abc.abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abc.abstractmethod
    def method2():
        pass


class B(A):
    def __init__(self):
        self.site = ""


def Test1():
    print(type(A))
    B()


if __name__ == '__main__':
    Test1()
