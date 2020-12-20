import functools

"""
参考文章:
https://wiki.python.org/moin/PythonDecoratorLibrary#Collect_Data_Difference_Caused_by_Decorated_Function
https://www.cnblogs.com/huchong/p/8244279.html
https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p13_using_mataclass_to_control_instance_creation.html

实现思路:
1. 利用python模块加载特性
2. 利用标记变量,保存类第一次实例化后的对象; 从第二次起,不再调用className()类实例化操作, 而是直接返回第一次的结果
    - 标记变量的实现: 全局变量, 类属性, 闭包内置变量, 
    - 具体实现方式(判断逻辑的位置): 函数, 闭包, 类方法, 类的__new__  
3. 通过元类,自定义类的实例化流程, 控制是否调用类自身的 __new__ __init__ 方法 


另一种理解方式：
1. 类多次实例化，但只执行了一次 __new__ __init__
2. 



"""

"""
考虑使用类实现装饰器

class Singleton:
    def __new__(cls, singleton_cls):
        #重新定义类的__new__ __init__方法
        ori__new__ = singleton_cls.__new__
        ori__init__ = singleton_cls.__init__
        def custom__new__(cls, *arg, **kwargs):
            _instance = cls.__dict__.get(["_instance"])
            if _instance is not None:
                cls.__init__ = object.__init__
                return _instance
            cls._instance = object.__new__(cls)
            return cls._instance
        
        singleton_cls.__new__ = custom__new__
        return singleton_cls
        
	def __init__(self, singleton_cls):
        self.

"""


def singleton(cls):
    """Use class as singleton"""
    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kwargs):
        instance = cls.__dict__.get('__instance__')
        if instance is not None:
            return instance

        cls.__instance__ = instance = cls.__new_original__(cls, *args, **kwargs)
        instance.__init_original__(*args, **kwargs)
        return instance

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__
    return cls


def Singleton(cls):
    """重写被装饰类的__new__方法"""
    __new__original__ = cls.__new__
    __init__original__ = cls.__init__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kwargs):
        instance = cls.__dict__.get("__instance__")
        if instance is not None:
            return instance

        cls.__instance__ = instance = __new__original__(cls, *args, **kwargs)
        # TODO 实例字典存储该实例，实现在类实例化后的单例模式
        __init__original__(cls.__instance__, *args, **kwargs)
        return instance

    cls.__new__ = singleton_new
    cls.__init__ = object.__init__
    return cls


# @singleton
@Singleton
class Foo:
    def __new__(cls, *args, **kwargs):
        cls.x = 10
        return object.__new__(cls)

    def __init__(self):
        assert self.x == 10
        self.x = 15


"""
==================================================================================================================
使用类实现单例模式

Singleton1:
- 每次实例化,调用的都是同一个cls对象, 实际内存分配的id是一致的
- 运行调用cls.__dict__ ; 不允许直接向其中添加属性 cls.__dict__['name'] = value
- 每次实例化后,返回的确实是同一个实例对象,但是每次实例化都会重新调用__init__方法; 每次都会覆盖之前的实例属性
- !!!失败, 没有实现只实例化一次,只调用一次当前类的__init__方法


改进方案:
- 第一次实例化后,直接覆盖原来的__init__方法,从第二次实例化开始,调用新的__init__方法
Singleton2:
- 每次实例化,依然会执行__init__方法, 但每次执行的已经不再是原来类的__init__方法
==================================================================================================================
"""


class Singleton1:
    def __new__(cls, *args, **kwargs):  # cls: 由type产生, type(cls):  <class 'type'>
        # print("cls  proxy", cls, id(cls), type(cls), cls.__class__)
        # print("cls", cls.__dict__)
        if cls.__dict__.get('__instance__'):
            return cls.__dict__.get('__instance__')
        instance = object.__new__(cls)
        # 错误的写法, 'mappingproxy' object does not support item assignment
        # cls.__dict__['instance'] = instance
        cls.__instance__ = instance
        return instance

    def __init__(self):
        print('__init__', self)
        self.tag = 10


class Singleton2:
    def __new__(cls, *args, **kwargs):  # cls: 由type产生, type(cls):  <class 'type'>
        # print("cls  proxy", cls, id(cls), type(cls), cls.__class__)
        instance = cls.__dict__.get('__instance__')
        if instance is not None:
            cls.__init__ = object.__init__  # 关键操作: 必须覆盖原始的__init__方法
            return instance
        cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def __init__(self, name=None):
        print('__init__', self)
        self.tag = 10
        self.name = name


