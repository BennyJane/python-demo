# -*- coding: utf-8 -*-
# @Time : 2020/10/31
# @Author : Benny Jane
# @Email : 暂无
# @File : demo-0.py
# @Project : Learning_Py_World

import signal, time


signal.alarm(3)

while True:
    time.sleep(1)
    print("working")