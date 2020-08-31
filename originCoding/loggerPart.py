import sys
import os
from loguru import logger
print(sys._getframe(0))


path = '/home/benny/PycharmProjects/2_BennyJane/Learning_Py_World/originCoding/loggerPart.py'

filename = os.path.basename(path)
print(filename)
module = os.path.splitext(filename)
print(module)