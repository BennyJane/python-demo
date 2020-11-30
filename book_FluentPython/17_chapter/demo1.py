import os
import time
import sys

import requests
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

"""
TIP:
("example") 与 ("example", )：
    - 前者类型仍然是字符串（已经使用type验证）
        - ()圆括号可以理解为元组， 然后解包的操作
        - ()生成器表达式
    - 后者是元组

多进程中map()函数：
    - 调用顺序决定了结果返回顺序； 返回顺序一定按照调用顺序来的

"""
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()
print(type(POP20_CC))

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = './downloads'  # . 表示当前目录

MAX_THREADS = 20  # 最大线程数
MAX_PROCESS = os.cpu_count()  # 最大线程数


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:  # 写入二进制文件
        fp.write(img)  # 写入文件


def get_flag(name):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=name.lower())
    resp = requests.get(url)
    return resp.content  # 请求的图片文件是二进制的


def show(text):
    print(text, end=" ")  # 设置多次打印的间隔是tab，而不是换行
    sys.stdout.flush()  # 及时刷新终端输出


def download_one(name):  # TODO 提供给线程处理的操作
    img = get_flag(name)
    show(name)
    save_flag(img, filename=name.lower() + '.gif')
    return name


# 多线程下载
def download_many_threads(targets: list):
    threading_count = min(MAX_THREADS, len(targets))  # 获取线程数，避免线程浪费
    # ThreadPoolExecutor继承的Executor类，实现了 __enter__ __exit__方法，所以可以使用with语法
    # ThreadPoolExecutor实例调用__exit__方法，其实调用self.shutdown(wait=True),会阻塞，直到所有线程都执行完毕
    with futures.ThreadPoolExecutor(threading_count) as executor:  # TODO 核心：开启多线程，获取线程句柄
        # 调用map方法， 返回生成器对象(迭代器)，可通过迭代获取各个函数的返回值  ——》源码： 返回一个被调用的闭包函数（该闭包函数是生成器函数）
        # download_one: 在多线程中并发调用（非并行）
        res = executor.map(download_one, sorted(targets))
    return len(list(res))


# 多线程： 步骤拆分
def download_many_threads_multi_step(targets: list):
    thread_count = min(MAX_THREADS, len(targets))
    """多线程分成两步：
    1. 开多线程，调用submit()方法，床架Future实例
    2. 通过concurrent.futures.as_completed() 传入Future实例列表，返回生成器，迭代获取执行结果
    """
    with ThreadPoolExecutor(thread_count) as executor:
        to_do = []  # 存储future实例
        for name in sorted(POP20_CC):
            # TODO 创建期物： Future实例
            future = executor.submit(download_one, name)  # 调用实例的submit方法，返回Future（期物）实例
            to_do.append(future)
            msg = "Scheduled for {}:{}"
            print(msg.format(name, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


# 多进程执行
def download_many_process(targets: list):
    # futures.ProcessPoolExecutor的max_workers 默认为本机的CPU数量
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(targets))

    return len(list(res))


if __name__ == '__main__':
    download_many_threads(POP20_CC)
    pass
