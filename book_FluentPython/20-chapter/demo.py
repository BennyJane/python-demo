class Quantity:
    __counter = 0  # <1>

    def __init__(self):
        cls = self.__class__  # <2>
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)  # <3>
        cls.__counter += 1  # <4>

    def __get__(self, instance, owner):  # <5>
        return getattr(instance, self.storage_name)  # <6>

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)  # <7>
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()  # <8>
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def base(self):
        raise Exception("base")


if __name__ == '__main__':
    # LineItem.weight

    LineItem.base
    print(vars(LineItem))