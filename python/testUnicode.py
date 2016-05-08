# coding=utf-8
__author__ = 'jim'

if __name__ == "__main__":
    # if coding is gbk, here it would be printed corrently, #
    # which means the coding of console is the same as windows--gbk #
    # the coding order is: console,input,assignment(gbk)-> encode coding here is utf-8 #
    # the reason of the messy code in variable a is bcz you input a gbk string and want it to be printed with utf-8.#
    # of course, it can't be decoded correctly #

    # Change Log:10/07/2015
    # 1.coding的作用：将unicode字符保存为coding的格式，此处为utf-8 详解看标签:python编码文件夹
    # 2.print 将要输出的内容传送了操作系统，操作系统会根据系统的编码对输入的字节流进行编码，因此在cmd中 utf-8格式的
    # 字符串“哈哈”，输出的是“鍝堝搱” e.g a='哈哈' print a.decode('gbk').encode('utf-8')
    # 3.pycharm ide 作用: coding 后文件格式保存成你指定编码格式。因此 此处的编码环境就是 utf-8.可以直接输出
    # str.encode 的过程是 str.decode(sys.getdefaultencoding()).encode(''),默认的getdefaultencoding()是ASCII,需要
    # setdefaultencoding()更改
    a = '我的'
    print a.decode('gbk').encode('utf-8')
    print a.decode('utf-8').encode('gbk')
    au = u'我的'
    # au = au.encode('ascii')
    a_decode = a.decode('utf-8')
    a_encode = a_decode.encode('gbk')
    au_encode = au.encode('utf-8')
    a_type = a.__class__
    au_type = au.__class__
    ad_type = a_decode.__class__
    ae_type = a_encode.__class__
    print a
    print au
    print a_decode
    print a_encode
    print a_type
    print au_type
    print ad_type
    print ae_type
    print au_encode
    # a=u'Map'
    print type(a)
    b = 'aaa'
    bu = u'aaa'
    print b != bu
    import sys

    print sys.getdefaultencoding()
