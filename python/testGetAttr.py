# coding=utf-8
__author__ = 'jim'


class A():
    attribute_1 = 'attribute_1'
    def __init__(self):
        self.attribute_2 = 'attribute_2'
    def classfunction(self):
        print u'buyaoxiao'
        return 1


def testFunction():
    print u'调用成功'


if __name__ == "__main__":
    li = ['1', '2']
    try:
        a = getattr(li, 'append' )
        b=A()
        c = getattr(b,'classfunction')
        d = getattr(b,'attribute_2')
        e = getattr(b,'attribute_1')
        # print a
        print c()
        # print d
        # print e
        a(3)
        # print li
    except AttributeError, ex:
        print 1
        print ex.message
