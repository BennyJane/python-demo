# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise

class Blog:
    __shared_title = {}

    def __init__(self):
        print(self.__class__, "is running '__init__()'")
        self.__dict__ = self.__shared_title

    def __str__(self):
        return self.title


# todo 默认继承父类的__init__方法， 实例化的时候，调用 super().__init__()
class MyBlog(Blog):
    """测试子类是否共享"""


class YourBlog(Blog):
    """测试子类是否共享"""

    def __init__(self):
        """"""
        self.title = "C++"


if __name__ == '__main__':
    example1 = Blog()
    example2 = Blog()

    example1.title = "python"
    example2.title = "go"

    print("example1", example1.title)
    print("example2", example2.title)

    example2.title = 'java'

    print("example1", example1.title)
    print("example2", example2.title)

    example3 = MyBlog()
    # example3.title = "C++"

    example4 = YourBlog()

    print("example1", example1.title)
    print("example2", example2.title)
    print("example3", example3.title)
    print("example4", example4.title)
