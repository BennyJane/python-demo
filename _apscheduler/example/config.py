# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/8 23:02
# Warning    ：The Hard Way Is Easier
from apscheduler.jobstores.redis import RedisJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

job_stores = {
    "redis": RedisJobStore(),  # 设置一个名为redis的job存储，后端使用 redis
    # 一个名为 default 的 job 存储，后端使用数据库（使用 Sqlite）
    # "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}

executors = {
    "default": ThreadPoolExecutor(20),  # 设置一个名为 default的线程池执行器， 最大线程设置为20个
    "processpool": ProcessPoolExecutor(5),  # 设置一个名为 processpool的进程池执行器，最大进程数设为5个
}

# 开启job合并，设置job最大实例上限为3
job_default = {
    'coalesce': False,
    'max_instances': 3
}
