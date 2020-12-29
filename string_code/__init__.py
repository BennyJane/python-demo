# -*- coding: utf-8 -*-
# @Time : 2020/11/29
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

s = "benny jane"

# 设置同行字符串的对齐方式
# __with：设置字符串的宽度
# __fillchar: 设置剩余位置的填充字符串
print(s.ljust(20, "-"), "benny")
print(s.rjust(20, "*"), s)
