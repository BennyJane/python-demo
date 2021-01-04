# -*- coding: utf-8 -*-
# @Time : 2020/10/27
# @Author : Benny Jane
# @Email : 暂无
# @File : asyncio_example.py
# @Project : Learning_Py_World
import queue
import threading
import time

'''
使用线程安全的队列实现多线程，主要解决I/O密集型任务
asynchronous 异步
block 阻塞
'''


class ThreadingOnQueue(object):
    def __init__(self, task_func, concurrency):
        self.task = task_func  # 核心任务函数
        self.concurrency = concurrency  # 线程数量
        # 线程安全的队列
        self.jobs = queue.Queue()  # 任务队列
        self.results = queue.Queue()  # 存储结果

    def MultiAndBlock(self):  # 主程序实现子进程内函数的并发， 但主程序会阻塞，等待子进程中任务结束，所以是同步执行
        # 该方法会启动多线程，但主程序会阻塞，直到所有子进程执行完，才会往下执行
        self.create_threads(self.worker)
        self.process()  # 此处阻塞，等待所有子程序执行结束后，再往下执行

    def create_threads(self, worker_func):
        for _ in range(self.concurrency):
            thread = threading.Thread(target=worker_func)
            thread.daemon = True  # 设置为守护进程，主进程结束后，子进程也结束
            thread.start()  # 进入阻塞；等待获取任务

    def worker(self):
        # 死循环，只适用于守护进程条件下适用：主进程结束后，子进程也会终止执行
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

    def add_jobs(self, push_data: tuple):
        # 函数参数； 可迭代对象
        # 想队列中添加数据
        for index, item in enumerate(push_data, start=1):
            self.jobs.put(item)
            # TODO 日志输出
        return index

    def process(self):
        try:
            # 等待所有任务结束
            self.jobs.join()
        except KeyboardInterrupt:  # windows可能会出bug； 是否使用 ctrl+c 终止程序
            print("强制终止程序")
        print('=====  end   =====')

    def output(self):
        # TODO 根据 results，将任务执行结果统计输出
        pass


def simple(num):
    print(num)
    time.sleep(1)
    return num


if __name__ == '__main__':
    data = [(i,) for i in range(20)]
    queueThreading = ThreadingOnQueue(simple, concurrency=16)
    queueThreading.add_jobs(set(data))
    queueThreading.MultiAndBlock()
    print("====== ending")
