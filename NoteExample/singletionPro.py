def _NOTE():
    file = """
    参考链接: 
    https://blog.csdn.net/weixin_40406241/article/details/89576600?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param#%E5%9B%9B%E3%80%81%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F%E7%9A%84%E5%AE%9E%E7%8E%B0
    https://www.cnblogs.com/tkqasn/p/6524879.html
    """
    return ""


'''
** 不传参时就是同一个对象，如果传了其他参数就另外生成一个对象
'''

# settings文件：
IP = '1.1.1.1'
PORT = 3306


# 单例实现文件：
# from settings import IP, PORT


def Singleton(cls):
    __instance = cls(IP, PORT)

    def inner(*args, **kwargs):
        if args or kwargs:
            obj = cls(*args, **kwargs)
            return obj
        return __instance

    return inner


@Singleton
class MySQL:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


obj1 = MySQL()
obj2 = MySQL()
obj3 = MySQL()
print(obj1)  # <__main__.MySQL object at 0x000000838F7A6710>
print(obj2)  # <__main__.MySQL object at 0x000000838F7A6710>
print(obj3)  # <__main__.MySQL object at 0x000000838F7A6710>

'''
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
'''

# 从配置文件导入配置
IP = '1.1.1.1'
PORT = 3306


class Mymeta(type):
    # self 就是MySQL这个类
    def __init__(self, class_name, class_bases, class_dic):
        self.__instance = self(IP, PORT)

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            obj = self.__new__(self)
            self.__init__(obj, *args, **kwargs)
            return obj
        else:
            return self.__instance


class MySQL(metaclass=Mymeta):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


obj1 = MySQL()  # <__main__.MySQL object at 0x0000000C02800B00>
obj2 = MySQL()  # <__main__.MySQL object at 0x0000000C02800B00>
obj3 = MySQL()  # <__main__.MySQL object at 0x0000000C02800B00>
print(obj1)
print(obj2)
print(obj3)
