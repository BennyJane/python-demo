# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import os

from pprint import pprint

# 设置环境变量
os.environ['FLASK_ENV'] = "development"
os.environ['FLASK_CONFIG'] = "ProductionConfig"

print("获取环境变量：", os.getenv("FLASK_ENV"))

# 删除环境变量
del os.environ["FLASK_ENV"]
# os.environ.pop("FLASK_CONFIG")  # os.environ其实就是字典类型

print("获取环境变量：", os.getenv("FLASK_ENV", "None"))
all_variables = os.environ  # 获取当前所有环境变量

## TODO 永久设置环境变量 ?? 没有成功

path = r"E:\env"
# command = r"setx permanent %s /m" % path
command = r"setx permanent %s" % path
os.system(command)

if __name__ == '__main__':
    pprint(dict(all_variables))
    FLASK_ENV = os.environ.get("FLASK_ENV")
    FLASK_CONFIG = os.environ.get("FLASK_CONFIG")
    print(FLASK_ENV, FLASK_CONFIG)

    print(os.environ.get("permanent"))
