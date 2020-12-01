import threading
import itertools
import time
import sys

"""
代码来源： spinner_thread.py 
TIP:
    - 改进demo1.py: 使用Event代替自定义的信号
:
"""


def spin(msg, done):
    write, flush = sys.stdout.write, sys.stdout.flush  # 获取系统输出的函数
    for char in itertools.cycle('|/-\\'):  # itertools.cycle 循环调用传入的可迭代对象
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # TODO \x08 退格符，移动光标回到初始位置
        # 修改下面时间，可以调整动画刷新的速度
        if done.wait(.1):  # 阻塞0.1秒(不设置时间，将会一直阻塞)； 但只有被通知后，才会执行break
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    done = threading.Event()  # TODO 信号，用来终止线程内的循环
    spinner = threading.Thread(target=spin, args=('thinking!', done))
    spinner.start()
    result = slow_function()  # 模拟CPU密集型计算任务，耗时长
    done.set()  # 修改信号的状态，终止spin内的循环
    spinner.join()  # 阻塞线程，等待线程结束
    return result


if __name__ == '__main__':
    res = supervisor()
    print("result: ", res)
    pass