"""
==================================================================================================================
使用元类实现单例模式:
- 元类被触发实例化的条件: 被继承使用；
    - 当没有类继承元类时,元类并不会被实例化
    - 每个继承元类的类,都会触发元类被实例化一次, 创建对应的类对象,就是元类中的cls对象
    - 元类的实例化,会在模块内所有代码执行前,被执行（优先模块中其他代码，元类默认会被直接实例化；而且只会被实例化一次）
- 原始类的__init__ 方法只执行了一次
- 类的实例化,都是在直接调用元类的__call__方法，　去触发子类的__new__ __init__ 实例化流程
==================================================================================================================
"""


class SingletonMeta(type):
    # TODO 该方法直接在模块代码被执行前,先被执行
    def __init__(cls, *args, **kwargs):
        # print("SingletonMeta __init__")
        print("SingletonMeta __init__ cls", cls, id(cls))
        cls.__instance = None  # 添加元类实例属性, 其实就是在类
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):  # 子类实例化都会执行该方法
        # print("SingletonMeta __call__")
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        return cls.__instance


class SingletonMeta2(type):
    def __call__(cls, *args, **kwargs):  # 子类后跟(), 进行实例化时, 都会执行该方法
        if not hasattr(cls, "_instance"):
            cls._instance = super().__call__(*args, **kwargs)
            # return cls._instance
        return cls._instance


# FIXME bug: 在类cls上不能添加 __attr 属性,因为该类属性会被认为私有属性, 存入类属性中时, 该属性对应的键会修改了 _class__attr
# cls.__dict__ 内实际存储的是 _SingletonMeta3__instance
class SingletonMeta3(type):
    def __call__(cls, *args, **kwargs):  # 子类后跟(), 进行实例化时, 都会执行该方法
        print('meta32', cls.__dict__, id(cls))
        # FIXME  正确的写法  hasattr(cls, '_SingletonMeta3__instance')
        if not hasattr(cls, "__instance"):
            # cls.__dict__ 内存储的其实是 _SingletonMeta3__instance
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Singleton3(metaclass=SingletonMeta):
    def __init__(self):
        print("singleton3 __init__")
        self.tag = 10

    def __call__(self, *args, **kwargs):
        """类自身的__calls__; 非元类的__call__"""
        # print("singleton3 __call__")


class Singleton31(metaclass=SingletonMeta):
    def __init__(self):
        print("singleton3.1 __init__")
        self.tag = 10


class Singleton32(metaclass=SingletonMeta2):
    def __init__(self):
        print("singleton3.2 __init__")
        self.tag = 10


"""
==================================================================================================================
函数+全局变量: 直接对类的实例化操作进行计数统计, 控制是佛调用 class()

- 全局变量记录类是否已经实例化
- 每次都通过函数来获取类实例


闭包:
- 利用闭包内的作用域, 存储类实例化的标记
- 利用闭包实现类装饰器
==================================================================================================================
"""


class Singleton4:
    def __init__(self, *args, **kwargs):
        self.tag = 10


__instance = None  # 仅仅实现制定类的单例模式


def SingletonFunc(*args, **kwargs):
    global __instance
    if __instance is None:
        __instance = Singleton4(*args, **kwargs)
    return __instance


__multi_instance = {}


def MultiSingletonFunc(cls, *args, **kwargs):
    global __multi_instance
    if cls not in __multi_instance:
        __multi_instance[cls] = cls(*args, **kwargs)
    return __multi_instance[cls]


# =====================================================================
# 使用闭包 取代原始的类
def SingletonWrapper():
    _instance = None

    def wrapper(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = Singleton4(*args, **kwargs)
        return _instance

    return wrapper


newSingleton = SingletonWrapper()


# =====================================================================
# 使用闭包 取代原始的类 ==> 只能针对单个类使用
def SingletonDecorator(cls):
    _instance = None

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = cls(*args, **kwargs)
        return _instance

    return wrapper


if __name__ == '__main__':
    assert Foo().x == 15
    Foo().x = 20
    assert Foo().x == 20
    #  测试单例模式的类
    assert Singleton2().tag == 10
    Singleton2().tag = 20
    print(Singleton2("benny").tag)
    assert Singleton2("tom").tag == 20
    print(Singleton2().name)
    # #  测试元类实现方法
    # assert Singleton3().tag == 10
    # Singleton3().tag = 20
    # print('[元类,检测结果]', Singleton3().tag)
    # assert Singleton3().tag == 20
    #
    # #  测试元类
    assert Singleton32().tag == 10
    Singleton32().tag = 20
    print('[元类32,检测结果]', Singleton32().tag)
    assert Singleton32().tag == 20
    #
    # #  测试闭包实现效果
    # assert newSingleton().tag == 10
    # newSingleton().tag = 20
    # print('[闭包,检测结果]', newSingleton().tag)
    # assert newSingleton().tag == 20
