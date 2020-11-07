# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class A(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self, arg=10):
        print(arg)
        print("property get ...")
        return self._name

    @name.setter
    def name(self, name):
        print("property setter ...")
        self._name = name


def base1():
    a = A("A")
    a.__dict__['name'] = "C0000"
    # a.name = "C"
    # setattr(a, "name", "C")
    A.__dict__['name'] = "benny"
    print(vars(a))
    print(vars(A))
    print(a.name)
    print(a._name)
    # a.name = "B"
    # print(a.name)


class lazy(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy
    def area(self):
        print('evalute')

        return 3.14 * self.radius ** 2


def base2():
    c = Circle(4)
    print(dir(c))
    print(c.radius)

    print(c.area)
    print(dir(c))
    print(c.area)
    print(c.area)


if __name__ == '__main__':
    base1()
    pass
