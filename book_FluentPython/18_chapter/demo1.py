import threading
import itertools
import time
import sys

"""
代码来源： spinner_thread.py 
TIP:
    - 必须使用终端运行： python demo1.py,才能看到动画，因为其中调用的 sys.stdout指的是系统终端输出

"""


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush  # 获取系统输出的函数
    for char in itertools.cycle('|/-\\'):  # itertools.cycle 循环调用传入的可迭代对象
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # TODO \x08 退格符，移动光标回到初始位置
        time.sleep(0.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()  # TODO 信号，用来终止线程内的循环
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    spinner.start()
    result = slow_function()  # 模拟CPU密集型计算任务，耗时长
    signal.go = False  # 终止子线程的循环
    spinner.join()  # 阻塞线程，等待线程结束
    return result


if __name__ == '__main__':
    res = supervisor()
    print("result: ", res)
    pass
