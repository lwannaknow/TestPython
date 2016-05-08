# coding=gbk
__author__ = 'Administrator'

s = '水壶'  # coding=utf, it can be decoded
a = '\xe6\xb0\xb4\xe5\xa3\xb6'
# print unicode(s, 'big5')
print unicode(s, 'gbk')
# print unicode(s, 'gb2312')
# print unicode(s, 'utf-8')
print unicode(a, 'big5')
print unicode(a, 'gbk')
print unicode(a, 'gb2312')
print unicode(a, 'utf-8')
for x in range(1,11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
    # {0:2d} 表示第一个参数x的格式。0 代表x,:2d 表示两个宽度的10进制数显示。