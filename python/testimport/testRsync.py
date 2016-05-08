__author__ = 'jim'

if __name__=="__main__":
    data='''ok ('dispense', 'running', 'open')'''
    print data.split(",")[2][0:-2].strip()
