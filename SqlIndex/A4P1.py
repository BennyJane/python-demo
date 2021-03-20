import time
import sqlite3
import random
from settings import DB_NAMES

from utils import get_average
from utils import load_upc_data

# 查询语句
SELECT_SQL = "SELECT * FROM Parts WHERE '{}' = {};"
# 执行次数
EXECUTE_NUMS = 100

# 生成索引
CREATE_INDEX = "CREATE INDEX idxNeedsPart ON Parts ( needsPart );"
# 删除索引
DROP_INDEX = "DROP INDEX idxNeedsPart;"


def execute_query():
    upc_data = load_upc_data()  # 加载UPC数据
    random.shuffle(upc_data)  # 打乱原始数据
    for db_name in DB_NAMES:  # 遍历5个数据库
        q1_time_sum = 0  # 记录查询1的执行总时间
        q2_time_sum = 0  # 记录查询2的执行总时间
        print(f"Opening {db_name}")
        conn = sqlite3.connect(db_name)
        for _ in range(EXECUTE_NUMS):
            # 每次执行前，都生成新的随机值
            select_q1 = SELECT_SQL.format("partNumber", int(upc_data.pop()))
            select_q2 = SELECT_SQL.format("needsPart", int(upc_data.pop()))
            time_point1 = time.time()
            conn.execute(select_q1)  # 执行查询1
            time_point2 = time.time()
            conn.execute(select_q2)  # 执行查询2
            time_point3 = time.time()
            q1_time_sum += (time_point2 - time_point1)  # 累计查询1的时间
            q2_time_sum += (time_point3 - time_point2)  # 累计查询2的时间
        print(f"Average query time for Query Q1: {get_average(q1_time_sum)} ms")
        print(f"Average query time for Query Q2: {get_average(q2_time_sum)} ms")
        conn.close()  # 关闭数据库连接
        print(f"Closing {db_name}")


def main():
    print("Executing Part 1\n")

    print("Executing Task A")
    execute_query()

    # 给每个数据库加上索引
    print("\nCreating Index")
    for db_name in DB_NAMES:
        conn = sqlite3.connect(db_name)
        conn.execute(CREATE_INDEX)
        conn.close()

    print("\nExecuting Task B")
    execute_query()

    # 删除现有的索引
    print("\nDrop Index")
    for db_name in DB_NAMES:
        conn = sqlite3.connect(db_name)
        conn.execute(DROP_INDEX)
        conn.close()


if __name__ == '__main__':
    main()
