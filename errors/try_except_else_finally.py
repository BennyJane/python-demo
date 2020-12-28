# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/24 19:34
# Warning    ：The Hard Way Is Easier

def base1():
    """测试try except"""
    try:
        raise KeyError("this is a KeyError error.")
        # return
    except KeyError as e:
        print(e)
        return  # 此处： 无法直接使用return 终止执行，实现跳过后续代码的目的
    except Exception as e:
        print(e)
    else:
        print("else ...")
    finally:
        # try ... except ... 代码块内，无论是否报错以及错误是否被捕捉，无论是否使用了return语句，finally内的代码都会被执行。
        # 但使用return后， finally后的代码不会被执行
        print("finally ...")

    # print("end ...")


def base2():
    print("start ...")
    # return  ==> 正确执行return后，直接返回，后续都不执行
    try:
        print("try ...")
        # raise KeyError("key error...")
        # return ==> 正确执行return后，先执行else块，再执行finally； 不执行try...except结构外的代码
    except Exception as e:
        print("except ...", e)
        # return ==> 正确执行return后，直接执行finally块； 不执行try...except结构外的代码
    else:
        print("else ...")
        # return ==> 正确执行return后，直接执行finally块； 不执行try...except结构外的代码
    finally:
        print("finally ...")
        # return ==> 正确执行return后， 不执行try...except结构外的代码

    print("end ...")  # try结构体中有return（无论出现在哪儿），则该段代码不执行

    # return ==> 返回


if __name__ == '__main__':
    base1()
    print()
    base2()
