from functools import wraps
from inspect import getgeneratorstate

"""
===============================================================================================================
案例01
===============================================================================================================
"""


def simple_coroutine():
    print('start coroutine')
    x = yield
    print('end coroutine', x)


def Test1():
    my_corou = simple_coroutine()
    print(type(my_corou))
    next(my_corou)
    my_corou.send(40)


def Test2():
    my_corou = simple_coroutine()
    # print(type(my_corou))
    # next(my_corou)
    my_corou.send(40)


"""
===============================================================================================================
案例02
===============================================================================================================
"""


def simple_coro2(a):
    print('start coroutine a = {}'.format(a))
    b = yield a
    print('-> Received b ={}'.format(b))
    c = yield a + b
    print('-> Received c ={}'.format(c))


def Test3():
    my_corou = simple_coro2(10)
    print(getgeneratorstate(my_corou))
    first_res = my_corou.send(None)
    print(getgeneratorstate(my_corou))
    print("first response", first_res)

    second_res = my_corou.send(11)
    print("second response", second_res)

    third_res = my_corou.send(12)
    print("third response", third_res)
    # yield


"""
===============================================================================================================
案例03:
生成器函数的使用：
- 直接调用仅仅返回生成器对象
- 也需要调用send() next()，才会执行到第一个yield处
===============================================================================================================
"""


def generatorItem():
    yield "this is a generator"


def Test4():
    res = generatorItem()
    # next(res)
    print(res.send(None))
    # print(next(res))
    print(res)


"""
===============================================================================================================
案例04:
使用协程实现计算移动平均值： 动态计算平均值
===============================================================================================================
"""


def averager():
    total = 0.0
    count = 0
    average = 0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


def Test5():
    ave = averager()
    next(ave)

    average1 = ave.send(10)
    average2 = ave.send(15)
    print(average1, average2)
    print(ave.send(25))
    print(ave.send(30))


"""
===============================================================================================================
案例05:
实现预激协程的装饰器
===============================================================================================================
"""


def corouDecorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        gen = f(*args, **kwargs)
        next(gen)
        return gen

    return wrapper


if __name__ == '__main__':
    # Test1()
    # Test2()
    # Test3()
    # Test4()
    Test5()
