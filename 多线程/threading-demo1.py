# -*- coding: utf-8 -*-
import sys
import threading
import time


class Dispacher(threading.Thread):
    def __init__(self, func, args):
        super(Dispacher, self).__init__()
        self.setDaemon(True)
        self.func = func
        self.args = args
        self.error = None
        self.result = None

        # 初始化的时候，就直接运行线程
        self.start()

    def run(self):
        try:
            self.result = self.func(self.args)
        except:
            self.error = sys.exc_info()


def task(i):
    time.sleep(4)
    print(f"task{i} is done!")
    return i * 2


if __name__ == '__main__':
    index = 1
    timeout = 2
    thr = Dispacher(task, index)
    thr.join(timeout)  # 主线程只阻塞2秒钟，2秒后，继续往下执行，

    # 如果子线程中任务并没有执行完毕； 主线程也还未结束，所以后台还会继续执行子线程任务
    if thr.is_alive():
        # 在调用thr.join(timeout)主动阻塞n秒后，仍然在执行的子线程，就是超时任务
        print("TimeoutError")
    elif thr.error:
        print(thr.error[1])
    res = thr.result
    print("[结果]: ", res)
