from functools import wraps


def outer(f):
    a = 100

    @wraps(f)
    def inner(*args, **kwargs):
        res = f(a, *args, **kwargs)
        return res

    return inner


@outer
def base(a):
    return a


result = base()
print(result)

Top = type("Top", (), {"name": "benny"})

top = Top()
print(top.name)


class MetaC(type):
    def __new__(cls, name, bases, attrs):
        '''
        :param args:  name 与 父类的元祖()
        :param kwargs: 属性字典
        :return:
        '''
        print(name)
        print(bases)
        print(attrs)
        return super(MetaC, cls).__new__(cls, name, bases, attrs)

    def __call__(self, *args, **kwargs):
        # fixme 元类的该方法,必须返回 元类的实例 ==> 就是生成继承当前元类的普通类
        print("call meta")
        # 非绑定方法, 直接调用type方法,需要传入首个参数 self
        # return type.__call__(self, *args, **kwargs)
        # return super(MetaC, self).__call__(*args, **kwargs)
        return self.__new__(self, args, kwargs)


'''
本质原因: 
当py程序载入的时候, 定义的普通类会查找自己继承的元类,并调用__new__方法,完成当前类的定义;
实例化普通类的时候, 实际上 调用的是 元类的 __call__ 方法 ==> 
        当元类的__call__ 方法没有返回普通类,将不会调用 __init__ 方法,也不会产生实例对象
http://c.biancheng.net/view/2380.html
'''


class baseClass(metaclass=MetaC):
    name = "benny"

    def __init__(self):
        pass

    def age(self):
        print("age")
        pass

    def target(self):
        print("target")
        return 'target'

    # def __call__(self, *args, **kwargs):
    #     print("call")


class finalClass(baseClass):
    pass


r = baseClass()
r.age()

f = finalClass()
print(f)
f.age()
print(hasattr(f, 'age'))


# f.age()


class Singletion:

    def age(self):
        print("age singletion")

    def __call__(self, *args, **kwargs):
        print('singletion call')

    pass

# singletion = Singletion()
# singletion.age()
