# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/8 23:02
# Warning    ：The Hard Way Is Easier

global count


def task1(x, y):
    s = x + y
    print(s)
    return s


def write_file():
    count += 1
    with open('./record.txt', 'a') as f:
        f.write(f"count: {count}")
