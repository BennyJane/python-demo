# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/8 23:02
# Warning    ：The Hard Way Is Easier
import redis
import datetime
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from _apscheduler.config import job_default
from _apscheduler.config import job_stores
from _apscheduler.config import executors
from _apscheduler.tasks import task1
from _apscheduler.tasks import write_file

# scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_default=job_default, timezone=utc)
scheduler = BackgroundScheduler(timezone=utc)
scheduler.start()

scheduler.add_job(
    task1,
    trigger="cron",
    second='*/10',
    args=(10, 20)
)

scheduler.add_job(
    write_file,
    trigger="cron",
    second='*/30'
)
