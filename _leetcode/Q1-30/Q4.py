# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Question-Steo
# Time       ：2020/12/18 14:08
# Warning    ：The Hard Way Is Easier


def binary_search(l: list, target: int) -> int:
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        guess = l[mid]
        if guess > target:
            # 如果此处设置为 right = mid;
            # 那么可能 上面计算得到的mid还是该值，就会陷入死循环
            right = mid - 1
        elif guess < target:
            left = mid + 1
        else:
            return mid
    return None


mylist = [1, 3, 5, 7, 9]
mylist = [1]

print(binary_search(mylist, 1))


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((high - low) / 2 + low)    # 避免(high + low) / 2溢出
        guess = list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid
    return None
mylist = [1,3,5,7,9]
print(binary_search(mylist, 1))