def _NOTE():
    file = """
    参考链接: 
    https://blog.csdn.net/weixin_40406241/article/details/89576600?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param#%E5%9B%9B%E3%80%81%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F%E7%9A%84%E5%AE%9E%E7%8E%B0
    https://www.cnblogs.com/tkqasn/p/6524879.html
    """
    return ""


'''
** 在导入时，类对象已经被创建；每次实例化类的时候，调用 __new__() 方法，返回已经生成的类(调用type的__new__生成的)，再调用__init__方法实例化
** 在导入时，类对象会查找继承的元类，最终调用type.__new__(), __init__()方法，完成新类的创建；
** 类实例化( SomeClass() ), 其实调用的是继承的元类的 __call__() 类方法 
    ==》 利用该特性实现单例 
    ==》新的调用顺序： 父类元类的 __call__ --> __new__(自身 or 父类) --> __init__(自身 or 父类)
** 普通类实例化的时候，不再调用元类的 __new__等方法； 只会调用自身的 __new__ __init__ 方法
'''

'''
__new__ 方法实现:
1. 在调用 __new__ 方法的时候，记录实例化的次数
2. 只实例化了一个对象；但每次实例化该类，会重新调用 __init__方法，覆盖之前的属性or方法： 允许多次实例化
'''


# FIXME 没有办法实例化; __init__() 实例化传入参数会报错
class FirstType:
    # 重写 __new__() 方法的时候， 需要接收cls,*args, **kwargs 三个参数
    # 调用父类的__new__(cls)的时候，只需要传入一个参数
    def __new__(cls, *args, **kwargs):  # 该方法是一个类方法： cls
        print(" __new__ ...")
        # todo 生成该类的不同写法：
        if not hasattr(cls, '_instance'):
            # fixme： 调用__new__() 方法的时候传入过多的参数，会造成该类无法调用__init__ 实例化
            # cls._instance = super(FirstType, cls).__new__(cls, *args, **kwargs)
            # cls._instance = super(FirstType, cls).__new__(cls)    # super() 的两种写法
            # cls._instance = super().__new__(cls)  # 简写
            # 直接调用父类的__new__()方法； fixme： 不能使用 type.__new__(cls) ？？
            cls._instance = object.__new__(cls)
            print('[first instance]: ', cls._instance, id(cls._instance.__class__))
        return cls._instance

    def __init__(self, name):
        self.name = name

    def age(self):
        print(f'{self.name} of age is ...')


def test1():
    initClass = globals()["FirstType"]
    print(id(initClass), initClass)

    first1 = FirstType("tom")
    first2 = FirstType("jane")
    print(first1.__class__, id(first1.__class__))
    print(first1 is first2)
    first1.age()


# test1()
'''
__new__： 限制实例化次数
'''


class FirstType2:
    __instance = None  # 记录是否已经通过__new__实例化
    Instance = False  # 记录是否已经通过 __init__ 方法初始化

    def __init__(self, name):
        if not self.Instance:
            self.name = name
            self.Instance = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


def test2():
    first1 = FirstType2("tom")
    first2 = FirstType2("jane")
    print(first1 is first2)
    print(first1.name)
    print(first2.name)


# test2()
'''
使用元类： 限制实例化次数
** 原理： 类实例化的时候，调用父类中元类的 __call__() 方法
** bug: 
'''


class Singleton(type):
    # todo 该属性绑定在 Singleton类上
    _instance = None

    #  无关代码，可删除
    def __new__(cls, *args, **kwargs):
        print("Singleton: __new__")
        return type.__new__(cls, *args, **kwargs)
        # return super().__new__(cls, *args, **kwargs)

    # noinspection PyTypeChecker
    def __call__(cls, *args, **kwargs):
        # todo cls 指代的是 子类 Child， 此时类 cls 并没有该属性 ==》 没有报错的原因：
        # 查找到了继承的父类 Singleton 有该属性； 修改为 cls.instance 就会报错 no attribute 'instance'
        if cls._instance is None:  # hasattr(cls, "_instance"): || if Singleton._instance == None
            # cls._instance = super().__call__(*args, **kwargs)
            # cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
            # todo 等效写法
            Singleton._instance = object.__new__(cls)  # 只返回了实例，但没有调用 __init__
            cls.__init__(Singleton._instance, *args, **kwargs)
        return cls._instance


class Child(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


def test3():
    first1 = Child("tom")
    first2 = Child("jane")
    print("[两次实例化是否为同一个实例对象]：", first1 is first2)
    print(first1.name)
    print(first2.name)
    # print(Singleton._instance)
    # print(first1._instance)


# test3()

'''
使用元类： 
** 使用元类创建类执行顺序： 继承的元类 __new__() --》 __init__() --> __call__() 触发子类的实例化流程|直接返回子类的实例，则不再向下调用 --> 子类的 __new__() __init__()
'''


class MetaClass(type):
    # 无关代码可删除
    def __new__(cls, *args, **kwargs):
        print("MetaClass: __new__")
        return type.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("MetaClass: __init__")
        # 给实例 metaChild 添加了类属性 _instance
        self._instance = None  # 此处的 self， 就是元类 metaClass的实例，也就是创建的子类 metaChild;
        super(MetaClass, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            # todo 触发子类 __new__ __init__ 方法
            self._instance = super().__call__(*args, **kwargs)
        return self._instance  # 将不会再调用 __new__ __init__ 方法


class metaChild(metaclass=MetaClass):
    def __new__(cls, *args, **kwargs):
        print("metaChild __new__")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


def test4():
    print(dir(metaChild))
    first1 = metaChild("tom")
    first2 = metaChild("jane")
    print("[两次实例化是否为同一个实例对象]：", first1 is first2)
    print(first1.name)
    print(first2.name)


# test4()

'''
模块导入
** 模块就是天然的单例模式，因为模块在第一次导入时，会生成.pyc文件，后续导入时，直接载入 .pyc 文件，不会再执行代码
'''


class SingletonModule:
    pass


singletonModule = SingletonModule()

'''
类 | 类方法
'''


class ClassMethod:
    __instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def getSingleton(cls, *args, **kwargs):
        if cls.__instance is None:
            # fixme 可以传入参数
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


def test5():
    first1 = ClassMethod.getSingleton("tom")
    first2 = ClassMethod.getSingleton("jane")
    print("[两次实例化是否为同一个实例对象]：", first1 is first2)
    print(first1.name)
    print(first2.name)


# test5()

'''
装饰器(类装饰器)
'''


def outer(cls):
    __instance = None

    def inner(*args, **kwargs):
        nonlocal __instance
        if __instance is None:
            __instance = cls(*args, **kwargs)
        return __instance

    return inner


@outer
class decorationClass:
    def __init__(self, name):
        self.name = name


def test6():
    first1 = decorationClass("tom")
    first2 = decorationClass("jane")
    print("[两次实例化是否为同一个实例对象]：", first1 is first2)
    print(first1.name)
    print(first2.name)


test6()
