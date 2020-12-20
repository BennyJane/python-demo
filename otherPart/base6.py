# -*- coding: utf-8 -*-


l = {"a": 1, "b": 5, "c": 2, "d": 9, "e": 3, }

if __name__ == '__main__':
    del l["a"]
    res = l.fromkeys("DA", 11)
    print(res)
    print(l.keys)

    if "a" in l.keys():
        print(True)

    print(l.items())
    print(type(l.items()))
    print(type(l.keys()))
    print(l.pop("sdfs", "12345"))
    print(l.popitem())


    print(l)
    pass
