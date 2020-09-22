def _NOTE():
    file = """
    参考链接: 
    https://blog.csdn.net/weixin_40406241/article/details/89576600?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param#%E5%9B%9B%E3%80%81%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F%E7%9A%84%E5%AE%9E%E7%8E%B0
    
    """
    return ""


'''
__new__ 方法实现丹利
'''


# FIXME 没有办法实例化; __init__() 实例化传入参数会报错
class FirstType:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(FirstType, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    # def __init__(self, name):
    #     self.name = name


first1 = FirstType()
first2 = FirstType()
print(first1 is first2)


class Child(FirstType):
    # def __init__(self, name):
    #     self.name = name
    pass


# first1 = Child("tom")
# first2 = Child("benny")
# print(first1 is first2)

'''
2: __new__ 方法实现丹利
'''


# -*- coding: utf8 -*-

class Singleton(object):
    def __init__(self, name):
        self.name = name
        print('entrance of __init__')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1 = Singleton("tom")
    s2 = Singleton("benny")
