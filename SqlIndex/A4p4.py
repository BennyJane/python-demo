import time
import random
import sqlite3
from threading import Thread

from settings import DB_NAMES
from utils import load_country_data
from utils import get_average
from utils import change_index

# PART4 查询随机选择的国家中最大price的值
EXECUTE_NUMS = 100
SELECT_SQL_Q1 = "select count(m.partNumber) from Parts m where not exists(select 1 from Parts n where m.partNumber = n.needsPart);"
SELECT_SQL_Q2 = "select count(partNumber) from Parts where partNumber not in(select needsPart from Parts);"
# 创建单索引：needsPart
CREATE_INDEX = "CREATE INDEX idxNeedsPart ON Parts ( needsPart );"
DROP_INDEX = "DROP INDEX idxNeedsPart;"
# 创建复合索引： needsPart, partNumber
CREATE_INDEX2 = "CREATE INDEX idxNeedsPartAndPartNumber ON Parts (needsPart, partNumber);"
DROP_INDEX2 = "DROP INDEX idxNeedsPartAndPartNumber;"


def execute_sql(conn):
    time_point1 = time.time()
    for _ in range(EXECUTE_NUMS):
        conn.execute(SELECT_SQL_Q1)
    time_point2 = time.time()
    for _ in range(EXECUTE_NUMS):
        conn.execute(SELECT_SQL_Q2)
    time_point3 = time.time()
    q1_time_sum = (time_point2 - time_point1)
    q2_time_sum = (time_point3 - time_point2)
    # print("Q1: ", q1_time_sum, "Q2: ", q2_time_sum)
    print(f"Average query time for Query Q1: {get_average(q1_time_sum)} ms")
    print(f"Average query time for Query Q2: {get_average(q2_time_sum)} ms")


def execute_query_no_index():
    origin_data = load_country_data()
    random.shuffle(origin_data)
    for index, db_name in enumerate(DB_NAMES):
        conn = sqlite3.connect(db_name)
        print(f"Opening {db_name}")
        if index < 2:  # 只执行 "A4v100.db", "A4v1k.db" 两个数据库的查询语句
            execute_sql(conn)
        else:
            print(f"Average query time for Query Q1: The query time is too long")
            print(f"Average query time for Query Q2: The query time is too long")
        conn.close()
        print(f"Closing {db_name}")


def execute_query_index():
    origin_data = load_country_data()
    random.shuffle(origin_data)
    for index, db_name in enumerate(DB_NAMES):
        conn = sqlite3.connect(db_name)
        print(f"Opening {db_name}")
        execute_sql(conn)
        conn.close()
        print(f"Closing {db_name}")


def main():
    print("Executing Part 4\n")

    print("Executing Task J1")
    execute_query_no_index()

    print("\nCreating Index")
    change_index(CREATE_INDEX)

    print("\nExecuting Task J2")
    execute_query_index()

    print("\nDrop Index")
    change_index(DROP_INDEX)

    print("\nCreating Index")
    change_index(CREATE_INDEX2)

    print("\nExecuting Task J2")
    execute_query_index()

    print("\nDrop Index")
    change_index(DROP_INDEX2)


if __name__ == '__main__':
    main()
