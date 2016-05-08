__author__ = 'Administrator'

import logging
import logging.handlers
import time
import datetime

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = logging.handlers.TimedRotatingFileHandler("logging_test2",
                                                    when='m',
                                                    interval=1,
                                                    backupCount=2)
logger.addHandler(handler)

while True:
    logger.info(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(0.1)
