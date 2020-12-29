# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 19:34
# Warning    ：The Hard Way Is Easier
l = [1, 2, 3, 4, [1, 2, 3]]


def add_element(l):
    l = list(l)  # list() 操作为浅拷贝
    l[-1].append(4)  # 修改嵌套列表元素
    return id(l)

"""
测试用例
"""


def test_change():
    l2_id = add_element(l)
    assert len(l[-1]) == 4  # 全局变量l列表中的可变元素被修改
    assert id(l) != l2_id  # add_element内部已经创建新的对象


