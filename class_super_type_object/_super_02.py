# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 13:10
# Warning    ：The Hard Way Is Easier

"""
==============================================================================================================
菱形继承：
类A继承层次结构如下：
  object
  	|
	D
   / \
  B   C
   \ /
    A

调用顺序
其中某个父类可以调用调用兄弟类的同名方法； 虽然这两个类没有继承关系
==============================================================================================================
"""


class D(object):

    def test(self):
        print('test in D')

    def d_method(self):
        print("method in D")


class C(D):

    def test(self):
        print('test in C')

    def c_method(self):
        print("method in C")


class B(D):

    def test(self):
        print('test in B')
        print(f"B： {id(self)}")
        # 在B实例上调用该方法，执行D的test方法（直接父类的方法）；使用的是B.__mro__
        # 在A实例上调用该方法，执行C的test方法（兄弟类的方法）; 使用的是A.__mro__, 位于B后面的类时C
        super(B, self).test()

    def b_method(self):
        print("method in B")


class A(B, C):

    def test(self):
        print('test in A')
        print(f"A： {id(self)}")
        super().test()  # 调用B的test方法


if __name__ == '__main__':
    a = A()
    print("A的方法解析顺序：", A.mro())
    print("A的方法解析顺序：", A.__mro__)
    # A 继承 b c d的方法，可以直接调用
    a.b_method()
    a.c_method()
    a.d_method()

    # super的调用顺序
    a.test()
    print("\n测试B类的继承调用")
    b = B()
    b.test()
