# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : Python-Exercise
# Time       ：2020/12/11 22:17
# Warning    ：The Hard Way Is Easier
import functools
from sqlalchemy import MetaData, Table, Column, create_engine, String, INTEGER
from sqlalchemy import insert, delete
from sqlalchemy.exc import InternalError

metadata = MetaData()
engine = create_engine("mysql+pymysql://root:5eNyj6Nf@127.0.0.1:13306/base_db?charset=utf8mb4")

# 设计锁字段： 必须唯一
lock_table = Table("task_lock", metadata,
                   Column("id", INTEGER(), primary_key=True, autoincrement=True),
                   Column("lock_key", String(120), unique=True, nullable=False, comment="任务锁")
                   )

# 创建数据表
metadata.create_all(engine)

"""
========================================================================================
锁机制： 只允许一个进程执行成功
========================================================================================
"""


# 加锁方法： bool值表示是否成功
def add_lock(lock_value):
    # 添加唯一锁
    ins = insert(lock_table).values(lock_key=lock_value)
    # 如果当前锁名称记录不存在，则插入成功，返回True
    try:
        engine.connect().execute(ins)
    except (InternalError, Exception) as e:
        # 当前插入锁值已存在，且表示尚未解锁，其他操作都会触发该异常，返回False
        return False
    else:
        return True


# 解锁方法，只要成功添加锁，执行任务后，无论成功与否，都要调取该方法解锁

def delete_lock(lock_value):
    d = delete(lock_table).where(lock_table.c.lock_key == lock_value)
    engine.connect().execute(d)
    # print("delete lock...")


"""
========================================================================================
装饰器： 修饰job函数
单节点任务装饰器，被装饰的任务在分布式多节点下同一时间只能运行一次

在执行原函数前，会先尝试加锁，即写入lock_key值，若写入成功，则获得锁，可以继续执行该任务函数；
若加锁失败，即写入lock_key时数据库已存在当前值，说明其他节点正在执行该任务，则无法获得锁，不能执行该任务函数，
只会打印提示信息。

========================================================================================
"""


def single_task(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        lock_name = f"crontab {f.__name__}"
        lock_res = add_lock(lock_name)
        print(f"{f.__name__} lock", lock_res)
        if lock_res:
            print("当前节点获取到任务：{}".format(f.__name__))
            try:
                result = f(*args, **kwargs)
            except Exception as e:
                pass
                # print(str(e))
                # raise e
            finally:
                delete_lock(lock_name)
            return result
        else:
            print("当前节点没有获取到任务：{}".format(f.__name__))

    return wrapper
