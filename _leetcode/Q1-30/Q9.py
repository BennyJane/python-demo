# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/20 20:54
# Warning    ：The Hard Way Is Easier

"""
179. 最大数
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

输入：nums = [10,2]
输出："210"


# TIP： 比较的逻辑
"""
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class custom_lt(str):  # 自定义重载运算符： __lt__ 小于等于
            def __lt__(self, other):
                # 默认降序： 为了确保大的数字在前面，所以下面判断： self更大的时候返回True
                # 如果下面用小于等于符号，sorted中需要设置 reverse = True
                return self + other > other + self

        # sorted() 默认排序时，触发每个对象的 __lt__ 方法，升序
        # 降序时触发： __gt__
        res = ''.join(sorted(map(str, nums), key=lambda x: custom_lt(x)))
        return '0' if res[0] == '0' else res

    def second(self, nums: List[int]) -> str:
        l = list(map(str, nums))
        # 冒泡排序
        right = 1
        _len = len(nums)
        while right <= _len - 1:
            for i in range(_len - right):
                if l[i] + l[i + 1] < l[i + 1] + l[i]:
                    l[i], l[i + 1] = l[i + 1], l[i]
            right += 1

        large_nums = ''.join(l)
        return '0' if large_nums[0] == '0' else large_nums

    def thrid(self, nums: List[int]) -> str:
        l = list(map(str, nums))
        # 冒泡排序
        _len = len(nums)
        for j in range(_len):
            for i in range(_len - 1 - j):
                if l[i] + l[i + 1] < l[i + 1] + l[i]:
                    l[i], l[i + 1] = l[i + 1], l[i]

        large_nums = ''.join(l)
        return '0' if large_nums[0] == '0' else large_nums

    def forth(self, nums: List[int]) -> str:
        l = list(map(str, nums))

        # 快排： 更快
        def qucik(ori):
            if len(ori) < 2:
                return ori
            else:
                pivot = ori[0]
                greater = [i for i in ori[1:] if i + pivot >= pivot + i]
                less = [i for i in ori[1:] if i + pivot < pivot + i]
                return qucik(greater) + [pivot] + qucik(less)

        res = qucik(l)
        large_nums = ''.join(res)
        return '0' if large_nums[0] == '0' else large_nums
