# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 15:34
# Warning    ：The Hard Way Is Easier
import os
import time
from threading import Thread
from multiprocessing import Process


def test_multi_process(func):
    cpu = os.cpu_count()
    print("cpu数量： ", cpu)
    for i in range(cpu):
        p = Process(target=func, args=())
        p.start()
    # time.sleep(120)


def test_multi_thread(func):
    cpu = os.cpu_count()
    for i in range(cpu):  # 和cpu数量没有关系
        t = Thread(target=func, args=())
        t.start()
    time.sleep(120)
