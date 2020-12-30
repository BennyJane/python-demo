# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/8 23:02
# Warning    ：The Hard Way Is Easier
import time
import random
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from _apscheduler.example.config import job_default
from _apscheduler.example.config import job_stores
from _apscheduler.example.config import executors

# 使用redis存储任务
scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_default=job_default, timezone=utc)


def task1(x, y):
    s = x + y
    print(s)
    return s


def write_file():
    number = random.randint(0, 100)
    with open('record.txt', 'a') as f:
        f.write(f"random num: {number}\n")


scheduler.add_job(
    task1,
    trigger="cron",
    second='*/10',
    args=(10, 20)
)

scheduler.add_job(
    write_file,
    trigger="cron",
    second='*/5'
)

if __name__ == '__main__':
    scheduler.start()
    print("调度器状态", scheduler.state)
    print("调度器是否运行", scheduler.running)
    time.sleep(60)
