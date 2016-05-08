__author__ = 'jim'

from pythonTest.python.testVariable import *

def change_object_property():
    before_change.a=1
    before_change.b=2

def change_variable():
    a=1
    b=2

def accumulation_object_property():
    before_change.a+=1
    before_change.b+=2
    return before_change.a,before_change.b

def info_merge(msg, **kargs):
    for k in kargs:
        msg[k]=k

def do_something():
    print "do sth else"

