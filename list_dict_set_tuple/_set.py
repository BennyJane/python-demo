# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 18:04
# Warning    ：The Hard Way Is Easier

s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9, 10}

# 删除操作： 输入值
s1.remove(1)
print("删除数据", s1)
# 弹出: 不接收参数，默认弹出索引为0的数据； 当元组为空，抛出keyValue
res = s1.pop()
print("弹出数据", res, s1)
# 参数： iterable,在集合中追加可迭代对象
s1.update({1, 10})
s1.update((11,))
s1.update([12])
s1.update("abc")
s1.update({"name": "benny"})  # 默认迭代key
print("追加数据", s1)
# 添加单个元素
s1.add(100)
print("添加元素", s1)
# 删除指定元素： 元素不存在就不操作；无返回值
s1.discard(5)
print("删除指定元素", s1)
# 求交集
intersection = s1.intersection(s2)
print("交集", intersection)
# 求并集
union = s1.union(s2)
print("并集", union)
# 求差集
difference = s1.difference(s2)
print("差集", difference)

# 清空元组，无返回值
s1.clear()
print("清空数据", s1)
