__author__ = 'Jim'

import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
a=0

# formatter
LOG_FORMAT = ('%(levelname) -10s %(asctime) -30s %(name)-20s.%(filename)-30s %(funcName)-s[line: '
              '%(lineno)-2d]     %(message)s')
formatter = logging.Formatter(LOG_FORMAT, datefmt='%Y/%m/%d %H:%M:%S')

logging.basicConfig(format=LOG_FORMAT)

# add HANDLER
FHANDLER = logging.FileHandler('trace.log')
FHANDLER.setFormatter(formatter)
FHANDLER.setLevel(logging.WARNING)
LOGGER.addHandler(FHANDLER)


if __name__ == "__main__":
    LOGGER.info('And this, too')
    LOGGER.error('And this, too')


LOGGER = logging.getLogger("mq")
LOGGER.setLevel(logging.DEBUG)
logging.basicConfig(filename="./mq.log",format=LOG_FORMAT)
