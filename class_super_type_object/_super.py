# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 10:16
# Warning    ：The Hard Way Is Easier


"""源码：
super() -> same as super(__class__, <first argument>)
super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
如果第二个参数省略，返回的super对象是未绑定到确定的MRO上的：
如果第二个参数是对象，那么isinstance(obj, type)必须为True；
如果第二个参数是类型，那么issubclass(type2, type)必须为True，即第二个参数类型是第一个参数类型的子类。


Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super().meth(arg)
This works for class methods too:
class C(B):
    @classmethod
    def cmeth(cls, arg):
        super().cmeth(arg)

# (copied from class doc)

================================================================================================================
super(cls, obj): 当接收两个参数时，必须确保obj是cls的子类
super([type[, object-or-type]])：
super函数返回委托类type的父类或者兄弟类方法调用的代理对象。super用来调用已经在子类中重写了的父类方法。
方法的搜索顺序与getattr()函数相同，只是参数类type本身被忽略。
"""


class A:
    def meth(self, arg):
        print("A:meth")
        # 单独实例化A类调用，会报错，父类无法找到该方法
        # 该方法在C类实例中调用，不会报错，会调用B类的同名方法
        super(A, self).meth()  # FIXME 应该定义为混入类来使用
        return arg * 1

    def cmeth(self, arg):
        print("A:cmeth")
        return 2 * arg


class B:

    def meth(self, arg):
        print("B:meth")
        return arg

    def cmeth(self, arg):
        print("B:cmeth")
        return 2 * arg


# C.__mro__() => [C,A, B, Object]
class C(A, B):
    def meth(self, arg):
        print("C:meth")
        # super(C, self).meth() 简写为 super().meth(arg)
        super().meth(arg)

    @classmethod
    def cmeth(cls, arg):
        print("C:cmeth")
        super().cmeth(arg)


if __name__ == '__main__':
    a = A()
