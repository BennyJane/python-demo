# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 20:09
# Warning    ：The Hard Way Is Easier

# 一句话输出99乘法表 ==> 噱头 + 丑陋的代码
import math


#  '\n'.join(['\t'.join(["%2s*%2s=%2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)])


def table_nine_mul_nine():
    res = [f"{i}x{j}={i * j}" for i in range(1, 10) for j in range(1, 10) if j <= i]
    print(res)

    groups = ["\t".join(["%2s*%2s=%2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]
    print("\n".join(groups))


def table_nine_mul_nine2():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}X{}={}\t".format(j, i, i * i), end=" ")  # \t 对齐； end=" "确保不换行
        print()  # 换行


# 打印菱形

def shape(n=7):
    print("\n".join([" " * (4 - i) + "*" * (2 * i - 1) for i in [1, 2, 3, 4, 3, 2, 1]]))


if __name__ == '__main__':
    # table_nine_mul_nine()
    # table_nine_mul_nine2()

    shape()
