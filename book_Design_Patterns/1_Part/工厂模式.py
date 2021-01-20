# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

import logging


class A:
    def __init__(self, *arg):
        self.arg = arg

    @property
    def common(self):
        return "result of A"


class B:
    def __init__(self, *arg):
        self.arg = arg

    @property
    def common(self):
        return "result of B"


def standard_factory(*arg):
    if arg[0].startswith("A"):
        target_obj = A(*arg)
    elif arg[0].startswith("B"):
        target_obj = B(*arg)
    else:
        raise Exception('没有找到相应的对象')
    return target_obj


def final_factory(*arg):
    factory = None
    try:
        factory = standard_factory(*arg)
    except Exception as e:
        logging.error(e)
    return factory


if __name__ == '__main__':
    res = final_factory("A")
    print(res.common)