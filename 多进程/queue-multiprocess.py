# -*- coding: utf-8 -*-
# @Time : 2020/11/1
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Learning_Py_World
import abc
import multiprocessing
import time

import math


class MultiProcessMeta(abc.ABC):
    def __init__(self):
        self._jobs = multiprocessing.JoinableQueue()
        self._results = multiprocessing.Queue()

    @abc.abstractmethod
    def create_process(self):
        """创建多进程"""

    @abc.abstractmethod
    def run(self):
        """运行多进程"""

    @abc.abstractmethod
    def worker(self):
        """任务函数"""

    def add_jobs(self, params):
        """添加任务数据"""
        for item in params:
            self._jobs.put(item)


class ProcessOnQueue(MultiProcessMeta):

    def __init__(self, task, params, concurrency, timeout=None):
        super(ProcessOnQueue, self).__init__()
        self.task_func = task
        self.jobs_data = params
        self.concurrency = concurrency
        self.timeout = timeout

    def run(self):
        self.create_process()
        self.add_jobs(self.jobs_data)
        try:
            self._jobs.join()
        except KeyboardInterrupt:
            print("canceling...")

    def worker(self):
        while True:
            try:
                data = self._jobs.get(timeout=self.timeout)
                try:
                    self.task_func(data)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
                break
            finally:
                self._jobs.task_done()

    def create_process(self):
        for _ in range(self.concurrency):
            process = multiprocessing.Process(target=self.worker)
            process.daemon = True
            process.start()


def mathFunc(a):
    n = 0
    while n < 5:
        res = math.pi * a
        print(res)
        time.sleep(1)
        n += 1


if __name__ == '__main__':
    pro = ProcessOnQueue()
