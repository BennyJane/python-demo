# -*- coding: utf-8 -*-
# @Time : 2020/11/15
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : Python-Exercise
from datetime import datetime

# Python datetime 模块是 date 与time模块的结合

now = datetime.now()  # 创建一个datetime对象; 实际调用的是time模块方法 t = _time.time()
day = now.day
year = now.year
month = now.month
print("当前时间: %s" % now)
print(year, month, day)  # 获取年 月 日属性

"""
datetime 之间可以直接进行加减操作
"""

end = datetime(year, 12, 31)
remaining = (end - now).days
print(f"{year}年剩余天数{remaining}")


"""
datetime.strftime('%Y-%m-%d'): 用于格式化datetime对象
%a	星期的英文单词的缩写：如星期一， 则返回 Mon
%A	星期的英文单词的全拼：如星期一，返回 Monday

%b	月份的英文单词的缩写：如一月， 则返回 Jan
%B	月份的引文单词的缩写：如一月， 则返回 January

%c	返回datetime的字符串表示，如03/08/15 23:01:26

%d	返回的是当前时间是当前月的第几天

%f	微秒的表示： 范围: [0,999999]

%H	以24小时制表示当前小时
%I	以12小时制表示当前小时

%j	返回 当天是当年的第几天 范围[001,366]

%m	返回月份 范围[0,12]

%M	返回分钟数 范围 [0,59]

%P	返回是上午还是下午–AM or PM

%S	返回秒数 范围 [0,61]。。。手册说明的

%U	返回当周是当年的第几周 以周日为第一天
%W	返回当周是当年的第几周 以周一为第一天
%w	当天在当周的天数，范围为[0, 6]，6表示星期天

%x	日期的字符串表示 ：03/08/15
%X	时间的字符串表示 ：23:22:08

%y	两个数字表示的年份 15
%Y	四个数字表示的年份 2015

%z	与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z	时区名称（如果是本地时间，返回空字符串）
"""
print("[%Y-%m-%d %H:%M:%S %f]: ", now.strftime("%Y-%m-%d %H:%M:%S %f"))
print("[%y-%m-%d %I:%M:%S %p]: ", now.strftime("%y-%m-%d %I:%M:%S %p"))

print("星期几，缩写 [%a]: ", now.strftime("%a"))
print("星期几，全称 [%A]: ", now.strftime("%A"))

print("月份，全称 [%b]: ", now.strftime("%b"))
print("月份，全称 [%B]: ", now.strftime("%B"))

print("字符串格式 [%c]: ", now.strftime("%c"))

print("本周的第几天 [%w]: ", now.strftime("%w"))
print("本年的第几天 [%j]: ", now.strftime("%j"))
print("本周是当年的第几周 [%U]: ", now.strftime("%U"))
print("今天是当月的第几天 [%d]: ", now.strftime("%d"))
