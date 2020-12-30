# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 23:38
# Warning    ：The Hard Way Is Easier

from private_public.module_private import *
from private_public.module_private import __all__ as module__all__

# print("globals ", globals().keys())
# print("before")
# print(globals())
# globals()
# print("after")


if "_private" in globals().keys():
    print("True")

print("module.__all__", module__all__)

# print("end")
if __name__ == '__main__':
    # TODO locals globals 都会导致模块中代码被执行了两遍； 甚至从其他模块导入的locals() globals() 都会被执行两次
    # print("locals ", locals().keys())
    # print("globals： ", globals().keys())
    pass
