# -*- coding: utf-8 -*-
# @Time : 2020/10/27
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Learning_Py_World
import concurrent.futures
import multiprocessing
import sys

if sys.version_info < (3, 2):
    print("requires Python 3.2+ for concurrent.futures")
    sys.exit(1)


# todo 优化日志输出

class ThreadingOnFeatures(object):
    def __init__(self, task_func, concurrency):
        self.task = task_func  # 核心任务函数
        # 线程数量
        self.concurrency = concurrency if concurrency else multiprocessing.cpu_count() * 4
        self.futures_container = set()  # 存储feature的执行对象
        # 修改为描述符
        self.__params_tuple = []
        self.__canceled = False  # canceled 记录是否使用 ctrl+c 终止程序
        self.__results = []
        self.__done = 0

    def main(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.concurrency) as executor:
            for param in self.__params_tuple:
                future = executor.submit(self.task, param)
                self.futures_container.add(future)
            self.process()
            if self.__canceled:
                executor.shutdown()

    def process(self):

        self.wait_for()
        if self.__canceled:
            for _ in (result for ok, result in self.__results if ok and result is not None):
                self.__done += 1
                # todo 添加结果处理与展示的代码 ==》可以提供另一个封装的接口
        else:
            self.__done = sum(1 for ok, result in self.__results if ok and result is not
                              None)

    def wait_for(self):
        try:
            for future in concurrent.futures.as_completed(self.futures_container):
                err = future.exception()
                if err is None:
                    ok, result = future.result()
                    if not ok:
                        print(result)
                    elif result is not None:
                        print(result)
                    self.__results.append((ok, result))

        except KeyboardInterrupt:
            self.__canceled = True
            for future in self.futures_container:
                future.cancel()

    def add_jobs(self, push_data):
        # 想队列中添加数据
        for _, item in enumerate(push_data, start=1):
            self.__params_tuple.append(item)
