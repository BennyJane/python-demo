# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 23:38
# Warning    ：The Hard Way Is Easier

__all__ = ["public", "__private_in_all"]

_private = "module: _private"
__private = "module: __private"
__private_in_all = "module: __private_in_all"

public = "module: public"
public_not_in_all = "module: public_not_in_all"

print("module: ", globals().keys())

if __name__ == '__main__':
    print(globals().keys())
