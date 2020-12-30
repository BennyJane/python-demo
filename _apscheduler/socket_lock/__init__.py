# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/11 16:03
# Warning    ：The Hard Way Is Easier
import os
from _apscheduler.base_scheduler import scheduler
from _apscheduler.multi_test import test_multi_thread
from _apscheduler.multi_test import test_multi_process


def socket_lock():
    """测试可以使用"""
    import socket
    pid = os.getpid()
    # gunicorn app:app -w 4 --preload
    # 不添加 --preload，会抛出进程终止异常(worker timeout,worker exit，然后重启进程)，然后部分任务执行失败
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 47200))
    except socket.error:
        print(f"端口已被占用， 进程({pid})不启动调度器")
        sock.close()
    else:
        # 只有上传try中代码执行成功，才会执行该部分代码
        # 确保只有一个进程启动调度器
        print(f"进程({pid})已经启动调度器")
        scheduler.start()


if __name__ == '__main__':
    # test_multi_process(socket_lock)
    test_multi_thread(socket_lock)
