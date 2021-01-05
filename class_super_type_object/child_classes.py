# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

class BaseViz(object):
    def __init__(self):
        self.name = "benny"

    def site(self, site="wuhan"):
        print("site: {}".format(site))


class FirstChild(BaseViz):

    def site(self, site="shanghai"):
        print("site: {}".format(site))


class SecondChild(BaseViz):

    def site(self, site="beijing"):
        print("site: {}".format(site))


class ThreeChild(BaseViz):

    def site(self, site="henan"):
        print("site: {}".format(site))


def get_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [sc for child in cls.__subclasses__() for sc in child.__subclasses__()]
    )


VIZ_TYPE_DENYLIST = ['FirstChild', ]

all_child_types = {
    c.__name__: c
    for c in get_subclasses(BaseViz) if c.__name__ not in VIZ_TYPE_DENYLIST
}

# 统计当前模块内BaseViz类的所有子类；并排除

if __name__ == '__main__':
    print(all_child_types)
