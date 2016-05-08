# coding=utf-8
__author__ = 'jim'

import random
import time

COLUMN = ["A", "B", "C", "D", "E", "F", "G"]

while True:
    print "%s%s" % (COLUMN[random.randint(0, 6)], random.randint(1, 16))
    time.sleep(1)
