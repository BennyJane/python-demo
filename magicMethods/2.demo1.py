# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise
import abc


def __getattr__(self, item):
    """"""
    return lambda *args, **kwargs: None


class Base(abc.ABC):
    def __init__(self, *args, **kwargs):
        """"""

    def __getattr__(self, item):
        """处理属性找不到的情况"""
        return lambda *args, **kwargs: None  # 返回一个可以调用的对象


class Test1:
    def __new__(cls, *args, **kwargs):
        if args[0] == 'err' and len(args) > 0:
            tempClass = type("tempTest", (object,), {"__getattr__": __getattr__, 'tag': args[0]})
            return tempClass()
        return super().__new__(cls)

    def __init__(self, tag):
        self.tag = tag
        print(self.tag)
        print(self.__dict__)

    def print(self, text):
        print(text)

    def __getattr__(self, item):
        """"""
        return lambda *args, **kwargs: None


class Test3:
    def __new__(cls, *args, **kwargs):
        if args[0] == 'err' and len(args) > 0:
            return type("tempTest", (),
                        {"__getattr__": Test3.notFind, 'tag': args[0]})()
        return super().__new__(cls)

    def __init__(self, tag):
        self.tag = tag
        print(self.tag)
        print(self.__dict__)

    def print(self, text):
        print(text)

    @staticmethod
    def notFind(instance, name):
        """单用一个类，解决这个问题"""
        print('not find ...')
        return lambda *args, **kwargs: None


class Test2:
    def __new__(cls, *args, **kwargs):
        if args[0] == 'err':
            tempClass = type("tempTest", (Base,), {})
            return tempClass(*args, **kwargs)
        return super().__new__(cls)

    def __init__(self, tag):
        self.tag = tag

    def print(self, text):
        print(text)


class Test:
    def __new__(cls, *args, **kwargs):
        if args[0] == 'err':
            # 根据输入参数，返回了不同的类实例
            return type("tempTest", (Base,), {})(*args, **kwargs)
        return super().__new__(cls)

    def __init__(self, tag):
        self.tag = tag

    def print(self, text):
        print(text)


# todo 思考： 能不能直接继承test类，而不用重新定义新的基类
if __name__ == '__main__':
    Test('good').print('12345')
    Test('err').print('123456')  # 怎么让这句执行正确?
    res = Test('err')

    Test3('good').print('12345')
    Test3('err').print('123456')  # 怎么让这句执行正确?
    res = Test3('err')

    # res = test('good')
    # print(test.__dict__)
    # print(res.__dict__)
    # print(dir(res))
    # print(dir(test))
