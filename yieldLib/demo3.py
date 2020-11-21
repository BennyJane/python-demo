from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple("Result", "count average")


def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    # return Result(count, average)


def Test1():
    data = [0, 2, 1, 5, 4, 5, 15, 25]
    gen = averager()
    gen.send(None)
    for i in data: gen.send(i)
    result = gen.send(None)
    print(result)


def gen2():
    while True:
        yield 1


def Test2():
    g = gen2()
    print(getgeneratorstate(g))
    next(g)
    g.send(10)
    print(getgeneratorstate(g))


if __name__ == '__main__':
    # Test1()
    Test2()
