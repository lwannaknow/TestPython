__author__ = 'Jim'

import time
import json

def function(a):
    if a==1:
        return "Fatal"
    elif a==2:
        return True
    elif a==3:
        return {'status':'True','code':2}
    else:
        return False

if __name__=="__main__":
    a=3
    if function(a)['status']!='True':
        print 'True'

    a={'data':{'a':1,'b':2}}
    print a['data']

    print time.time()
    a={'status':'Fatal','code': 0100,'details':'socket connect failed'}
    b={'uuid' : "t001" , 'shopping_cart_uuid ': "001",'product_id ': "p001" , 'product_name ': "milk"}
    c=""
    print json.dumps(dict(c,**a))
    # print str(time.time())

