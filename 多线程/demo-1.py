# -*- coding: utf-8 -*-
# @Time : 2020/10/27
# @Author : Benny Jane
# @Email : 暂无
# @File : demo-1.py
# @Project : Learning_Py_World
import queue
import threading

'''
使用线程安全的队列实现多线程，主要解决I/O密集型任务

'''


class ThreadingOnQueue(object):
    def __init__(self, task_func, data, concurrency):
        self.task = task_func  # 核心任务函数
        self.concurrency = concurrency  # 线程数量
        self.data = data  # 函数参数； 可迭代对象
        # 线程安全的队列
        self.jobs = queue.Queue()  # 任务队列
        self.results = queue.Queue()  # 存储结果

    def main(self):
        # 线程安全的队列
        print("=== start ===")
        self.create_threads()
        self.add_jobs()
        # self.process()
        pass




    def create_threads(self):
        for _ in range(self.concurrency):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True  # 设置为守护进程，主进程结束后，子进程也结束
            thread.start()  # 进入阻塞；等待获取任务

    def worker(self):
        while True:
            try:
                params = self.jobs.get()
                result = self.task(*params)
                # TODO 根据结果输出日志
                self.results.put(result)  # 将任务执行结果存储起来
            except Exception as e:
                print(e)
            finally:
                self.jobs.task_done()

    def add_jobs(self):
        # 想队列中添加数据
        for index, item in enumerate(self.data, start=1):
            self.jobs.put(item)
            # TODO 日志输出
        return index

    def process(self):
        # canceled 记录是否使用 ctrl+c 终止程序
        canceled = False
        try:
            # 等待所有任务结束
            self.jobs.join()
        except KeyboardInterrupt:  # windows可能会出bug
            canceled = True
        # todo 输出任务结束日志
        print('=====  e   =====')

    def output(self):
        # TODO 根据 results，将任务执行结果统计输出
        pass


def simple(num):
    print(num)
    return num


if __name__ == '__main__':
    data = [(i, ) for i in range(20)]
    queueThreading = ThreadingOnQueue(simple, data, concurrency=3)
    queueThreading.main()
