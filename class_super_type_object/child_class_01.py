# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
from class_super_type_object.child_class_base import BaseViz
from class_super_type_object.child_class_base import get_subclasses


class FirstChild(BaseViz):

    def site(self, site="shanghai"):
        print("site: {}".format(site))


class SecondChild(BaseViz):

    def site(self, site="beijing"):
        print("site: {}".format(site))


class ThreeChild(BaseViz):

    def site(self, site="henan"):
        print("site: {}".format(site))


first_file_children = {
    c.__name__: c
    for c in get_subclasses(BaseViz)
}

# 统计当前模块内BaseViz类的所有子类；并排除

if __name__ == '__main__':
    print(first_file_children)
