# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/11 22:17
# Warning    ：The Hard Way Is Easier
import time
import random

from _apscheduler.mysql_lock.utils import single_task
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


@single_task
def task1(arg1, arg2):
    print("----------------------------------------------")
    print("开始执行task1")
    time.sleep(random.randint(1, 5))
    print("task1执行完成")
    print("----------------------------------------------" + "\n")
    return arg1 + arg2


def task2(arg1, arg2):
    print("----------------------------------------------")
    print("开始执行task2")
    time.sleep(random.randint(1, 5))
    print("task2执行完成")
    print("----------------------------------------------" + "\n")
    return arg1 * arg2


@single_task
def task3(arg1, arg2):
    print("----------------------------------------------")
    print("开始执行task2")
    time.sleep(random.randint(1, 5))
    print("task2执行完成")
    print("----------------------------------------------" + "\n")
    return arg1 / arg2


if __name__ == '__main__':
    executors = {
        "default": ThreadPoolExecutor(20),  # 设置一个名为 default的线程池执行器， 最大线程设置为20个
        "processpool": ProcessPoolExecutor(5),  # 设置一个名为 processpool的进程池执行器，最大进程数设为5个
    }
    print("开始执行定时任务")
    scheduler = BlockingScheduler(executors=executors, timezone="Asia/Shanghai")
    scheduler.add_job(task1, args=(5, 5), trigger="interval", seconds=5)
    scheduler.add_job(task2, args=(5, 5), trigger="interval", seconds=5)
    scheduler.add_job(task3, args=(5, 5), trigger="interval", seconds=5)
    scheduler.start()
