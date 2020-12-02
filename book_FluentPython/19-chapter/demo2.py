class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        print("property weight")
        return self.__weight  # 这里不能调用self.weight，避免循环调用

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value  # 设置也不能使用 self.weight
        else:
            raise ValueError('value must be > 0')


class LineItem2:
    def __init__(self, description, weight, price):
        self.__description = description
        self.__weight = weight
        self.__price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        print("property weight")
        return self.__weight  # 这里不能调用self.weight，避免循环调用

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value  # 设置也不能使用 self.weight
        else:
            raise ValueError('value must be > 0')

    @weight.deleter
    def weight(self):
        del self.__weight


class Base:
    data = "the class data attr"  # 类属性

    def __init__(self, name="name"):
        self.name = name
        # self.data = "self.data"

    def data(self):  # 实例方法，也可视作 实例属性的一种
        print("the class method")
        return

    @property  # 特性：类属性的一种
    def data(self):
        print("the class property")
        self.__data = "self .__data"
        return

    @property
    def prop(self):
        return "the prop value"

    def a(self):
        print("method d")

    @staticmethod
    def s():
        print("staticmethod a")

    @classmethod
    def c(cls):
        print("class method c")


if __name__ == '__main__':
    line_item = LineItem('abc', 50, 150)
    # print(line_item.weight)

    line_item = LineItem2('abc', 50, 150)
    # print(line_item.weight)
    # line_item.weight = 200
    # print(line_item.weight)

    b = Base()
    print(vars(b))
    print(vars(Base))
    # print(dir(b))
    print(b.__dict__)
    b.data
    print(b.__dict__)
    b.d()
    b.a()
    b.c()

    Base.a()
    Base.c()
    # Base.d()
