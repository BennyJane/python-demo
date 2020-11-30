from collections import namedtuple
from inspect import getgeneratorstate
import time
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


def dynamic_step_seq(size, start=0, default_step=1):
    s = 0
    for _ in range(size):
        step = yield s
        if step is not None:
            s += step
        else:
            s += default_step


# 生成器使用方法
# for s in dynamic_step_seq(10):
#     print(s, end=' ')


def Test3():
    s = "abc"
    l = [1, 2, 3, 4, 5]
    t = (1, 2, 3, 4)
    j = {1, 2, 3, 4, 5}
    print(iter(t))
    t_iterator = iter(t)
    print(t_iterator.__class__, hasattr(t_iterator.__class__, '__next__'))
    print(next(t_iterator))
    print(t.__class__, hasattr(t.__class__, '__next__'))
    print(t.__class__, hasattr(t.__class__, '__iter__'))
    print(t.__class__.__iter__)
    print(t, hasattr(t, 'next'), hasattr(t, '__next__'))

    s_iterator = iter(s)
    print(next(s_iterator))

    l_iterator = iter(l)
    print(next(l_iterator))
    # print(next(l))
    # next(s)
    # print(next(s))
    # print(next(j))
    j_iterator = iter(j)
    print(next(j_iterator))


class iteratorEx(object):
    def __init__(self, end):
        self.end = end
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.end:
            # cur, self.num = self.num, self.num + 1
            self.num = self.num + 1
            # 返回当前的self.num, 并对self.num 进行累加
            return self.num - 1
        raise StopIteration()

    # 定义该方法依然不能当做迭代器使用
    # def __getitem__(self, item):
    #     return self.nums[item]


def Test4():
    iterator = iteratorEx(100)
    print(type(iterator))
    sum_n = sum(iterator)
    print(sum_n)
    # print(sum(iterator))
    # for i in iterator:
    #     print(i)

    print(iter(iterator))

    # next(iterator)
    # print(next(iterator))


def Test5():
    def add_A(seq):
        print("A-before")
        time.sleep(1)
        for item in seq:
            print("A")
            yield item + '-A'

    def add_B(seq):
        print("B-before")
        time.sleep(1)
        for item in seq:
            print("B")
            yield item + '-B'

    def add_C(seq):
        print("C-before")
        time.sleep(1)
        for item in seq:
            print("C")
            yield item + '-C'

    seq = ['apple', 'banana', 'orange']

    stacked_generator = add_C(add_B(add_A(seq)))

    next(stacked_generator)

    # for item in stacked_generator:
    #     print(item)

    """
    apple-A-B-C
    banana-A-B-C
    orange-A-B-C
    """


if __name__ == '__main__':
    # Test1()
    # Test2()
    # Test3()
    # Test4()
    Test5()
