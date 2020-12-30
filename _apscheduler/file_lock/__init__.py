# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 15:14
# Warning    ：The Hard Way Is Easier
from _apscheduler.base_scheduler import scheduler
from _apscheduler.multi_test import test_multi_thread
from _apscheduler.multi_test import test_multi_process


def file_lock():
    """文件锁： 可以实现; linux上测试"""
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


if __name__ == '__main__':
    # test_multi_process(file_lock)
    test_multi_thread(file_lock)
