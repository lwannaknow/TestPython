__author__ = 'jim'

import os
import sys

print os.path.abspath(__file__)
print os.path.normpath(__file__)
print os.path.realpath(__file__)
print __file__
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
print dirname
print filename