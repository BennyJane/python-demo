# -*- coding: utf-8 -*-
# @Time : 2020/10/27
# @Author : Benny Jane
# @Email : 暂无
# @File : demo1.py
# @Project : Learning_Py_World
import abc
import queue
import threading
import time
from queue import Empty


# 定义抽象类
class ThreadingMeta(abc.ABC):
    def __init__(self):
        # 线程安全的队列
        self.jobs = queue.Queue()  # 任务队列
        self.results = queue.Queue()  # 存储结果
        self.stop_signal = 'stop'

    @abc.abstractmethod
    def run(self):
        """运行多线程任务"""

    @abc.abstractmethod
    def create_threads(self):
        """创建多进程"""

    @abc.abstractmethod
    def worker(self):
        """进程执行的任务函数"""

    def add_jobs(self, push_data: tuple):
        # 函数参数； 可迭代对象
        # 想队列中添加数据
        for item in push_data:
            self.jobs.put(item)


class MultiAndAsync(ThreadingMeta):
    def __init__(self, task, concurrency: int, timeout=None):
        super(MultiAndAsync, self).__init__()
        self.task = task  # 核心任务函数
        self.concurrency = concurrency  # 线程数量
        self.timeout = timeout  # 设置阻塞时间，用来等待添加任务； 默认为None，子进程会一直阻塞在获取任务的步骤

    def run(self):
        self.create_threads()
        print("进程已经启动")

    def create_threads(self):
        for _ in range(self.concurrency):
            thr = threading.Thread(target=self.worker)
            # todo 这里不能设置为守护进程,因为主线程不阻塞
            # thr.daemon = self.daemon
            thr.start()

    def worker(self):
        while True:
            try:
                # 当队列为空, block=True, 会在此处阻塞,
                # 设置timeout, 设置阻塞超时时间
                params = self.jobs.get(block=True, timeout=self.timeout)
                result = self.task(*params)
                self.results.put(result)  # 将任务执行结果存储起来
            except Empty:
                # queue 内定义了Empty异常类，但该类为空，没有定义任何提示信息
                print("The threading is timeout!")
                break
            except Exception as e:
                print(e)
                # 当进程执行异常不是 Empty的时候，一定会执行 self.jobs.task_done()
                self.jobs.task_done()
            self.jobs.task_done()


def simple(num):  # 模拟阻塞任务， 休息时间一定要设置在print前
    time.sleep(4)
    print(num)
    return num


def test1(data):
    # 测试守护进程 ==》 主程序结束后，立即结束子线程， 子线程来不及执行
    queueThreading = MultiAndAsync(simple, concurrency=16, daemon=True, timeout=3)
    queueThreading.add_jobs(set(data))
    queueThreading.run()
    print("主程序已经执行完毕")

    # 启动16个线程，第一次添加了10个任务，有6个线程没有获取任务，3秒后捕获超时异常退出；
    # 10个线程执行完领取的任务花费大约4秒，然后进入3秒的等待时间，
    # 3秒内再次获取任务，就会执行，否则退出
    # 因此，所有在7秒后添加的任务都不会被执行，因为所有子线程都已经终止运行了
    time.sleep(7)
    print('再次添加数据')
    second_data = [(i,) for i in range(10, 20)]
    queueThreading.add_jobs(set(second_data))


if __name__ == '__main__':
    data = [(i,) for i in range(10)]
    # 主程序结束后，立即结束子线程， 子线程来不及执行
    test1(data)
