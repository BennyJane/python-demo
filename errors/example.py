# -*- coding: utf-8 -*-
# @Time : 2020/11/29
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
import os

print(os.getcwd())
"""
异常处理模块：


Python内置的异常类：
    AssertionError
    AttributeError
    Exception
    IndentationError
    IndexError
    IOError
    KeyError
    NameError
    OSError
    TabError
    SyntaxError
    SystemError
    TypeError
    ValueError
    ZeroDivisionError

"""


class CustomError(Exception):
    """自定义异常类"""

    def __init__(self, msg):
        self.err = msg

    def __str__(self):
        return "%s" % self.err


def Test():
    try:
        raise CustomError("错误信息")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    Test()
