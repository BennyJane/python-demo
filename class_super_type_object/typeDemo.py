# from six import with_metaclass
import os

""""
参考文章:https://www.cnblogs.com/ajianbeyourself/p/4052084.html
元类: 创建类的类  ==> 实例化后,得到类, 也是元类
Python中只有type类及其子类可以作为元类

type类的元类是自身,但是type本省也是对象,也是继承自object
一切类的创建最终都会调用type.__new__(cls, classname, bases, attrs)
    - type(obj)
        - 等效: obj.__class__
        - obj.__class__.__class__ 获取类的元类;   不断增加,最后会获取type
    - type(classname, parentClasses, attrs)
    - type("newClassName", (), {})
        - 创建名称为 className, 继承parentClasses, 具有属性attrs的类
        - 类名称:最后返回实例类的名称
        - 父类:
        - 类属性
    
    - type.__new__(cls, className, bases, attrs)
        - 使用cls元类,创建名称为 className, 继承bases, 具有attrs属性的类
        - cls是元类, 是type or type的子类
    
"""


# Flask 的 views.py 包内
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""

    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instantiation that replaces
    # itself with the actual metaclass.
    class metaclass(type):
        def __init__(cls, name, this_bases, d):
            print("========================                metaclass __init__")
            super().__init__(name, this_bases, d)

        def __new__(metacls, name, this_bases, d):
            print("========================                metaclass __new__")
            return meta(name, bases, d)  # 调用了 meta的 __init__ 方法

    return type.__new__(metaclass, "temporary_class", (), {})  # 只是调用 __new__ 方法


class A:
    def add(self, x):
        return 10 + x


class B(type):
    """元类添加的属性,子类无法继承"""

    def __init__(cls, name, bases, d):
        print("==================  B  __init__ ")
        super().__init__(name, bases, d)


class C(with_metaclass(B, A)):  # C 继承metaclass, 这儿, 元类metaclass被实例化,调用了 __new__方法
    name = "B"


print("C.__bases__: \n", C.__bases__)
# 利用type, __class__ 查询类的继承关系: C -> B -> Type
# 元类的继承关系
print("type(C): \n", type(C), type(type(C)))
# mro: 显示类的继承关系: C -> A -> object
# 非元类的继承关系
print("C.mro(): \n", C.mro())
print("C.__mro__: \n", C.__mro__)

c = C()
print(c.add(10))
print(c.__class__)
print(c.__class__.__class__)
print(c.__class__.__class__.__class__)
# 实例继承关系: c C B type
print(type(c), type(type(c)), type(type(type(c))))

# print(type(c)())
"""
===========================================================================================================
with_metaclass 的作用
===========================================================================================================
"""
print("\n========================= \n"
      "with_metaclass 作用探究\n"
      "========================= \n")
d = with_metaclass(B, A)
print(dir(d))
print(d.mro())
print(d.__class__, d.__class__.__class__)
print(type(d), type(type(d)))
print(with_metaclass(B))


class D:
    name = "D"

# print(D.mro())
# print(D.__mro__)
