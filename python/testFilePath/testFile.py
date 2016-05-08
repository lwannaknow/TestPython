# coding=utf-8
__author__ = 'jim'

import sys

reload(sys)
sys.setdefaultencoding('utf8')
import datetime
import os

LOG_PATH = "~/kiosk/log/"
dt = datetime.datetime
today = '{0}-{1}-{2}'.format(dt.now().month, dt.now().day, dt.now().year)
LOG_FILE = '%srobo.log.%s' % (LOG_PATH, today)
log_details = os.popen('tail %s' % (LOG_FILE))
for i in log_details:
    print i
log_details.close()
a = ''
a = dict(a)
b = {"2": "3"}
data = dict(a, **b)
print data
import io
a=u"你好"
b="一定是中文"
a+="%s"%b

f = io.open("./lalag.csv", "w+", encoding="gbk")
f.write(a)
f.close()
f = io.open("./lalau.csv", "w+", encoding="utf-8")
f.write(a)
open("./lalag.csv")
f.close()
