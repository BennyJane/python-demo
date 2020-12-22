# -*- coding: utf-8 -*-
# @Time : 2020/11/29
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
import os

print(os.getcwd())

"""
字符串与字节码转化：
bytes: 主要给计算机看的，string给用户看的；
两者中间通过编码规则转换，一般使用utf-8；
bytes: 二进制，容易转化为16进制
string_demo：通过encode()， 编码为bytes
bytes: 通过decode(),解码为string；反解码的编码规则是有范围的

"""
# 符号b， 表示bytes格式
b = b'example'
print(b)
s = "example"

# string_demo -> bytes
# 必须指定编码格式
b2 = bytes(s, encoding='utf-8')

# string_demo, encode获取一个bytes对象
b3 = s.encode()
print(type(b3))

# bytes 转化为 string_demo
s2 = b.decode()
print(type(s2))
