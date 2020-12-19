# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/19 15:59
# Warning    ：The Hard Way Is Easier
from typing import List

"""
给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。

输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]

提示：
0 <= len(array) <= 1000000
"""


# TODO 前提假设：数列为递增

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        """
        从左往右遍历：记录当前已遍历数据的最大值，后续所有小于记录最大值的数据都是需要重新排序的对象
        从右往左遍历： 记录当前已遍历数据的最小值，后续所有大于记录值的数据都是需要重新排序的对象
        """
        import sys
        _len = len(array)
        _max, _min = -1 * sys.maxsize, sys.maxsize
        l, r = -1, -1
        for i in range(_len):  # 正序遍历
            if array[i] < _max:  # 非递增数据出现
                r = i  # 标记有需要重新排序的最右侧位置
            else:  # 正常递增，_max记录当前遍历数值中最大值
                _max = array[i]

        for i in range(_len - 1, -1, -1):
            if array[i] <= _min:  # 正常：应该递减，相等的值不需要调整位置
                _min = array[i]
            else:
                l = i
        return [l, r]

    def second(self, array: List[int]) -> List[int]:
        """将序列排列好后，再进行逐个比对"""
        l = sorted(array)
        gap = [-1, -1]
        _len = len(array)
        for i in range(_len):
            if array[i] != l[i]:
                gap[0] = i
                break

        for i in range(_len - 1, -1, -1):
            if array[i] != l[i]:
                gap[1] = i
                break
        return gap

    def third(self, array: List[int]) -> List[int]:
        l = sorted(array)
        if l == array:
            return [-1, -1]
        m = 0
        n = len(array) - 1
        while l[m] == array[m] and m < n:  # 最后一个数值不需要判断，乱序至少涉及两个位置
            m += 1
        while l[n] == array[n] and m < n:
            n -= 1
        return [m, n]


if __name__ == '__main__':
    l = [5, 3, 1, 7, 9]
    s = Solution()
    print(s.subSort(l))
