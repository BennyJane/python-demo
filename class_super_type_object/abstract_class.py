# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/21 21:08
# Warning    ：The Hard Way Is Easier
import abc


class Sheep(object):
    """普通类"""

    def get_size(self):
        """定义必须实现的方法"""
        raise NotImplementedError


"""
========================================================================================================================
抽象类定义形式
class AbstractSheep(metaclass=abc.ABCMeta):

class AbstractSheep(metaclass=abc.ABC):
    
class AbstractSheep(object):
    __metaclass__ = abc.ABCMeta
    
========================================================================================================================
"""


class AbstractSheep(metaclass=abc.ABCMeta):
    """抽象类"""

    @abc.abstractmethod
    def get_size(cls):
        """抽象方法"""


class ChildSheep(AbstractSheep):
    """继承自抽象类的子类"""

    def get_size(self):
        return 10


class ChildrenSheep(object):
    """子类"""



def Test1():
    s1 = Sheep()
    # s1.get_size()  # 抛出 NotImplementError

    # s2 = AbstractSheep()  # 抽象类允许实例化，但抽象方法没有实现会报错
    s2 = ChildSheep()  # 子类需要实现； 未实现抽象方法，抛出TypeError


if __name__ == '__main__':
    t = Test1()
