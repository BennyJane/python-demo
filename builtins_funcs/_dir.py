# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import os
import inspect
from pprint import pprint

# 获取模块的帮助文档
# help(os)

# os模块内具有很多属性与方法，使用一行代码打印os模块下所有的方法名称
# 参考文章： https://www.itranslater.com/qa/details/2110320005110825984

# pprint(dir(os))
print(dir(os))  # 输出模块内所有属性名称、方法名称

# 输出所有可调用对象（类、方法、实例(__call__))
print([f for f in dir(os) if callable(getattr(os, f))])

# 输出函数
# inspect.isfunction() 源码=> isinstance(object, types.FunctionType)
print([f for f in dir(os) if inspect.isfunction(getattr(os, f))])  # 失效

import types

print([f for f in dir(os) if isinstance(getattr(os, f), types.FunctionType)])

# 输出类方法
print([f for f in dir(os) if inspect.ismethod(getattr(os, f))])
