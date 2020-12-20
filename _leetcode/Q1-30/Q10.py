# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/20 21:34
# Warning    ：The Hard Way Is Easier
"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。


_len = len(citations)
h 的最大值为 _len
从左往右遍历，每移动一位，h的最大值就减少1；
当移动到当前引用次数 c >= 剩余数量时， 次数剩余数量就是h的值


"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0 or max(citations) == 0:
            return 0
        citations.sort()
        _len = len(citations)
        for i in range(_len):
            remaining = _len - i  # 右侧剩余数量其实就是h指数
            if citations[i] >= remaining:
                return remaining
