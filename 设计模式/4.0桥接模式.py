# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self._radius = radius
        self._drawing_api = drawing_api  # 出入的是类的实例

    # 下级的， 具体的实现  ==》 无法合并的属性，差异化的属性
    def draw(self):
        self._drawing_api.draw_circle(self.x, self.y, self._radius)

    # 高级别，抽象的 ==》 抽象出来的共同属性
    def scale(self, pct):
        self._radius *= pct


# 具体的实现
class DrawingAPI1(object):
    def draw_circle(self, x, y, radius):
        print("API1.circle at {}:{} radius {}".format(x, y, radius))


class DrawingAPI2(object):
    def draw_circle(self, x, y, radius):
        print("API1.circle at {}:{} radius {}".format(x, y, radius))


def main():
    shapes = (
        # todo 注意，这儿必须传入类的实例
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(1, 2, 3, DrawingAPI2()),
    )

    for shape in shapes:
        shape.scale(2.5)  # 抽象出来的共同属性： 高级属性
        shape.draw()


if __name__ == '__main__':
    main()
