# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

"""
从抽象的高级 逐步具体化

"""


class Building(object):
    """最终成果的抽象： 属性"""

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return "Floor: %s | Size: %s" % (self.floor, self.size)


# 整体的规划者
class Director(object):
    """建造者：负责总体规划与创建流程"""

    def __init__(self):
        """建造者的抽象：需要的功能"""
        self.builder = None

    def construct_building(self):
        """具体创建Building类属性的过程"""
        self.builder.new_building()  # 实例化 Building
        self.builder.build_floor()  # 添加属性 floor
        self.builder.build_size()  # 添加属性 size

    def get_building(self):
        """返回最终的成果：Building的实例"""
        return self.builder.building


# 抽象的工人
class Builder(object):
    """建筑工人：具体实现者"""

    def __init__(self):
        """todo 每个具体的建筑工人都负责建造具体的建筑"""
        self.building = None

    def new_building(self):
        """负责的建筑对象"""
        self.building = Building()


# 具体的实施者：各自负责不同个功能
# 两个负责不同类型建筑的建筑工人
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = "One"

    def build_size(self):
        self.building.size = "Big"


class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = "More then One"

    def build_size(self):
        self.building.size = "Small"


if __name__ == '__main__':
    director = Director()  # 规划先行
    director.builder = BuilderHouse()  # 挑选具体的建筑工人
    director.construct_building()  # 开始建造
    building = director.get_building()  # 返回成果
    print(building)
