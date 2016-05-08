# coding=UTF-8
__author__ = 'jim'



class NoClassFound(Exception):
    def __init__(self, sentence, error_id):
        self.message = sentence
        self.error_id = error_id


def testException1():
    try:
        # raise NoClassFound("Second Exception",444)
        print "first Exception"
        try:
            print a
            print "second Exception"
            raiseException()

        except Exception as ex:
            print 2
            print Exception,":",ex.message
            print 3
    except NoClassFound, ex:
        print 4
        print ex.message
    finally:
        print 5

def testException2():
    un_ass_var=[]
    try:
       fh = open("testfile", "w")
       try:
          fh.write("This is my test file for exception handling!!")
          print un_ass_var[1]
       finally:
          print "Going to close the file"
          fh.close()
    except Exception:
       print "Error: can\'t find file or read data"

def socketPollDataTest():
    data=1
    try:
        data=data.split(",")[2][0:-2].strip()
    except:
        print "lala"
    print data

def raiseException():
    # raise NoClassFound("exception in method",4375)
    raise Exception("exception in method", 4375)


def function1():
    print 1
    function2()
    print 3


def function2():
    print 2
    return False


if __name__ == "__main__":
    # testException2()
    # raiseException()
    socketPollDataTest()
    # function1()