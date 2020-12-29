# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/28 17:18
# Warning    ：The Hard Way Is Easier
import os
import sys

"""
os: 对操作系统的高度封装
"""


def os_funcs():
    os.getenv("key", "default")
    pwd = os.getcwd()  # 获取当前运行路径
    print("pwd", pwd)
    path = 'F:\LearnExercise\Python-Exercise\standard_pkg'
    dir_files = list(os.walk(path))  # 生成指定目录下的文件夹以及文件; 返回生成器
    print(dir_files)  # 元组构成列表：每个元组包含三个元素： 文件目录路径， 目录列表，文件列表
    os.makedirs()  # 生成多层级目录
    os.mkdir()  # 生成目录，多层级会报错
    os.rmdir()  # 删除指定目录
    os.removedirs()  # 删除多层级目录
    os.listdir()  # 列出指定目录下的所有文件夹以及文件
    os.path.join()  # 将可迭代对象拼合为单个路径名
    os.path.getsize()  # 获取指定目录或文件的大小
    os.path.exists()  # 判断目录或文件是否存在
    os.path.isabs()  # 判断指定目录是否时绝对路径
    os.path.isdir()  # 判断给定路径是否时文件目录
    os.path.isfile()  # 判断给定路径是否时文件


def sys_funcs():
    sys.argv()  # 获取命令行参数列表
    sys.exit()  # 推出程序，并返回指定的整数
    sys.maxunicode  # 最大的unicode值
    sys.modules  # 系统导入的模块名称
    sys.path  # PY搜索模块时的路径
    sys.stdout  # 标准输出
    sys.stdin  # 标准输入
    sys.stderr  # 错误输出


if __name__ == '__main__':
    pass
