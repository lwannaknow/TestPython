# coding=gbk
__author__ = 'Jim'

import sys


def invoking():
    print 'here is init.py'

if __name__=="__main__":
    print sys.path
    print sys.path[0]
# print str.decode(sys.path[0],'gbk')
