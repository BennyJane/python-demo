# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 19:40
# Warning    ：The Hard Way Is Easier
import os
import time
import random

from multiprocessing import Process
from multiprocessing import Pool

"""
进程池：
进程池内部维护一个进程序列，当需要使用时，就到进程池中去获取进程，
如果进程池序列中没有可以供使用的进程池，
那么就阻塞，等待进程池中有可用的进程

进程池中的调用方法：
apply: 同步，一般不使用
apply_async: 异步
"""


def task(name: int):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def process_pools(n: int):
    pools = Pool(n)
    for i in range(10):
        pools.apply_async(task, args=(i,))  # 异步不阻塞

    print("主进程...")
    # .close .join 依序调用
    pools.close()  # 调用close后，不能再继续添加新的process
    pools.join()  # 阻塞等待所有子进程执行完毕
    print("end ....")


if __name__ == '__main__':
    process_pools(8)
