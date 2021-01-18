# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
class BaseViz(object):
    def __init__(self):
        self.name = "benny"

    def site(self, site="wuhan"):
        print("site: {}".format(site))


def get_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [sc for child in cls.__subclasses__() for sc in child.__subclasses__()]
    )
