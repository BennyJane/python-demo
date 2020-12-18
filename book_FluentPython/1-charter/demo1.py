# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/18 21:27
# Warning    ：The Hard Way Is Easier
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        s = ''
        if nums[-1] == 0:
            return('0')
        for i in nums:
            s = str(i) + s
        return s


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num



