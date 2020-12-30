# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 23:38
# Warning    ：The Hard Way Is Easier


_g = "private global var"

g = "public global var"


class A:
    def __init__(self):
        self.public_var = "A public_var"
        # 绑定在实例上的私有属性：实际存储名称 _A__private_var
        self.__private_var = "A private_var"

    def __private_func(self):
        """绑定在类A上的方法，实际存储名称 _A_private_func"""
        print("A private function.")

    def public_func(self):
        print("A public function.")

    def pub_call_private(self):
        self.__private_func()


class B(A):
    def __init__(self):
        A.__init__(self)  # 为了继承A实例属性

    def __private_func(self):
        """绑定在类B上的方法，实际存储名称 _B_private_func; 外部不能通过__private_func调用"""
        print("B private function.")

    def b_pub_call_private(self):
        self.__private_func()  # 类内部触发__private_fun,实际调用 _B_private_func


if __name__ == '__main__':
    pass
    # 查看类属性
    # print(dir(A))  # 触发 __dir__
    # print(type.__dir__(A))  # 检索元类继承链
    # print(object.__dir__(A))  # 检索普通类的继承链
    # print(vars(A))
    # print(A.__dict__)

    a = A()
    print(dir(a))
    print(vars(a))

    # 下面两者调用效果一致  __dir__(self) 接收一个实例参数
    # print(object.__dir__(A()))
    # print(dir(A()))
