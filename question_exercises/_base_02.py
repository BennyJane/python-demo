# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

# TODO 关于 == and or 位运算符的题目

"""
================================================================
python： 位运算符号
参考文章： https://www.runoob.com/python/python-operators.html
<<
    - a << move
    - a 被修改的原始数值； move 移动的位数
    - 左移运算符：运算数 每个二进位全部左移若干位
    - 规则： 高位的0丢弃，低位补0
"""
a = 60
print(a, bin(a))
a_res = a << 2
print(a_res, bin(a_res))

print(1 << 1)

"""
================================================================
0b 二进制
0o 八进制
0x 十六进制

int 将其他进制转化为十进制
"""
a = 10
print("[10 的二进制表示] ", bin(a))
print("[10 的二进制表示] ", oct(a))
print("[10 的十六进制表示] ", hex(a))
a_0x = hex(a)
print("[~转十进制] ", a_0x, int(a_0x))


# TODO 进制比较
print("0x56" < "56")
# 0x: 16进制
print(0x56 < 56)
print(int(0x56))