def process_data(data):
    """处理文件"""

chunk_size = 1024
with open('target.txt', 'rb') as f:
    for chunk in iter((lambda: f.read(chunk_size)), ""):
        process_data(chunk)



if __name__ == '__main__':
    pass

