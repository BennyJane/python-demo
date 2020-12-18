# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Question-Steo
# Time       ：2020/12/18 14:41
# Warning    ：The Hard Way Is Easier


def bubbleSort(relist):
    right = 1
    length = len(relist)
    # 临界点判断： length - right >= 2
    while right <= (length - 2):
        for i in range(length - right):
            first = relist[i]
            second = relist[i + 1]
            if first > second:
                relist[i], relist[i + 1] = second, first
        right += 1

    return relist


def selectSort(ori: list) -> list:
    right = 0
    _len = len(ori)
    while right <= (_len - 2):
        min_value = None  # 此处应该设置为无穷大
        min_index = None
        for i in range(right, _len):
            if min_value is None:
                min_value = ori[i]
                min_index = i
                continue
            if ori[i] < min_value:
                min_value = ori[i]
                min_index = i
        ori[right], ori[min_index] = min_value, ori[right]
        right += 1
    return ori


def selectSort2(ori: list) -> list:
    right = 0
    _len = len(ori)
    while right < (_len - 2):
        min_index = right
        for i in range(right + 1, _len):
            if ori[i] < ori[right]:
                min_index = i
        ori[right], ori[min_index] = ori[min_index], ori[right]
        right += 1
    return ori


def shellSort(ori: list) -> list:
    _len = len(ori)
    gap = _len // 2
    while gap > 0:
        for j in range(gap, _len):
            temp = ori[j]
            while j >= gap and ori[j - gap] > temp:
                print("shell", gap, j)
                ori[j] = ori[j - gap]
                # break
                j -= gap
            ori[j] = temp
        print(ori)
        gap = gap // 2

    return ori


if __name__ == '__main__':
    # l = [3, 10, 1, 25, 325, 1254, 235, 254, 543, 254, 52, 32, 2]
    # print(bubbleSort(l))

    l = [3, 10, 1, 25, 325, 1254, 235, 254, 543, 254, 52, 32, 2]
    print(selectSort(l))
    print(selectSort([1, 5, 6, 7, 9, 8, 2, 4, 3]))

    l = [3, 10, 1, 25, 325, 1254, 235, 254, 543, 254, 52, 32, 2]
    print(selectSort2(l))
    print(selectSort2([1, 5, 6, 7, 9, 8, 2, 4, 3]))

    print([1, 5, 6, 7, 9, 8, 2, 4, 3])
    print(shellSort([1, 5, 6, 7, 9, 8, 2, 4, 3]))

    sorted(l, key=str)
