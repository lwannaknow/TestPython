# coding=utf-8
def fuck(fn):
    print "fuck %s" % fn.__name__[::-1].upper()


@fuck
def wfg():
    pass


from functools import wraps


def hello(fn):
    @wraps(fn)
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__

    return wrapper


@hello
def foo():
    '''foo help doc'''
    print "i am foo"
    pass


foo()
print foo.__name__  # 输出 foo
print foo.__doc__  # 输出 foo help doc

a = [0, 1, 2, 3, 4]
a[::2] = [5, 6, 7]
print a
a = [0, 1, 2, 3, 4]
print a[1:3]
a[1:3] = [5, 6, 7]
print a
