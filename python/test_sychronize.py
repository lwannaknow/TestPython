# coding=utf-8
__author__ = 'jim'
from testpyramid.models import *

if __name__ == '__main__':
    # qcs_Thread = machine_submit.qcs_Thread("qcs_Thread2", 'QM_ORANGE2', '127.0.0.1(1421)')
    # qcs_Thread.start()
    # qcs_Thread = machine_submit.qcs_Thread("qcs_Thread",'QM_ORANGE','127.0.0.1(1415)')
    # qcs_Thread.start()
    #
    # qsrthread1 = server_receive.qsrthread("qsrthread1")
    # qsrthread1.start()
    # qsrthread1.join()
    # server_update.update_machine_data('MSM001',
    #                                   [{u'g_name': u'\u5546\u54c11', u'price': 2.0, u'g_id': 1, u'number': 100},
    #                                    {u'g_name': u'\u5496\u55b1\u68d2', u'price': 5.5, u'g_id': 2, u'number': 200}])
    qumthread1 = machine_update.qumthread("qumthread1")
    qumthread1.start()
    qumthread1.join()

    print "Exiting Main Thread"
