import time
import random
import sqlite3
from threading import Thread

from settings import DB_NAMES
from utils import load_country_data
from utils import get_average
from utils import change_index

# PART4 查询随机选择的国家中最大price的值
EXECUTE_NUMS = 1
SELECT_SQL_Q1 = "select count(m.partNumber) from Parts m where not exists(select 1 from Parts n where m.partNumber = n.needsPart);"
SELECT_SQL_Q2 = "select count(m.partNumber) from Parts m where m.partNumber not in(select partNumber from Parts n where m.partNumber = n.needsPart);"
CREATE_INDEX = "CREATE INDEX idxNeedsPart ON Parts ( needsPart );"
DROP_INDEX = "DROP INDEX idxNeedsPart;"

CREATE_INDEX2 = "CREATE INDEX idxNeedsPartAndPartNumber ON Parts ( needsPart, partNumber);"
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
    print("Q1: ", q1_time_sum, "Q2: ", q2_time_sum)
    print(f"Average query time for Query Q1: {get_average(q1_time_sum, EXECUTE_NUMS)} ms")
    print(f"Average query time for Query Q2: {get_average(q2_time_sum, EXECUTE_NUMS)} ms")


def execute_query_no_index():
    origin_data = load_country_data()
    random.shuffle(origin_data)
    for index, db_name in enumerate(DB_NAMES):
        conn = sqlite3.connect(db_name)
        print(f"Opening {db_name}")
        if index < 2:
            execute_sql(conn)
        else:
            print(f"Average query time for Query Q1: The query time is too long")
            print(f"Average query time for Query Q2: The query time is too long")
        conn.close()
        print(f"Closing {db_name}")


def execute_query_index():
    origin_data = load_country_data()
    random.shuffle(origin_data)
    db_name = "A4v1M.db"
    conn = sqlite3.connect(db_name)
    print(f"Opening {db_name}")
    execute_sql(conn)
    conn.close()
    print(f"Closing {db_name}")


def main():
    print("Executing Part 4")

    # print("Executing Task J1")
    # execute_query_no_index()

    print("\nCreating Index")
    change_index(CREATE_INDEX)

    print("\nExecuting Task J2")
    execute_query_index()

    print("\nDrop Index")
    change_index(DROP_INDEX)

    print("\nCreating Index2")
    change_index(CREATE_INDEX2)

    print("\nExecuting Task J2")
    execute_query_index()

    print("\nDrop Index2")
    change_index(DROP_INDEX2)


if __name__ == '__main__':
    main()
