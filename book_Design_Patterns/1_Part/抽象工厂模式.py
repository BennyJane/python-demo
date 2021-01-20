# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

class A:
    """基础类A"""


class B:
    """基础类B"""


class Factory1:
    def __init__(self, *arg, **kwargs):
        self.attr = arg

    def com_method1(self):
        """返回被管理的类实例"""
        return A()

    def com_method2(self):
        """返回被管理的类实例"""
        return B()


class C:
    """基础类C"""


class D:
    """基础类D"""


class Factory2:
    def __init__(self, *arg, **kwargs):
        self.attr = arg

    def com_method1(self):
        """返回被管理的类实例"""
        return C()

    def com_method2(self):
        """返回被管理的类实例"""
        return D()


# 抽象工厂使用管理类
class AbstractFactoryManage:
    def __init__(self, factory):
        """传入"""
        self.com_attr1 = factory.com_method1()
        self.com_attr2 = factory.com_method2()

    def common(self):
        """各个抽象工厂实例的使用逻辑代码"""


if __name__ == '__main__':
    # 根据条件，选择需要实例化的抽象工厂：例如 Factory1
    factory_instance = Factory1()
    _instance = AbstractFactoryManage(factory_instance)
    _instance.common()
