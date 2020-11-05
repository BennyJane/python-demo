# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

import weakref


class Card(object):
    # 弱引用
    _CardPool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit, **kwargs):
        obj = Card._CardPool.get(value + suit, None)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __init__(self, value, suit):
        self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


if __name__ == '__main__':
    # 可以注释掉 __new__ 来进行对比
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))
