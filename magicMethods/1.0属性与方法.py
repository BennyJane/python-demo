# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

"""
函数:
getattr setattr delattr

上述函数对应的内部方法
__getattr__ __setattr__ __delattr__

函数: getattr

__getattribute__

描述器定义的方法:
__get__ __set__ __del__


__dict__ __dir__() dir()
vars()
globals()
locals()
"""


class A(object):
    name = "A"

    def __init__(self, site=None):
        self.site = site

    def work(self):
        self.work_name = "coder"
        return f"{self.name} is doing..."

    @property
    def pet(self):
        # FIXME 该属性并没有绑定到实例上，也没有绑定到类上；
        self.pet_name = "zsy"
        return "a pig"

    def __getattribute__(self, item):
        # 错误写法, 循环调用,超出递归深度
        # return self.__getattribute__(item)
        # return self.__dict__[item]
        print("====    __getattribute__  is called     =====")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return "error, not found"

    @staticmethod
    def run():
        print("running ...")

    @classmethod
    def eat(cls):
        print("eating ...")


a = A(site="shanghai")
"""
==================================================================================
getattr() 与　．　点属性方法对比
==================================================================================
"""
aSite = a.site
aWork = a.work
print(aWork())  # 调用实例(类方法)方法； 直接使用 a.work()
# getattr(obj, name) ==>　等效(源码注释)　　obj.name
print(getattr(a, 'site'))  # 获取实例属性
print(getattr(a, 'work'))  # 获取实例方法
print(getattr(a, 'name'))  # 在实例上，获取类属性；　
# print(getattr(A, 'site'))

print("===========================================================================")
# ================================================================================== #
"""
==================================================================================
对比实例与类的属性集合
==================================================================================
"""
print(a.__dir__)
# 先调用一次__getattribute__获取__dir__内建函数属性,再调用两次__getattribute__ 属性获取结果
# print(a.__dir__())
print(dir(a))
# print(dir())  # 空值，等效于 globals()  locals()
# print(dir(A))
#
print(["实例与类属性的差值"], set(dir(a)).difference(set(dir(A))))

print(a.__weakref__)
# print(A.__dir__())
setattr(a, "name", "a")  # 添加实例属性，不覆盖类同名属性，但类属性仍然存在
a.__setattr__("name", "c")  # 等效 setattr()
print(a.name)

print(a.__dict__)  # 仅仅获取实例的属性，不包含方法在内, 也不包含@property修饰的类
print(vars(a))  # vars() 实际调用__dict__; 只能处理有__dict__属性的类；仅仅获取实例的属性，包含其他动态绑定的属性，但不包含@property内绑定的属性

print(a.__dir__())
delattr(a, "name")
a.__delattr__("site")
print(a.name)
print(a.__dir__())

# fixme
print(a.pet_name)

"""
==================================================================================
对属性的增,删,查,改
==================================================================================
"""
# getattr()
# setattr()
# delattr()

# a.__setattr__("job", "actor")
# print(a.__dict__)
