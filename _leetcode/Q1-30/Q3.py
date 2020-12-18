# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Question-Steo
# Time       ：2020/12/17 23:54
# Warning    ：The Hard Way Is Easier


def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


def answer(l1, l2):
    temp = []

    def _recursion_merge(ori1, ori2):
        if any([len(ori1) == 0, len(ori2) == 0]):
            temp.extend(ori1)
            temp.extend(ori2)
            return temp  # 必须返回结果
        else:
            if ori1[0] > ori2[0]:
                temp.append(ori2[0])
                del ori2[0]
            else:
                temp.append(ori1[0])
                del ori1[0]
        return _recursion_merge(ori1, ori2)

    return _recursion_merge(l1, l2)


def answer2(l1, l2):
    temp = []
    first = second = 0

    def wrap(ori1, ori2):
        nonlocal first, second
        if any([first >= len(ori1), second >= len(ori2)]):
            if first < len(ori1):
                temp.extend(ori1[first:])
            if second < len(ori2):
                temp.extend(ori2[second:])
            return temp
        else:
            if ori1[first] > ori2[second]:
                temp.append(ori2[second])
                second += 1
            else:
                temp.append(ori1[first])
                first += 1
        return wrap(ori1, ori2)

    return wrap(l1, l2)


if __name__ == '__main__':
    l1 = [1, 3, 5, 6, 8, 9, 12, 56, 78]
    l2 = [2, 4, 7, 14, 35, 42, 58, 102]
    res = recursion_merge_sort2(l1, l2)
    print(res)

    l1 = [1, 3, 5, 6, 8, 9, 12, 56, 78]
    l2 = [2, 4, 7, 14, 35, 42, 58, 102]
    res = answer(l1, l2)
    print(res)

    l1 = [1, 3, 5, 6, 8, 9, 12, 56]
    l2 = [2, 4, 7, 14, 35, 42, 58, 102]
    res = answer2(l1, l2)
    print(res)

    l1 = [1, 3, 5, 6, 3, 8, 9, 3, 12, 56]
    print(l1.index(3, 1, 8))
    l1.remove(56)
    # del l1[56]
    l1.pop()
    print(l1)
