# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import string
import random

num_and_word = string.digits + string.ascii_letters
print(random.sample(num_and_word, 5))
print(random.choice(num_and_word))
print(random.random())
print(random.randint(0, 100))
print(random.uniform(0, 100))


