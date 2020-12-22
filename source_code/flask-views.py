from flask import request


def with_metaclass(meta, *bases):
    # 实现元类 meta 对 *bases 类的继承
    class metaclass(type):
        def __new__(metacls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, "temporary_class", (), {})


http_method_funcs = frozenset(
    ["get", "post", "head", "options", "delete", "put", "trace", "patch"]
)


class View(object):
    methods = None
    decorators = {}

    def dispatch_request(self):
        """子类必须实现的方法"""
        raise NotImplementedError()


class MethodViewType(type):
    # 根据type()接收参数的个数,决定了type函数执行的功能
    # type(classname, parentClasses, attrs) 生成类的功能 ==> __init__() 需要能接收三个参数
    def __init__(cls, name, bases, d):
        super(MethodViewType, cls).__init__(name, bases, d)

        if "methods" not in d:
            methods = set()

            for base in bases:
                if getattr(base, "methods", None):
                    methods.update(base.methods)

            for key in http_method_funcs:
                if hasattr(cls, key):
                    methods.add(key.upper())

            if methods:
                cls.methods = methods


class MethodView(with_metaclass(MethodViewType, View)):
    """最简单的应用类示例"""

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)

        if meth is None and request.method == "HEAD":
            meth = getattr(self, "get", None)

        assert meth is not None, "Unimplemented method %r" % request.method
        return meth(*args, **kwargs)
