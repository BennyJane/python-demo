# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/20 20:08
# Warning    ：The Hard Way Is Easier

"""
给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直面积 的宽度。

垂直面积 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直面积 为宽度最大的一个垂直面积。

请注意，垂直区域 边上 的点 不在 区域内。
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_w = 0
        l = sorted(points, key=lambda x: x[0])
        for i in range(len(l) - 1):
            width = l[i + 1][0] - l[i][0]
            if width > max_w:
                max_w = width

        return max_w

    def second(self, points: List[List[int]]) -> int:
        class max_w:
            def __le__(self, other):
                return self[0] < other[0]

        l = sorted(points, key=lambda x: max_w(x))
        print(l)


if __name__ == '__main__':
    class max_w:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return abs(self.value[0] - other.value[0])


    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    # points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    points.sort()
    l = sorted(points, key=lambda x: max_w(x), reverse=True)
    print(l)
