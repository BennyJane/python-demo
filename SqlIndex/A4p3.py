import random
import sqlite3
import time
from settings import DB_NAMES
from utils import load_country_data
from utils import get_average
from utils import change_index

# PART3 查询随机选择的国家中最大price的值
EXECUTE_NUMS = 100
SELECT_SQL = "SELECT * FROM Parts WHERE madeIn  = '{}' order by partPrice desc limit 1;"
# SELECT_SQL = "SELECT MAX(partPrice) FROM Parts WHERE madeIn  = '{}';"
# 创建索引: idxMadeIn
CREATE_INDEX = "CREATE INDEX idxMadeIn ON Parts ( MadeIn );"
DROP_INDEX = "DROP INDEX idxMadeIn;"

# 创建索引: idxPartPrice
CREATE_INDEX2 = "CREATE INDEX idxPartPrice ON Parts ( partPrice );"
DROP_INDEX2 = "DROP INDEX idxPartPrice;"

# 创建索引: idxPartPriceAndMadeIn
CREATE_INDEX3 = "CREATE INDEX idxPartPriceAndMadeIn ON Parts ( partPrice, madeIn );"
DROP_INDEX3 = "DROP INDEX idxPartPriceAndMadeIn;"


def execute_query():
    origin_data = load_country_data()
    random.shuffle(origin_data)
    for db_name in DB_NAMES:
        conn = sqlite3.connect(db_name)
        print(f"Opening {db_name}")
        time_point1 = time.time()
        for _ in range(EXECUTE_NUMS):
            select_q1 = SELECT_SQL.format(random.choice(origin_data)["Code"])
            conn.execute(select_q1)
        time_point2 = time.time()
        for _ in range(EXECUTE_NUMS):
            select_q2 = SELECT_SQL.format(random.choice(origin_data)["Code"])
            conn.execute(select_q2)
        time_point3 = time.time()
        q1_time_sum = (time_point2 - time_point1)
        q2_time_sum = (time_point3 - time_point2)
        print(f"Average query time for Query Q1: {get_average(q1_time_sum)} ms")
        print(f"Average query time for Query Q2: {get_average(q2_time_sum)} ms")
        conn.close()
        print(f"Closing {db_name}")


# 第二种索引最快，
def main():
    print("Executing Part 3\n")

    print("Executing Task A")
    execute_query()

    # 测试第一种索引设置
    print("\nCreating Index1")
    change_index(CREATE_INDEX)

    print("\nExecuting Task B")
    execute_query()

    print("\nDrop Index")
    change_index(DROP_INDEX)

    # 测试第二种索引设置
    print("\nCreating Index2")
    change_index(CREATE_INDEX2)

    print("\nExecuting Task B")
    execute_query()

    print("\nDrop Index2")
    change_index(DROP_INDEX2)

    # 测试第三种索引设置
    print("\nCreating Index3")
    change_index(CREATE_INDEX2)

    print("\nExecuting Task B")
    execute_query()

    print("\nDrop Inde3x")
    change_index(DROP_INDEX2)


if __name__ == '__main__':
    main()
