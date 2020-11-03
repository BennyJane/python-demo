# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise
import os


class MoveFileCommand:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        """调用__call__ 方法"""
        self()

    def __call__(self, *args, **kwargs):
        print("renaming {} to {}".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print("renaming {} to {}".format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == '__main__':
    command_stack = [MoveFileCommand('__init__.py', 'init.py'),
                     MoveFileCommand('init.py', 'it.py')]

    for cmd in command_stack:
        cmd.execute()

    # reversed(list) 倒序排列
    for cmd in command_stack[::-1]:
        cmd.undo()
