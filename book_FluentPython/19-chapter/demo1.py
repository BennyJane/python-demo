import threading
import itertools
import time
import sys
import json
import keyword
from collections import abc

"""
用类来解析一个json格式的数据
代码来源： example.py 

TIP:
    - 改进demo1.py: 使用Event代替自定义的信号
:
"""


def read_json():
    with open('./example.json', 'rb') as f:
        local_json = json.load(f)
    return local_json


class JsonConvertClass:
    def __init__(self, mapping):  # mapping： 非不可变类型数据，最好拷贝一份
        # print("--init__", mapping)
        # self.__data = dict(mapping)  # 复制原始数据
        self.__data = {}
        for key, value in mapping.items():  # 处理Python内置关键字的键
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):  # 处理实例对象找不到属性的情况
        # hasattr()：该方法用于获取对象的属性，无法从字典结构中获取键对应的值
        # 用于调用字典对象自身的方法： dict.keys() dict.items() 等等； 其他情况下不执行
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        # print("== not hasattr")
        # 当self.__data不是类对象,当做字典处理，获取键的值
        return JsonConvertClass.build(self.__data[name])  # 将当前__data内的一个键的值转为类对象，或者直接返回（非嵌套结构直接返回 ）

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)  # 字典类型，递归转化为 类对象
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]  # 返回实例的列表，只能通过下标获取对象
        else:
            # 非字典，列表的obj，直接返回； 其实就是最终获取的值 ==》 获取的非嵌套结构后，直接返回
            # 从内存的字典内获取键值后，直接返回，不需要实例化类
            return obj


"""
========================================================================================================================
example2.py
使用__new__方法，实现上面功能
========================================================================================================================
"""


class JsonConvertClass2:
    def __new__(cls, arg):  # __new__: 方法本身也是类方法
        if isinstance(arg, abc.Mapping):
            return object.__new__(cls)  # 类方法： 返回实例对象
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg  # 非类对象，不会进行后续实例化

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return JsonConvertClass2(self.__data[name])


if __name__ == '__main__':
    origin_data = read_json()
    res = JsonConvertClass(origin_data)
    print(res.Schedule.events[0].name)
    print(res.keys())
    # print(res.Schedule.events[0].serial)
    # print(res.Schedule.speakers[0].position)
    pass
