# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/30 13:32
# Warning    ：The Hard Way Is Easier
"""
混入类
"""


class FirstMixins(object):
    """混入类： 在header列表末尾添加data1"""

    def get_header(self):
        print("run FirstMixins.get_header")
        ctx = super(FirstMixins, self).get_header()
        ctx.append("data1")  # 该方法第一个被调用，但最后一个被执行完毕
        return ctx


class SecondMixins(object):
    """混入类： 在header列表头部添加data2"""

    def get_header(self):
        print("run SecondMixins.get_header")
        ctx = super(SecondMixins, self).get_header()
        ctx.append("data2")
        # ctx.insert(0, "data2")
        return ctx


class Header(object):
    header = []

    def get_header(self):
        print("run Header.get_header")
        return self.header


class Final(FirstMixins, SecondMixins, Header):
    def get_header(self):
        return super(Final, self).get_header()


class Final2(Header, FirstMixins, SecondMixins):
    """在父类搜索到同名方法后，就会停止继续搜索，除非调用super方法"""

    def get_header(self):
        return super(Final2, self).get_header()


if __name__ == '__main__':
    f2 = Final2()
    res = f2.get_header()
    print("Final2 调用结果", res)

    f = Final()
    res = f.get_header()
    print(res)
