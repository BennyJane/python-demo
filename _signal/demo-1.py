# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/24 23:55
# Warning    ：The Hard Way Is Easier


import signal, time

signal.alarm(3)

while True:
    time.sleep(1)
    print("working")
