# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 19:51
# Warning    ：The Hard Way Is Easier
import os
import time
import random
from multiprocessing import Pool

"""
进程池 map 方法：
参数:
    - 函数
    - 参数组成的可迭代对象
实现多进程执行任务。
"""


def task(name):
    time.sleep(random.randint(1, 5))
    print("处理事务：CPU/IO密集{}".format(name))

    return f"进程id:{os.getpid()}; 事务：{name}"


def process_map(n):
    pools = Pool(n)
    print("start ...")
    result = pools.map(task, [i for i in range(10)])  # TODO 阻塞
    print("执行结果", result)
    print("running ...")
    # pools.close()
    # pools.join()
    print("end ...")


if __name__ == '__main__':
    process_number = 5
    process_map(process_number)
