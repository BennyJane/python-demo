def process_data(data):
    """处理文件"""


"""
大文件处理策略
"""

"""
=================================================================================================
第一种方式: 生成器
=================================================================================================
"""


def read_in_chunks(file_object, chunk_size=1024):
    """借助生成器函数，实现懒加载方式，逐块读取，默认1K"""
    while True:
        f = file_object.read(chunk_size)
        if not f:
            break
        yield f


with open('pathFile.txt') as f:
    for piece in read_in_chunks(f):
        process_data(piece)

# 使用 iter() 方法直接获取生成器
# 读取文件的句柄处理本身就是一个生成器

f = open('target.txt')


def read1K():
    return f.read(1024)


for piece in iter(read1K, ""):
    process_data(piece)

# 处理行文件
for line in open('target.txt'):
    process_data(line)

"""
=================================================================================================
第二种方式: iter() 内置函数
iter(object[, sentinel])
object：支持迭代的集合对象（可迭代对象）;
    - 当只传入object时，
sentinel： 如果传递了该参数，则object必须是一个可调用对象（如：函数）；
    此时，iter创建一个迭代器对象，每次调用这个迭代器对象的__next__方法时，都会调用object

l = [1,2,3,5,6]
for i in iter(l):
    print(i)
=================================================================================================
"""


