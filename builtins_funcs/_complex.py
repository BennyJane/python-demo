# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

# 虚数 complex
_complex = complex(1, 1)
complex_obj_j = 10.0 + 1.0j
complex_obj_J = 0.0 + 1.0J
complex_obj_J_2 = 1.0 + 1.0J

# 计算方法
# 参考文章： https://blog.csdn.net/weixin_43718414/article/details/85778572

if __name__ == '__main__':
    default_complex = complex()
    print("[默认的复数], real, imag:", default_complex, default_complex.real, default_complex.imag)
    print("[复数类型]：", _complex)  # (1+1j)
    print("[复数.实部]：", _complex.real)
    print("[复数.虚部]：", _complex.imag)
    print("[复数.共轭复数]：", _complex.conjugate())
    print(complex_obj_j, type(complex_obj_j))
    print(complex_obj_J)
    print(complex_obj_J_2)
