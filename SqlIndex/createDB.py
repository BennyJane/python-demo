import os
import random
import sqlite3
import copy

from settings import DB_NAMES
from settings import DB_NUMS
from settings import CREATE_SQL
from settings import INSERT_SQL
from utils import load_upc_data
from utils import load_country_data

# 生成数据库
def create_db(name: str, num: int):
    os.remove(name)  # 每次删除数据库，并重新创建
    conn = sqlite3.connect(name)  # 连接数据库
    conn.execute(CREATE_SQL)  # 创建数据表

    # 获取地区与UPC数据
    country_data_list = load_country_data()
    upc_data = load_upc_data()
    upc_data_copy = copy.deepcopy(upc_data)  # 深拷贝，获取第二份UPC数据，用于生成needsPart

    print("数据库名称: {}; 插入数据量： {}".format(name, num))
    # 打乱数据排列
    random.shuffle(country_data_list)
    random.shuffle(upc_data)
    random.shuffle(upc_data_copy)
    # 根据num值，确定插入数据表的数据
    for _ in range(num):
        partNumber = upc_data.pop(0)    # 从UPC数据获取数值
        partPrice = random.randint(1, 100)  # 随机生成1-100的数据
        needsPart = upc_data_copy.pop(0)
        madeInTEXT = random.choice(country_data_list)["Code"]   # 获取地区缩写字母
        # 插入数据，并捕获主键已存在的异常
        while True:
            try:
                insert_sql = INSERT_SQL.format(partNumber, partPrice, needsPart, madeInTEXT)
                conn.execute(insert_sql)
            except Exception as e:  # 主键重复
                partNumber = upc_data.pop(0)
                print(e)
            else:  # 没有异常就执行下一步操作
                break
    print("insert done!")
    conn.commit()  # 提交，真正插入数据库
    conn.close()    # 关闭数据库连接
    print("commit done!")


def main():
    # 遍历生成5个数据库文件
    for index, db in enumerate(DB_NAMES):
        nums = DB_NUMS[index]
        create_db(db, nums)
        # break


if __name__ == '__main__':
    main()
