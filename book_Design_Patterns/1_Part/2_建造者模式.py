# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

class Base:
    def __init__(self, name):
        self.name = name

    def common(self):
        """公共方法，提高代码复用率"""


class FirstBuilder:
    def __init__(self):
        self.attr = "first"

    def first_step(self):
        """构造序列1"""

    def second_step(self):
        """构造序列2"""

    def third_step(self):
        """构造序列3"""


class SecondBuilder:
    def __init__(self):
        self.attr = "second"

    # 每一个步骤都完成对象的部分功能构造
    def first_step(self):
        """构造序列1"""

    def second_step(self):
        """构造序列2"""

    def third_step(self):
        """构造序列3"""


class Conductor:
    def __init__(self):
        self.builder = None

    def construction(self, builder):
        self.builder = builder  # 接收传入的建造者类
        [step() for step in (builder.first_step, builder.second_step, builder.third_step)]

    @property
    def result(self):
        return self.builder


if __name__ == '__main__':
    builder = FirstBuilder()
    conductor = Conductor()
    building = conductor.construction(builder)
    result = building.result
