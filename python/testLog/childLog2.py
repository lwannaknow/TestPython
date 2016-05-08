__author__ = 'jim'

from pythonTest.python.testLog import *

def Log2():
    # print __name__
    # pythonTest.python.testLog.LOGGER.error("you should be childLog")
    LOGGER.error("you should be childLog")
    LOGGER.info("you should be childLog")

if __name__=="__main__":
    Log2()
