# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 18:28
# Warning    ：The Hard Way Is Easier
from multiprocessing import Manager
from multiprocessing import Process

"""
进程之间的数据共享： 允许一个进程去修改另一个进程数据
Manager
使用Manager提供的字典与列表，可以在子进程中，添加与修改字典、列表的内容；
实现多进程之间的数据共享，即可以共同修改同一份数据
"""


def task(d: dict, l: list, index: int):
    d[index] = "a"
    d["2"] = "b"
    l.append(index)


def process_manager():
    with Manager() as manager:
        d = manager.dict()  # TODO 必须使用Manager提供的字典与列表，普通字典不行
        l = manager.list([])  # 可以设置默认列表

        process_list = []
        for i in range(10):
            p = Process(target=task, args=(d, l, i))
            p.start()
            process_list.append(p)

        for res in process_list:
            res.join()
        print(d)
        print(l)


if __name__ == '__main__':
    process_manager()
