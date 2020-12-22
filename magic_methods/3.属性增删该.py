# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class A(object):
    def __init__(self, name):
        self.name = name  # 调用 __setattr__ 方法

    def __getattr__(self, item):
        """处理异常：找不到属性时执行该方法"""
        print("=== 没有该属性：{} ===".format(item))
        return None

    def __getattribute__(self, item):
        print("==== __getattribute__ ====")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """需要避免死循环（循环调用）"""
        # self.__dict__[key] = value
        print("==== __setattr__ ====")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        print("==== __delattr__ ====")
        # del self.__dict__[item]
        object.__delattr__(self, item)


class B(object):
    def __init__(self, name):
        self.name = name  # 调用 __setattr__ 方法

    def __getattr__(self, item):
        """处理异常：找不到属性时执行该方法"""
        print("=== 没有该属性：{} ===".format(item))
        return None

    def __getattribute__(self, item):
        print("==== __getattribute__ ====")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """需要避免死循环（循环调用）"""
        print("==== __setattr__ ====")
        self.__dict__[key] = value

    def __delattr__(self, item):
        print("==== __delattr__ ====")
        del self.__dict__[item]


if __name__ == '__main__':
    # a = A("test")
    a = B("test")
    print(a.name)
    print(a.age)

    print("=================================================================================================")
    name_res = getattr(a, 'name', "None")
    print(name_res)

    print("=================================================================================================")
    age_res = getattr(a, 'age', "None")
    print(age_res)

    print("=================================================================================================")
    setattr(a, "age", 26)
    print(a.age)

    print("=================================================================================================")
    del a.age
    # print(a.age)

    print("=================================================================================================")
    delattr(a, 'name')

