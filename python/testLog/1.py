__author__ = 'Administrator'
import logging


LOG_FORMAT = ('%(levelname) -10s %(asctime) -30s %(name)-20s.%(filename)-30s %(funcName)-s[line: '
              '%(lineno)-2d]     %(message)s')
logging.basicConfig(filename="./mq.log",format=LOG_FORMAT,level=logging.DEBUG)
logging.info('1')