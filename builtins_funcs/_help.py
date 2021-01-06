# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import os

"""
help: 显示对象的文档注释
__doc__: 对象的文档注释；第一行内容
"""

name = "benny"


# print(help(name))


def f():
    """this is a simple func"""
    name = "benny"
    return name


class A:
    def get_name(self):
        """this is a method..."""
        return "jane"


if __name__ == '__main__':
    help(f)
    help(A)
    help(name)
    print(A.__weakref__)
    # help(os)
