# -*- coding: utf-8 -*-
# @Time : 2020/11/6
# @Author : Benny Jane
# @Email : 暂无
# @File : 2.0demo.py
# @Project : Python-Exercise
import math


class lazyCache(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print("__get__...  ")
        val = self.func(instance)
        # setattr(instance, self.func.__name__, val)  #
        return val


class Circle(object):
    def __init__(self, circle):
        self.radius = circle
        # self.area = 20

    @lazyCache
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def name(self):
        print("property ...")
        return self.area


if __name__ == '__main__':
    c = Circle(10)
    print(c.area)
    print(vars(c))
    c.__dict__['area'] = 20
    # print(Circle.__dict__)
    # print(dir(Circle))
    print(c.name)
    Circle.name = "benny"
    # Circle.__dict__['name'] = 'benny'
    # setattr(Circle, "name", "benny")
    c.name = "tom"


    c.__dict__['name'] = "zsy"
    print(vars(c))
    # setattr(c, "name", 'jane')
    print(c.name)
    print(c.area)
    print(c.area)
    print(c.area)
