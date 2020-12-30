# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 15:44
# Warning    ：The Hard Way Is Easier
from pytz import utc
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def timed_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("run task at {0}...".format(now))


scheduler = BackgroundScheduler(timezone=utc)
scheduler.add_job(timed_task, trigger='interval', seconds=5)
