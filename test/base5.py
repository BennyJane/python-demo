# -*- coding: utf-8 -*-


l = {"a": 1, "b": 5, "c": 2, "d": 9, "e": 3, }


res = sorted(l.items(),)

s = 'asdf234GDSdsf23'  #排序:小写-大写-奇数-偶数
print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x))))

def keyFunc(x):
    res = (x.isdigit(), 	# 数字返回True， 其他返回False
           x.isupper(),
           x.islower(),
           x.isdigit() and int(x) %2 ==0,	# 判断是否为偶数
           x
          )
    return res

print("".join(sorted(s, key=keyFunc)))


print("10".isdigit())
print("sdfs".isdigit())
print("sdfs".isascii())