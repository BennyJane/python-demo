# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import time
import functools
import asyncio

"""
Coroutine
协程： 交给 asyncio 执行的任务
一个协程可以放弃执行，把机会让给其他协程，通过 yield form 或者 await ==> 本质：协程调度，协程切换

协程可以完成的任务：
- 等待一个future 结束
- 等待另一个协程（产生结果，或引发一个异常）
- 产生一个结果给在等它的协程
- 产生一个异常给正在等它的协程

调用协程函数，并不会直接运行，而是返回一个协程对象。

运行协程的两个方法：
- 在另一个已经运行的协程中使用 `await`等待它
- 通过 `ensure_future`函数计划它的执行
其实，只有loop运行了，协程才会运行

loop = asyncio.get_event_loop()
loop.run_until_complete()
    - 参数必须是future,但传入协程后，会先判断其不是future，然后将其转化为future
    - 内部调用函数 asyncio.ensure_future(coroutine_func())
"""


async def do_work(x):  # 协程函数
    print("do work before...")
    print("sleep %d" % x)
    await asyncio.sleep(x)  # asyncio.sleep也是一个协程
    print("do work end...")


def done_callback(future):  # 至少需要接受一个参数，该函数会被绑定为对象方法
    print("done callback ...")


def test_coroutine():
    assert asyncio.iscoroutinefunction(do_work), "do work 不是协程函数"
    # assert asyncio.iscoroutine(do_work), "do work 不是协程对象"

    coroutine_obj = do_work(2)
    assert asyncio.iscoroutine(coroutine_obj), "这不是一个协程对象"


def run_coroutine():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_work(2))  # 阻塞调用，直到协程运行完毕后，才会返回


def run_coroutine2():
    loop = asyncio.get_event_loop()
    futu = asyncio.ensure_future(do_work(3))  # 先将协程转化为future
    futu.add_done_callback(done_callback)  # future对象，绑定回调函数；
    loop.run_until_complete(futu)


def run_coroutine_list():
    # asyncio.gather(): 将多个future对象打包成一个对象
    loop = asyncio.get_event_loop()
    # 异步执行多个协程任务
    loop.run_until_complete(asyncio.gather(do_work(1), do_work(2), do_work(3)))

    loop = asyncio.get_event_loop()
    coroutine_list = [do_work(1), do_work(2), do_work(3)]
    loop.run_until_complete(asyncio.gather(*coroutine_list))  # 使用解包操作


def run_coroutine_forever():
    loop = asyncio.get_event_loop()
    futu = asyncio.gather(do_work(3))  #
    loop.run_forever()  # 如果不主动终止，会一直运行; 协程终止后，与不会终止程序
    # loop.stop() 在这里会永远执行不到； 需要放到协程中


def stop_callback(loop, futu):
    print("stop run forever...")
    loop.stop()
    loop.close()    # 执行后，将无法再通过loop.run_until_complete来启动协程


def run_coroutine_forever_stop():
    """策略： 先使用asyncio.gather() 将多个协程打包为一个future，然后再在其上绑定回调函数，终止协程"""
    loop = asyncio.get_event_loop()
    coroutine_list = [do_work(1), do_work(2), do_work(3)]
    futu = asyncio.gather(*coroutine_list)
    futu.add_done_callback(functools.partial(stop_callback, loop))
    loop.run_forever()


if __name__ == '__main__':
    # run_coroutine()
    # run_coroutine2()
    # run_coroutine_list()
    # run_coroutine_forever()
    run_coroutine_forever_stop()
