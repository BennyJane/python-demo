# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Question-Steo
# Time       ：2020/12/17 22:26
# Warning    ：The Hard Way Is Easier
def output(args):
    print("[最终结果为]： {}".format(args))


"""
台阶问题：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

"""
A: 求多少种可能的题目，一般有递推性质，即 f(n) 和 f(n-1)...f(1)之间有关系
所以，从f(1)开始思考：
n=1 1 
n=2 2 
n=3 3 
n=4 5
...

归纳： f(n) = f(n-1) + f(n-2)
转化为： 斐波那契数列问题
"""

"""
动态规划： 
以斐波那契数列性质 f(n + 1) = f(n) + f(n - 1)f(n+1)=f(n)+f(n−1) 为转移方程。
从计算效率、空间复杂度上看，动态规划是本题的最佳解法。
"""


def Answer_1(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    output(a)
    return a


"""
递推： 存在大量重复计算
把 f(n)f(n) 问题的计算拆分成 f(n-1)f(n−1) 和 f(n-2)f(n−2) 两个子问题的计算，并递归，以 f(0)f(0) 和 f(1)f(1) 为终止条件
缺点： 大量重复的递归计算，例如 f(n)f(n) 和 f(n - 1)f(n−1) 两者向下递归都需要计算 f(n - 2)f(n−2) 的值。
"""

# 耗时超长，舍弃
def Answer_2(n: int) -> int:
    # 临界值的设置：n -2 >=1  n>=3; n< 3 的情况就是 1 2，直接返回就可以
    fib = lambda n: n if n < 3 else fib(n - 1) + fib(n - 2)
    res = fib(n)
    output(res)
    return res


"""
记忆方法：
原理： 在递归法的基础上，新建一个长度为 n 的数组，用于在递归时存储 f(0)至 f(n) 的数字值，
重复遇到某数字时则直接从数组取用，避免了重复的递归计算。
缺点： 记忆化存储的数组需要使用 O(N)的额外空间。
"""


def cache(func):
    cached = {}

    def wrap(arg):
        if arg not in cached:
            cached[arg] = func(arg)
        return cached[arg]

    return wrap


@cache
def fib(n):
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 2)


def mem_fib(n):
    """利用数组存储已经计算的值"""


"""
======================================================================================================
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
======================================================================================================
n=1 1 
n=2 2 
n=3 4 
n=4 8
n=5 16
n=6 32

       | 0 ,(n=0 )
f(n) = | 1 ,(n=1 )
       | 2*f(n-1),(n>=2)
"""




if __name__ == '__main__':
    Answer_1(39)
    # Answer_2(39)
    # print(fib(39))
