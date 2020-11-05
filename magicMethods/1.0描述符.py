# -*- coding: utf-8 -*-
# @Time : 2020/11/5
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class Base:
    name = "base"

    def __get__(self, instance, owner):
        """"""
        return self


b = Base()

b.__setattr__("job", "actor")
print(b.__dict__)

getattr()
setattr()
delattr()