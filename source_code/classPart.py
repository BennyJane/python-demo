import os
import inspect


class Part:
    def __init__(self, name):
        self._base = name
        self.name = name

    def area(self):
        print('perpory name')
        setattr(self, self.area.__name__, self.name * 2)
        # return self.name * 2

    @property
    def base(self):
        print('base')
        return self._base


p = Part('benny')
p.area()
print(p.area)
print(p.__dict__)
print(p.__module__)
print(p.__dir__())
print(p.name)
