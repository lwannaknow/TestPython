__author__ = 'jim'

from server.aplayer import Player
from server.extends import *
START_LOGIN_MP3 = "%s/mp3/input_password.mp3" % RESOURCE_PATH

if __name__=='__main__':
    Player(START_LOGIN_MP3)