# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/22 9:56
# Warning    ：The Hard Way Is Easier
import math
import typing

name = "benny jane"

mid = (11 + 12) // 2
print(mid, round(mid), math.ceil(mid))

mid = (11 + 11.8) / 2
print(mid, round(mid), math.ceil(mid))

if __name__ == '__main__':
    res = name.find("n")
    print(res)
