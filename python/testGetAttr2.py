__author__ = 'jim'

import testGetAttr2

def function():
    print "11"


if __name__ == "__main__":
    a = getattr(testGetAttr2, "function")
    a()
