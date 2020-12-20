import functools
from types import MethodType

"""
MethodType 的使用方法
- 将外部方法绑定到类 或者 类的实例中
- python2 与 python3 使用方式不同

三种情况说明:
- python2 中 obj.method = MethodType(func, obj, Cls)
- python2 中 obj.method = MethodType(func, Cls)
- python2 中 obj.method = MethodType(func, None, Cls)

python3 中只接收两个参数


参考文章:
https://blog.csdn.net/kk123k/article/details/82684704
"""


class Foo:
    name = 'benny'

    def rename(self, name):
        self.name = name


def set_name(self, name):
    print('set_name', self, type(self))
    self.name = name


"""
=======================================================
将函数绑定到 [类的实例] 上, 成为实例方法:
- 函数中self,指的是 <__main__.Foo object at 0x7f6ab05870b8> 类实例
- 不同类实例之间不受影响, 只会在特定的实例上添加方法
- 绑定的实例方法名可以与添加的函数名不一致

=======================================================
"""


def Test1():
    f1 = Foo()
    f2 = Foo()
    f3 = Foo()

    f1.change_name = MethodType(set_name, f1)
    f2.set_name = MethodType(set_name, f2)

    f1.change_name('jane')
    f2.set_name('tom')
    try:
        f3.set_name('jane')
    except AttributeError as e:
        print(e)
    print(f1.name)
    print(f2.name)
    print(f3.name)


"""
=======================================================
将函数绑定到 [类] 上, 作为类方法:
- 此时, 函数中 self, 其实指的是 cls, <class '__main__.Foo'>

=======================================================
"""


def Test2():
    f1 = Foo()
    f2 = Foo()
    f3 = Foo()

    Foo.set_name = MethodType(set_name, Foo)
    # print(Foo.__dict__)
    f1.set_name('jane')  # 调用的其实是类方法, 设置的name, 也是类属性
    f2.set_name('tom')
    print(f1.name)
    print(f2.name)
    print(f3.name)

    f1.rename('jane1')  # 优先调用实例方法,设置的是实例属性
    f2.rename('jane2')
    print(f1.name)
    print(f2.name)
    print(f3.name)  # 没有实例属性,依旧去访问实例属性


if __name__ == '__main__':
    # Test1()
    Test2()
