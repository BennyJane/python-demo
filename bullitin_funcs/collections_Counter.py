# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 10:50
# Warning    ：The Hard Way Is Easier
from collections import Counter

a = 'sdfalsdfhashdfjksadflksjakdf'

result = Counter(a)
print(result)
print(result.values())
print(result.keys())
print(result.items())
print(result.most_common(2))
