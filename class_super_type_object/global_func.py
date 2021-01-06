# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
from pprint import pprint

print("this is a simple test!")

global_params = globals()


def f():
    res = globals().keys()
    return list(res)


# print(f()[0], "this is a function ")
# print(global_params.get("__name__"))
name = "benny"

if __name__ == '__main__':
    print("")
