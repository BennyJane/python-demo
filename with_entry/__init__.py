# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 17:18
# Warning    ：The Hard Way Is Easier
from contextlib import contextmanager

"""
========================================================================================================================
类模式: 实现 __enter__ __exit__协议
========================================================================================================================
"""


class StandardStructure:
    def __enter__(self, *args, **kwargs):  # 可接收额外的参数
        # 实现获取资源，或者初始化状态的操作
        return self  # 可以返回内容，也可以不返回

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        释放资源，或者还原状态的操作
        :param exc_type: 异常类（例如 KeyValueError）
        :param exc_val: 异常实例；有时会有参数传递给异常构造方法，例如错误信息，这些参数可以使用exc_value.args获取
        :param exc_tb: traceback 对象
        :return: True: 异常已经处理； 非True（例如None），任意异常都会向上冒泡
        """
        return True  # 异常已经处理返回True， 其他返回值都会导致异常向上抛出


# 使用方式
# TODO with语句
with StandardStructure() as res:  # 执行上下文管理器类的__enter__方法，获取返回值，并赋值给 res
    pass
# 无论退出with语句的方式：return语句、异常、sys.exit()，
# 都会执行 上下文管理器类的__exit__方法
# with语句中赋值变量res，在退出with语句后，仍然可以访问，可以访问其属性；但with管理的资源已经关闭，不能再像with语句块内调用

# TODO 不适用with
_instance = StandardStructure()  # 获取上下文管理器实例
res = _instance.__enter__()  # 在实例上调用__enter__
# 使用res

_instance.__exit__(None, None, None)  # 在实例上调用__exit__，完成收尾的处理

"""
========================================================================================================================
装饰器: contextmanager
使用该装饰器修饰 【生成器函数】，可以快速实现一个上下文管理器；
contextlib.contextmanager 装饰器会把函数包装成实现 __enter__ 和 __exit__ 方法的类。

这个类的 __enter__ 方法有如下作用。
(1) 调用生成器函数，保存生成器对象（这里把它称为 gen）。
(2) 调用 next(gen)，执行到 yield 关键字所在的位置。
(3) 返回 next(gen) 产出的值，以便把产出的值绑定到 with/as 语句中的目标变量上。

with 块终止时，__exit__ 方法会做以下几件事。
(1) 检查有没有把异常传给 exc_type；如果有，调用 gen.throw(exception)，在生成器函数
定义体中包含 yield 关键字的那一行抛出异常。
(2) 否则，调用 next(gen)，继续执行生成器函数定义体中 yield 语句之后的代码。
========================================================================================================================
"""


@contextmanager
def generator_func(*args, **kwargs):  #
    # <setup> 打开连接、资源、锁等
    res = ""
    try:
        yield res  # 使用with语句调用后，返回res； yield语句前代码都会在with块开始时调用（即，解释器调用__enter__）
        # 退出with语块后，开始执行yield后续的代码
    except Exception as e:  # 捕获生成器调用方（with语句块内）抛出的异常
        pass
    finally:
        # <cleanup> 关闭资源、连接、锁
        pass


# TODO 使用
with generator_func() as res:
    # <body> 完成核心任务
    pass

if __name__ == '__main__':
    pass
