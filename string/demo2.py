# -*- coding: utf-8 -*-
# @Time : 2020/11/29
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
import os

print(os.getcwd())

"""
进制转换：
"""
# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


# 二进制 -》 十进制
def bin2dec(string_num):
    return str(int(string_num, 2))


# 10进制 -》 2进制


def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])  # 倒序


# 16进制 -》 10进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


# dec2hex
# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# hex2tobi 十六进制 to 二进制: bin(int(str,16))
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))

# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))