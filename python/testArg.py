# coding=utf-8
__author__ = 'jim'

import sys

print "脚本名:" + sys.argv[0].decode("gbk").encode("utf-8")+"\n"
for i in range(1, len(sys.argv)):
    print 1
    print sys.argv[i]
