import time
import random
import sqlite3
from settings import DB_NAMES
from utils import load_country_data
from utils import get_average

EXECUTE_NUMS = 100
SELECT_SQL = "SELECT AVG(partPrice) FROM Parts WHERE madeIn  = '{}';"
CREATE_INDEX = "CREATE INDEX idxMadeIn ON Parts ( MadeIn );"
DROP_INDEX = "DROP INDEX idxMadeIn;"


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


def main():
    print("Executing Part 2\n")

    print("Executing Task A")
    execute_query()

    print("\nCreating Index")
    for db_name in DB_NAMES:
        conn = sqlite3.connect(db_name)
        conn.execute(CREATE_INDEX)
        conn.close()

    print("\nExecuting Task B")
    execute_query()

    # 先删除现有的索引
    print("\nDrop Index")
    for db_name in DB_NAMES:
        conn = sqlite3.connect(db_name)
        conn.execute(DROP_INDEX)
        conn.close()


if __name__ == '__main__':
    main()
