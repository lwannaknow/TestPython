# encoding=utf-8
__author__ = 'Administrator'

import json

from pythonTest.python.testVariable import *


def object_orient():
    change_object_property()
    print before_change.a
    print before_change.b


def normal_variable():
    print before_change.a
    print before_change.b


def return_object_property():
    return accumulation_object_property()


def b_ar(msg):
    global load_ss
    if msg == 0:
        load_ss = []
    else:
        for i in range(2):
            load_ss.append(i)
            print load_ss


def c_ar():
    global load_ss
    d_ar(load_ss)


def d_ar(msg):
    print msg


if __name__ == "__main__":
    # normal_variable()
    # msg = {"key": "value"}
    # print info_merge(status=1, lala="hahah", msg=msg)
    # print msg
    a = {"中文": 1}
    b=json.dumps(a , encoding='UTF-8', ensure_ascii=False)
    print b
