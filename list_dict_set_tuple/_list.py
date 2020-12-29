# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 10:30
# Warning    ：The Hard Way Is Easier
l = [1, 2, 3, 4, 5, 6, 7]


def Test1():
    # l.clear()
    l.pop(2)
    del l[0]
    print("test 1", l)


def Test2():
    s = 'ddddkkksfhjsglllll'
    s = set(s)
    # 该方法没有返回值，原来的s值也没有被修改
    # print(list(set(s)).sort())
    res = sorted(list(set(s)))
    # print(s)
    print(res)


t = [[1, 2], [3, 4], [5, 6]]
# way 1
res = []
for item in t: res.extend(item)
print(res)

# way 2
res = [i for temp in t for i in temp]
print(res)

print(l.pop(0))
print(l.count(3))
print(l.remove(2))
l.reverse()
print(l)
if __name__ == '__main__':
    # Test1()
    # Test2()
    pass
