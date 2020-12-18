# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Question-Steo
# Time       ：2020/12/17 23:29
# Warning    ：The Hard Way Is Easier

# https://blog.csdn.net/anascetic/article/details/78631073


def Answer(n):
    res = 0
    for i in range(1, n + 1):  # 从1开始循环到N
        if i < 3:
            res = i
            continue
        res = 2 * res
    print(res)
    return res


fib = lambda n: n if n < 2 else 2 * fib(n - 1)

if __name__ == '__main__':
    Answer(10)
