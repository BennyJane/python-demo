import json
import sqlite3

from settings import COUNTRY_DATA, DB_NAMES
from settings import UPC_DATA


# 读取地区数据
def load_country_data():
    with open(COUNTRY_DATA, 'r', encoding='utf-8') as f:
        country_data_str = f.read()
    country_data_list = json.loads(country_data_str)
    return country_data_list


# 读取UPC数据
def load_upc_data():
    upc_data = []
    with open(UPC_DATA, 'r', encoding='utf-8') as f:
        f.readline()  # 跳过第一行
        all_rows = f.readlines()  # 剩余 1048576行数据
    for row in all_rows:
        ean = row.split(",")[0]  # 获取数值部分
        ean = ean.replace("null", "").strip()  # 排除 null 值影响
        if ean:
            upc_data.append(ean)
    return upc_data


def change_index(change_index_sql):  # 修改所有数据库的索引，接收修改索引的SQL语句
    print("chang index...")
    try:
        for db_name in DB_NAMES:
            conn = sqlite3.connect(db_name)
            conn.execute(change_index_sql)
            conn.close()
    except Exception as e:
        print(e)


def get_average(time_sum, total=100, num=5):
    # 秒 转 毫秒，并保留5位小数
    return round(time_sum / total * 1000, num)
