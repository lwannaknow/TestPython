__author__ = 'jim'

import time

a = {'status': 'haha'}
if a != True:
    print 1

a = 0

while a != 11:
    time.sleep(1)
    a += 1
    print 1
else:
    print "hahaha"
