# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/18 21:30
# Warning    ：The Hard Way Is Easier

"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]


- 先排序，利用字典存储数值出现的频率； 再对字典进行排序
"""


class Solution(object):
    def topKFrequent(self, nums: list, k: int) -> list:
        """"""
        count = {}
        for item in nums:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        # 对字典进行排序
        # count.items() => 将字典转化为元祖迭代器
        # reverse 修改默认降序为升序
        output = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = [output[i][0] for i in range(k)]
        return res

    def second(self, nums: list, k: int) -> list:
        """使用PY内置的collections.Counter"""
        import collections
        counter = collections.Counter(nums)
        return [item[0] for item in counter.most_common(k)]

    def third(self,  nums: list, k: int):
        """将统计好的数据，根据次数填入列表对应索引的位置"""
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # 生成足够长度的列表： 最大索引为len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            bucket[value].append(key)
        print("[列表索引就是频率]", bucket)

        result = []
        for i in range(len(nums), 0, -1):
            result.extend(bucket[i])
            if len(result) == k:
                return result

        return result



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    print(s.topKFrequent(nums, 2))
    print(s.third(nums, 2))
