__author__ = 'jim'

import datetime
import sys
import json

def f(timeout=""):
    if timeout!="":
        print timeout
    else:
        print 2
print datetime.datetime.utcfromtimestamp(1446367918.794).strftime("%Y-%m-%d %H:%M:%S")
# 17:54:46
# 17:55:32
print datetime.datetime.utcfromtimestamp(1445680506.04).strftime("%Y-%m-%d %H:%M:%S")
f(timeout=None)
print __name__
# simulated_time = ""
# if simulated_time:
#     print 1
# else:
#     print 2
#
# if __name__ == "__main__":
#     load_list=[]
#     for i in range(4):
#         load_list.append(i)
#     msg={"data":json.dumps(load_list)}
#     print json.dumps(msg)
