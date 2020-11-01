# -*- coding: utf-8 -*-
# @Time : 2020/11/1
# @Author : Benny Jane
# @Email : 暂无
# @File : demo-1.py
# @Project : Learning_Py_World
import importlib

import_string = 'from otherPart import name'

module = __import__('otherPart.name', fromlist=('name'), level=0)
print(module)
print(module.name)


# print(module.init_name)
# print(module._private_name)

# print(module.__getattribute__('init_name'))

def run():
    exec(import_string, globals())
    print(name)


# run()

target_name = 'otherPart.name'

target = importlib.import_module(target_name)
target.add(10, 20)

