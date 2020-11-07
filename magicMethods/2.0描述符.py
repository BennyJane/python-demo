# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise
import math


class A(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("property get ...")
        return self._name

    @name.setter
    def name(self, name):
        print("property setter ...")
        self._name = name


def base1():
    a = A("A")
    a.__dict__['name'] = "C"  # 跳过 __setter__  __set__方法,直接修改存储内容
    # a.name = "C"  # 对于描述符, 调用 __set__
    # setattr(a, "name", "C")   #  对于描述符, 调用 __set__; 一般属性, 调用 __setattr__
    # print(dir(a))
    print(a.name)
    # a.name = "B"
    # print(a.name)


class lazy(object):
    def __init__(self, func):
        print("lazy init ....")
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        # setattr(instance, self.func.__name__, val)
        # instance.__dict__[self.func.__name__] = val
        return val


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy  # code运行以前就会被执行, 参考装饰器
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2

    def length(self):
        return 2 * math.pi * self.radius

    lazyAttr = lazy(length)
    print(lazy(length))
    A("A")


def base2():
    c = Circle(4)
    # print(dir(c))
    print(c.radius)

    print(c.area)
    c.area = "10"
    # print(dir(c))
    print(c.area)
    print(c.area)


def base3():
    print(dir(Circle))
    c = Circle(10)
    print(dir(c))
    pass


if __name__ == '__main__':
    # base1()
    # base2()
    base3()
    pass
