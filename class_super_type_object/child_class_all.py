# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
from pprint import pprint
from class_super_type_object.child_class_01 import first_file_children
from class_super_type_object.child_class_02 import second_file_children
from class_super_type_object.child_class_03 import three_file_children

# 删除指定类
VIZ_TYPE_DENYLIST = ['FirstChild', ]
all_child = first_file_children
all_child.update(second_file_children)
all_child.update(three_file_children)
for key in VIZ_TYPE_DENYLIST:
    all_child.pop(key)

if __name__ == '__main__':
    pprint(all_child)
