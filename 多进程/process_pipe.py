# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 18:27
# Warning    ：The Hard Way Is Easier
import time
from multiprocessing import Process
from multiprocessing import Pipe

"""
进程间通信
管道：Pipe
实例化后，返回两个句柄，通过句柄实现主进程与子进程之间的通信
"""


def task(conn):
    time.sleep(5)
    print("子进程 begin running")
    conn.send("子进程.send： 01")
    recv_msg = conn.recv()  # TODO 接收消息：该方法会阻塞程序
    print("子进程接收到消息： {}".format(recv_msg))
    conn.close()
    print("子进程 end ...")


def process_func():
    conn1, conn2 = Pipe()  # 返回两个句柄
    p = Process(target=task, args=(conn2,))
    p.start()
    print("主进程等待接收消息...")
    msg = conn1.recv()  # TODO 接收消息：该方法会阻塞程序
    print("主进程接收到消息： {}".format(msg))
    conn1.send("主进程.send: 01")
    p.join()  # 阻塞：等待子进程执行完毕
    print("end ...")


if __name__ == '__main__':
    process_func()
