class A:
    def __init__(self, x):
        # self.x = x
        self.__dict__['x'] = x

    def __getattribute__(self, item):
        print('开始执行 getattribute')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        # setattr(self, key, value)
        # print("__setattr__")
        # object.__setattr__(self, key, value)


if __name__ == '__main__':
    a = A("test")
