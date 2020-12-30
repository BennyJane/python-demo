# -*- coding: utf-8 -*-
# @Time : 2020/10/27
# @Author : Benny Jane
# @Email : 暂无
# @File : example.py
# @Project : Learning_Py_World
import abc
import queue
import threading
import time

'''
使用线程安全的队列实现多线程，主要解决I/O密集型任务
'''


# 定义抽象类
class ThreadingMeta(abc.ABC):
    # 子进程数量，该类变量主要用于发送终止信号; 确保该值 >= 实际进程数
    # 设置该值也是为了在父类中调用时，不会报错
    concurrency = 100

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

    def setTimeout(self, timeout):
        last_time = now_time = 0
        while True and (now_time - last_time) < timeout:  # 超时退出
            jobs_num = self.jobs.qsize()  # 获取任务列表的长度
            if jobs_num == 0 and last_time == 0:
                last_time = time.time()
            elif jobs_num == 0 and last_time != 0:
                now_time = time.time()
            else:
                last_time = now_time = 0
        self.send_stop_signal()
        print('发送终止进程信号')

    def send_stop_signal(self):
        print("self.concurrency: 实际取子类实例化传入的值", self.concurrency)
        res = [(self.stop_signal,) for _ in range(self.concurrency)]
        self.add_jobs(res)

    def isTimeout(self, timeout):
        if timeout is not None:
            thr = threading.Thread(target=self.setTimeout, args=(timeout,))
            # thr.daemon = True  # 没有必要设置为守护进程， 该任务非死循环
            thr.start()


class MultiAndAsync(ThreadingMeta):
    def __init__(self, task, concurrency: int, daemon=False, timeout=None):
        super(MultiAndAsync, self).__init__()
        self.task = task  # 核心任务函数
        self.concurrency = concurrency  # 线程数量
        self.timeout = timeout  # 设置阻塞时间，用来等待添加任务； 默认1h
        self.daemon = daemon

    def run(self):
        self.isTimeout(self.timeout)  # 使用单独的进程，监控任务队列长度； 当任务为零的状态超过设置的时间后，将终止所有子进程
        self.create_threads()
        print("进程已经启动")

    def create_threads(self):
        for _ in range(self.concurrency):
            thr = threading.Thread(target=self.worker)
            thr.daemon = self.daemon  # 是否设置为守护进程
            thr.start()

    def worker(self):
        while True:
            try:
                # 当队列为空的时候， 会在此处阻塞  todo 如何在这里捕获超时异常
                params = self.jobs.get()
                if params[0] == self.stop_signal:  # 接收终止信号，停止运行
                    break
                result = self.task(*params)
                self.results.put(result)  # 将任务执行结果存储起来
            except Exception as e:
                print(e)
            finally:
                self.jobs.task_done()


def simple(num):  # 模拟阻塞任务， 休息时间一定要设置在print前
    time.sleep(2)
    print(num)
    return num


def test1(data):
    # 测试守护进程 ==》 主程序结束后，立即结束子进程， 子进程来不及执行
    queueThreading = MultiAndAsync(simple, concurrency=16, daemon=True)
    queueThreading.add_jobs(set(data))
    queueThreading.run()
    print("主程序已经执行完毕")


def test2(data):
    # 不设置过期时间；非守护进程
    queueThreading = MultiAndAsync(simple, concurrency=16)
    queueThreading.add_jobs(set(data))
    queueThreading.run()
    print("主程序已经执行完毕")


def test3(data):
    # 不设置过期时间；非守护进程
    queueThreading = MultiAndAsync(simple, concurrency=16, timeout=5)
    queueThreading.add_jobs(set(data))
    queueThreading.run()
    print("主程序已经执行完毕")

    time.sleep(10)
    print('再次添加数据')
    queueThreading.add_jobs(set(data))


if __name__ == '__main__':
    data = [(i,) for i in range(20)]
    # 主程序结束后，立即结束子进程， 子进程来不及执行
    # test1(data)

    # 主程序率先执行完毕，所有任务被执行； 但 子进程最后处于阻塞状态，始终在等待获取任务，进程没有终止
    # test2(data)

    # 第一次添加的任务全部被执行，超过过期时间后，所有子进程被通知终止运行； 第二次添加的任务没有被处理
    test3(data)
