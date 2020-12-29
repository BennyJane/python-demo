# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 14:15
# Warning    ：The Hard Way Is Easier
from contextlib import contextmanager


@contextmanager
def generator(name):
    try:
        yield name
    except Exception as e:
        pass
    finally:
        pass


with generator("benny   ") as f:
    name = f.strip()
    print(name + " jane")
    # raise KeyError("this a error")

if __name__ == '__main__':
    pass
