# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/14 17:02
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

# 定义一个个普通方法,注意方法的参数是self.
def selfMethod(self):
    print("this %s's content is ............." % self.name)

def Test1():
    book = Book("a", "...")
    book.test = types.MethodType(selfMethod, book)
    # print(dir(book))
    # print(vars(book))
    # Book.bkContent = None
    # print(Book.__dict__)
    # print(book.bkContent)
    del Book.bkContent
    del Book.C_Content
    del Book.S_Content
    del Book.showInfoself
    del book.bkContent
    print([k for k in vars(Book).keys()])
    del book.name
    del book.test
    # delattr(book, "bkContent")
    # print(dir(book))
    print(book.__dict__)
    print(vars(book))

    # book.bkContent()


if __name__ == '__main__':
    Test1()
