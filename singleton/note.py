import os

"""
python 中对象实例化步骤
https://www.cnblogs.com/111testing/p/13660863.html
## 从内存角度解释
实例化所经历的步骤: 
     1.类名() 之后的第一个事儿 :开辟一块儿内存空间
     2.调用 __init__ 把空间的内存地址作为self参数传递到函数内部
     3.所有的这一个对象需要使用的属性都需要和self关联起来
     4.执行完init中的逻辑之后,self变量会自动的被返回到调用处(发生实例化的地方)


"""

if __name__ == '__main__':
    print(os.path.curdir)
