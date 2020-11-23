def process_data(data):
    """处理文件"""


chunk_size = 1024
with open('./target.txt', 'rb') as f:
    for chunk in iter((lambda: f.read(chunk_size)), b""):
        print(chunk)
        process_data(chunk)

with open('./target.txt', 'r') as f:
    for chunk in iter(lambda: f.read(chunk_size), ""):
        print(chunk)
        process_data(chunk)


def someFunc():
    return f.read(chunk_size)


with open('./target.txt', 'r') as f:
    for chunk in iter(someFunc, ''):
        process_data(chunk)

res = iter(someFunc, '')
print(type(res))
print(dir(res))
if __name__ == '__main__':
    pass
