# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/18 21:30
# Warning    ：The Hard Way Is Easier


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


def cmp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


if __name__ == '__main__':
    l = [3, 30, 34, 5, 9]
    s = Solution()
    res = s.largestNumber(l)
    print(res)

    print(list(map(str, l)))
    new_l = list(map(str, l))
    new_l = sorted(new_l, key=lambda x: x[0], reverse=True)
    print(new_l)

    import functools
    L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
    # 根据元组索引1的值排序
    res = sorted(L, key=functools.cmp_to_key(cmp))  # 利用cmp函数
    print(res)
