# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/20 23:10
# Warning    ：The Hard Way Is Easier

"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
"""


def quick(L: list) -> list:
    if len(L) < 2:
        return L
    else:
        start = L[0]
        less = [i for i in L[1:] if i + start < start + i]
        greater = [i for i in L[1:] if i + start >= start + i]
        return quick(less) + [start] + quick(greater)


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        l = list(map(str, nums))

        res = quick(l)
        min_value = ''.join(res)
        # return '0' if min_value[0] == '0' else min_value
        return min_value
