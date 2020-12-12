# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/11 16:03
# Warning    ：The Hard Way Is Easier
import sys, socket

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.executors.pool import ProcessPoolExecutor
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask

app = Flask(__name__)

JOB_EXECUTORS = {
    "default": ThreadPoolExecutor(10),  # 设置一个名为 default的线程池执行器， 最大线程设置为20个
    # TODO 线程过多，会出现同一个任务被多次执行的情况
    "processpool": ProcessPoolExecutor(4),  # 设置一个名为 processpool的进程池执行器，最大进程数设为5个
}


def timed_task():
    print("run task...")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


scheduler = BlockingScheduler(executors=JOB_EXECUTORS, timezone="Asia/Shanghai")
scheduler.add_job(timed_task, trigger='interval', seconds=5)


def way_first():
    """success"""
    # gunicorn app:app -w 4 --preload
    # 不添加 --preload，会抛出进程终止异常(worker timeout,worker exit，然后重启进程)，然后部分任务执行失败
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 47200))
    except socket.error:
        print("!!!scheduler already started, DO NOTHING")
    else:
        # 只有上传try中代码执行成功，才会执行该部分代码
        scheduler.start()
        print("scheduler started")


# way_first()

def way_second():
    """文件锁： 可以实现"""
    # gunicorn app:app -w 4 --preload
    import fcntl
    import atexit
    f = open("scheduler.lock", "wb")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        scheduler.start()
    except Exception as e:
        print(e)

    def unlock():
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()

    atexit.register(unlock)


way_second()

if __name__ == '__main__':
    app.run(debug=False)
