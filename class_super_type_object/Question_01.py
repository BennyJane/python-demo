# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

# 判断题目
class A(object):
    pass


class B(A):
    pass


b = B()

assert isinstance(b, A) == True, "b 不是A的实例"
assert isinstance(b, object) == True, "b 不是object的实例"
assert issubclass(B, A) == True, "B 不是A的子类"
assert issubclass(b, B) == True, "b 不是B的子类"

