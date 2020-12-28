# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 15:21
# Warning    ：The Hard Way Is Easier

n = 1.33335855

# %.nf  n表示保留几位小数， n过大，补0
a = "%.5f" % 1.3335
print(a)

b = round(n, 5)
print(b)

import sys

print(sys.argv)

