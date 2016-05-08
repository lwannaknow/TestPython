__author__ = 'Administrator'

from pythonTest.python.testLog import *
# import pythonTest.python.testLog

def Log1():
    # print __name__
    # pythonTest.python.testLog.LOGGER.error("you should be childLog")
    LOGGER.error("you should be childLog")
    LOGGER.info("you should be childLog")

if __name__=="__main__":
    Log1()