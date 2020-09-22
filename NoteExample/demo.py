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
    def __new__(cls, *args, **kwargs):
        '''
        :param args:  name 与 父类的元祖()
        :param kwargs: 属性字典
        :return:
        '''
        print(args)
        print(kwargs)
        return super(MetaC, cls).__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("call meta")
        # return type.__call__(self, *args, **kwargs)


class Field(object, metaclass=MetaC):
    name = "benny"

    def __init__(self):
        pass

    def age(self):
        print("age")
        pass

    def target(self):
        print("target")

    # def __call__(self, *args, **kwargs):
    #     print("call")


f = Field()
print(f)
# f.age()


class Singletion:

    def age(self):
        print("age singletion")

    def __call__(self, *args, **kwargs):
        print('singletion call')
    pass

# singletion = Singletion()
# singletion.age()
