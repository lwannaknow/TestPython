# coding=gbk
__author__ = 'Administrator'

s = 'ˮ��'  # coding=utf, it can be decoded
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
    # {0:2d} ��ʾ��һ������x�ĸ�ʽ��0 ����x,:2d ��ʾ������ȵ�10��������ʾ��