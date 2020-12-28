# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 9:59
# Warning    ：The Hard Way Is Easier


class ClassParams:
    def __new__(cls, *args):
        return object.__new__(cls)

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    c = ClassParams("benny")

