# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise


class Handler(object):
    def successor(self, successor):
        """todo 核心设计点：指定下一步负责人"""
        self.successor = successor


class ConcreteHandler1(Handler):
    def handle(self, request):
        if 0 < request <= 10:
            print("in handler1")
        else:
            self.successor.handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request):
        if 10 < request <= 20:
            print("in handler2")
        else:
            self.successor.handle(request)


class ConcreteHandler3(Handler):
    def handle(self, request):
        if 20 < request <= 30:
            print("in handler3")
        else:
            print('end of chain, no handler for {}'.format(request))


class Client:
    def __init__(self):
        self.h1 = ConcreteHandler1()
        self.h2 = ConcreteHandler2()
        self.h3 = ConcreteHandler3()

        # todo 第一次调用 successor方法, 指定了后续的责任函数，同时该方法被覆盖为属性self.successor = next_func
        self.h1.successor(self.h2)
        self.h2.successor(self.h3)

    def core(self, data):
        for item in data:
            self.h1.handle(item)


if __name__ == '__main__':
    client = Client()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.core(requests)
