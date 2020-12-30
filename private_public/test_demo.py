# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/29 23:40
# Warning    ：The Hard Way Is Easier

from private_public.module_private import *

args = locals()


def test_module():
    # 无法通过 from module import * 导入 _private __private
    #  __all__ 具有更高的优先级，来决定变量是否可以被 from module import * 导入
    assert "_private" not in args.keys()
    assert "__private" not in args.keys()
    assert "public_not_in_all" not in args.keys()
    assert "__private_in_all" in args.keys()
    assert "public" in args.keys()

    # 可以直接导入模块，然后通过模块访问私有变量
    import private_public.module_private as module_dict
    assert hasattr(module_dict, "_private") is True
    assert hasattr(module_dict, "__private") is True

    # 模块内私有变量可以直接被显式导入
    from private_public.module_private import _private
    from private_public.module_private import __private
    assert _private is not None
    assert __private is not None
