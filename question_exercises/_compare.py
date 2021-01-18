# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
================================================================
元组比较： 同位置逐个比较

ASCII码大小：
- 数字（需要转为字符串，才可使用ord()计算） < 大写字母 < 小写字母
"""

# 报错： '<' not supported between instances of 'int' and 'str'
# print((3, 2) < ("a", "b"))
print(("3", "2") < ("a", "b"))
print(3 > 2 > 2)

print(ord("1"), ord("A"), ord("a"))
