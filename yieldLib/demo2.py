import time
from collections import namedtuple

"""
===============================================================================================================
案例01
===============================================================================================================
"""

Result = namedtuple("Result", "count average")


def childGen():  # 子生成器
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # 只接收调用方的值，不返回值，返回None
        time.sleep(0.2)
        # print("childGen run", term)
        if term is None:  # 哨符值，用来主动终止协程
            break
        total += term
        count += 1
        average = total / count
    # 如果直接使用该生成器，最后返回值后，仍会抛出异常
    # 使用 yield from 管理该协程，则会自动处理异常，并获取返回值
    return Result(count, average)


def genManage(results, key):
    # 传入的参数仅仅用于存储子生成器返回的值
    while True:  # 此处的死循环，是为了避免抛出 StopIteration异常
        # print("run genManage")
        results[key] = yield from childGen()


def report(res):
    for key, result in sorted(res.items()):
        group, unit = key.split(';')
        print("{:2} {:5} averaging {:.2f}{}".format(result.count, group, result.average, unit))
    print(".... end ...")


def core():
    results = {}
    for key, values in data.items():
        """
        > 调用genManage，返回委派生成器（genManage）对象;
        > 此时，委派生成器处于等待开始状态
        > 每个key都会创建一个委派生成器；
        """
        group = genManage(results, key)
        # print(type(group))
        # print(getgeneratorstate(group))
        """
        > 预激协程，激活的是委派生成器；
        > 代码执行到while True: 下的 yield from, 调用 子生成器，然后委派生成器在此处暂停
        > yield from后的子生成器，被直接预激活，进去暂停状态，即不需要预激子生成器
        """
        next(group)
        for value in values:
            """
            > 向子生成器内传递数据；genManage并不知道传递的具体内容； 实现了与子生成器直接沟通的数据管道
            > 调用方与子生成器之间直接传递数据
            """
            group.send(value)
        """
        > 当调用方不再调用.send()方法，子生成器暂停在yield表达式处，并没有终止运行；
        > 如果不终止子生成器，委派生成器将暂停在yield from处，不会执行左侧的赋值步骤；
            > 再次执行genManage()创建新委派生成器，并赋值给group，因此上一个委派生成器（以及它创建的尚未种植的子生成器实例）就会被垃圾回收程序回收
        """
        # TODO 终止子生成器的运行；利用了哨符值None
        res = group.send(None)
        # print(res, type(res))
        # break

    report(results)  # 打印输出最后的结果


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


def Test1():
    group = genManage({}, 'a')
    next(group)
    res = group.send(None)
    print(res, type(res))

    first = childGen()
    second = childGen()
    print(first, second)


if __name__ == '__main__':
    core()
    # Test1()
