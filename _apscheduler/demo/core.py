# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/8 23:02
# Warning    ：The Hard Way Is Easier
import redis
import time
import datetime
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from _apscheduler.demo.config import job_default
from _apscheduler.demo.config import job_stores
from _apscheduler.demo.config import executors
from _apscheduler.demo.tasks import task1
from _apscheduler.demo.tasks import write_file

# scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_default=job_default, timezone=utc)
scheduler = BackgroundScheduler(timezone=utc)
# scheduler = BlockingScheduler(timezone=utc)


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
    print(scheduler.state)
    print(scheduler.running)
    time.sleep(60)
