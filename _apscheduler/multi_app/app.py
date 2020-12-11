# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/11 16:03
# Warning    ：The Hard Way Is Easier
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
scheduler.add_job(timed_task, trigger='interval', seconds=10)

scheduler.start()
if __name__ == '__main__':
    app.run(debug=False)
