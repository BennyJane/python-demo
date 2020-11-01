# -*- coding: utf-8 -*-
# @Time : 2020/11/1
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Learning_Py_World
import abc
import concurrent.futures
import multiprocessing

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
        self.concurrency = concurrency if concurrency else multiprocessing.cpu_count()
        self.timeout = timeout

    def run(self):
        self.create_process()  # 创建进程需要花费不少时间
        self.add_jobs(self.jobs_data)
        try:
            self._jobs.join()
            pass
        except KeyboardInterrupt:
            print("canceling...")

    def worker(self):
        while True:
            try:
                data = self._jobs.get(timeout=self.timeout)
                try:
                    self.task_func(*data)
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


class ProcessOnFutures(MultiProcessMeta):

    def __init__(self, task, params, concurrency, timeout):
        super().__init__()
        self.task_func = task
        self.jobs_data = params
        self.concurrency = concurrency if concurrency else multiprocessing.cpu_count()
        self.timeout = timeout
        self.futures = set()

    def run(self):
        self.create_process()
        self.run()

    def worker(self):
        pass

    def create_process(self):
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.concurrency) as executor:
            for item in self.get_jobs():
                future = executor.submit(self.task_func, item)
                self.futures.add(future)
            self.wait_for()

    def get_jobs(self):
        for item in self.jobs_data:
            yield item

    def wait_for(self):
        try:
            # futures.as_completed() 调用任务，持续阻塞，返回完成的任务
            for future in concurrent.futures.as_completed(self.futures):
                err = future.exception()
                if err is None:
                    result = future.result()
                else:
                    print(str(err))
        except KeyboardInterrupt:
            for future in self.futures:
                future.cancel()
            pass


def mathFunc(a):
    n = 0
    while n < 5:
        res = math.pi + a
        # print(res)
        # time.sleep(1)
        n += 1
    # print(res)


if __name__ == '__main__':
    data = [(i,) for i in range(30)]
    pro = ProcessOnQueue(mathFunc, data, concurrency=4)
    pro.run()

    # 直接执行几乎立即完成 ==》 多进程反而增加了时间
    # for i in range(30):
    #     mathFunc(i)
