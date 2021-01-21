# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

MINI14 = "1.4GHz MAC mini"


class AppleFactor:
    # TODO 嵌套类，可以避免该类被直接实例化
    class MacMini14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = ("Model: {}".format(MINI14),
                    "Memory: {}GB".format(self.memory),
                    "Hard Disk: {}GB".format(self.hdd),
                    "Graphics Card: {}".format(self.gpu),
                    )
            return "\n".join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))


if __name__ == '__main__':
    afac = AppleFactor("A")
    mac_mini = afac.build_computer(MINI14)
