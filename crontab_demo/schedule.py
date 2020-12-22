from threading import Timer
import psutil
import time
import datetime


def MonitorSystem(logfile=None):
    cpuper = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    memper = mem.percent
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print(line)
    if logfile:
        logfile.write(line)
    # 启动定时器任务，每三秒执行一次
    Timer(3, MonitorSystem).start()


def MonitorNetWork(logfile=None):
    netinfo = psutil.net_io_counters()
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} bytessent={netinfo.bytes_sent}, bytesrecv={netinfo.bytes_recv}'
    print(line)
    if logfile:
        logfile.write(line)
    # 启动定时器任务，每秒执行一次
    Timer(1, MonitorNetWork).start()


MonitorSystem()
# MonitorNetWork()
