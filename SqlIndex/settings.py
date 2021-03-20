# 常量
# 5个数据库的名称
DB_NAMES = ("A4v100.db", "A4v1k.db", "A4v10k.db", "A4v100k.db", "A4v1M.db")
# 5个数据库的数据量
DB_NUMS = (100, 1000, 10000, 100000, 1000000)
# 创建数据表的SQL
CREATE_SQL = """CREATE TABLE Parts (
partNumber INTEGER, -- a UPC code 
partPrice INTEGER, -- in the [1, 100] range
needsPart INTEGER, -- a UPC code
madeIn TEXT, -- a country (2 letters) code 
PRIMARY KEY(partNumber)
);"""
# 删除数据表的SQL
DROP_SQL = """DROP TABLE Parts;"""

# 插入数据的SQL
INSERT_SQL = """INSERT INTO Parts (partNumber, partPrice, needsPart, madeIn)
 VALUES ({}, {}, {}, '{}')
 """

# 原始数据的路径
COUNTRY_DATA = "./data/data_json.json"
UPC_DATA = "./data/upc_corpus.csv"
