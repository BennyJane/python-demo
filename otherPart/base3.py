# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/14 16:49
# Warning    ：The Hard Way Is Easier

import types


class Book(object):
    def __init__(self, name, page):
        self.name = name
        self.page = page

    def showInfoself(self):
        print("book info:{0},{1}".format(self.name, self.page))


# 定义一个个普通方法,注意方法的参数是self.
def bkContent(self):
    print("this %s's content is ............." % self.name)


# 定义一个类方法
@classmethod
def C_Content(cls):
    print("这是类方法")


# 定义一个静态方法
@staticmethod
def S_Content():
    print("这是静态方法")


# 定义一个无参的普通方法
def o_Content(self):
    print("这是普通无参方法")


book3 = Book("小时代", 555)

# TODO 这种方式不行;实例的设置属性，优先添加在实例上，而不是类上；但方法都是类属性
# 这样绑定的方法，调用的时候，不会直接添加self
# book3.bkContent = bkContent

book3.bkContent = types.MethodType(bkContent, book3)  # 里面的参数是方法名，对象名
book3.bkContent()  # this 小时代's content is .............

a = types.MethodType(bkContent, book3)
a()  # this 小时代's content is .............

book3.a = types.MethodType(bkContent, book3)  # 注意前面的引用名，可以自定义，但是与调用名要一致
book3.a()  # this 小时代's content is .............

Book.C_Content = C_Content
Book.C_Content()  # 这是类方法
book4 = Book("红楼梦", 1113)
book4.C_Content()  # 实例调用类方法：这是类方法

book5 = Book("水浒传", 222)
Book.S_Content = S_Content
Book.S_Content()  # 这是静态方法
book5.C_Content()  # 这是类方法


Book.o_Content = o_Content
Book.o_Content()  # 没有报错：这是普通无参方法
book6 = Book("一地鸡毛", 211)
book6.o_Content()
