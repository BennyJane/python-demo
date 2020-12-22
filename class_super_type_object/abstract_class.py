# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/21 21:08
# Warning    ：The Hard Way Is Easier
import abc


# 参考文章：https://www.jb51.net/article/87710.htm
# FIXME 抽象属性应该已经被弃用

class Sheep(object):
    """普通类"""

    def get_size(self):
        """定义必须实现的方法"""
        raise NotImplementedError


"""
========================================================================================================================
抽象类定义形式
class AbstractSheep(metaclass=abc.ABCMeta):

class AbstractSheep2(abc.ABC):
    
class AbstractSheep(object):
    __metaclass__ = abc.ABCMeta

子类：调用抽象父类的方法
super(ChildClass, self).method()
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


# 不能使用 metaclass=abc.ABC
class AbstractSheep2(abc.ABC):
    """抽象类"""

    @abc.abstractmethod
    def get_size(cls):
        """抽象方法"""
        print("AbstractSheep2...")


class ChildrenSheep(AbstractSheep2):
    """子类"""

    def get_size(self):
        super(ChildrenSheep, self).get_size()
        return 11


"""
========================================================================================================================
__subclasses__  : 获取所有子类的对象列表

__subclasshook__: 由issubclass()方法触发， 修改子类判断逻辑
========================================================================================================================
"""

for cls in AbstractSheep2.__subclasses__():
    print(cls.__name__)


class CustomAbstract(object):
    child_method = "say"

    @classmethod
    def __subclasshook__(cls, Obj):
        #  Obj 必须时类，实例没有 __mro__属性
        print("__subclasshook__")
        if cls is CustomAbstract:
            if any("say" in subclass.__dict__ for subclass in Obj.__mro__):
                return True
        return NotImplementedError


class ChildCustom(object):
    def say(self, name):
        print(name)


def Test1():
    s1 = Sheep()
    # s1.get_size()  # 抛出 NotImplementError

    # s2 = AbstractSheep()  # 抽象类允许实例化，但抽象方法没有实现会报错
    s2 = ChildSheep()  # 子类需要实现； 未实现抽象方法，抛出TypeError

    s2 = ChildrenSheep()


def Test2():
    c = CustomAbstract()
    child = ChildCustom()
    print(issubclass(ChildCustom, CustomAbstract))  # False
    print(isinstance(child, CustomAbstract))  # False
    print(CustomAbstract.__subclasshook__(ChildCustom))


if __name__ == '__main__':
    t = Test1()
    Test2()
