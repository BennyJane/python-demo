# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 18:51
# Warning    ：The Hard Way Is Easier

t1 = (1, 2, 3, 4, 5, 6)
t2 = (7, 8, 9, 10, 11)

# 统计元素数量：没有返回0
res = t1.count(1)
res2 = t1.count(100)
print("计算元素数量", res, res2)

# 获取元素索引：不存在元素抛出错误
res = t1.index(2)
try:
    res2 = t1.index(100)
    print("获取元素索引", res, res2)
except ValueError:
    pass

