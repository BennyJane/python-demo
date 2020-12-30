# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 18:10
# Warning    ：The Hard Way Is Easier
import os
import time
from multiprocessing import Process


def task(name):
    pid = os.getpid()
    time.sleep(5)
    print(f"当前进程（{pid}）,父进程ID:{os.getppid()}, 任务名称：{name}")


def process_func1():
    process_list = []
    for i in range(os.cpu_count()):
        p = Process(target=task, args=(f"Python{i}",))
        p.start()
        process_list.append(p)
    # 阻塞：等待任务执行结束
    # for i in process_list:
    #     p.join()


"""
使用类实现进程
"""


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        """重写run方法，添加待执行的任务"""
        pid = os.getpid()
        print(f"class: 当前进程（{pid}）, 父进程({os.getppid()}), 任务名称：{self.name}")
        time.sleep(1)


def process_func2():
    process_list = []
    for i in range(os.cpu_count()):
        p = MyProcess(f"Class:Process{i}")
        p.start()  # FIXME 不是调用run方法
        process_list.append(p)
    # 阻塞：等待任务执行结束
    for i in process_list:
        p.join()


if __name__ == '__main__':
    process_func1()
    process_func2()
    print("end...")
