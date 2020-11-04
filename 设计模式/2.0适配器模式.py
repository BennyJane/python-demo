# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat:
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human:
    def __init__(self):
        self.name = "Human"

    def make_noise(self):
        return "hello!"


class Car:
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" * octane_level)


# todo 其他的实现方法： 类工厂，直接生成传入对象的子类， 并添加新的方法名，但调用被取代的方法
class Adapter(object):
    """
    调整一个对象方法调用的方式（修改方法调用的名称）
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """

    def __init__(self, obj, adapted_methods: dict):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """todo: 调用其他没有被修改的方法，也会指向原来的对象; 该方法必须写，否则新的实例对象，无法调用原来对象的其他属性；
        优点： 不需要直接继承原来的类
        """
        return getattr(self.obj, attr)


if __name__ == '__main__':
    dog = Dog()
    new_obj = Adapter(dog, dict(make_noise=dog.bark))
    print(new_obj.__dir__())  # 有 make_noise 属性，没有name属性
    print(dir(dog))  # 有name bark 属性，但没有 make_noise 属性
    print(f"A {new_obj.name} goes {new_obj.make_noise()}")
