# coding=utf-8
__author__ = 'Administrator'

# def lalal():
#     import time
#     a=1
#     while 1:
#         if a==1:
#             time.sleep(1)
#             print 1
#         else:
#             pass


if __name__ == "__main__":
    a = """ok ('goto', 'idle', True) """
    b = """ok ('goto', 'running', 'doing') """
    a_result = a.split(",")[2][0:-2].strip()
    print b.split(",")[2][0:-2].strip()
    if 'True' in a_result:
        print 1
    # lalal()
    c = "adminMaizestore/commercial/advertisement/1451047378769_6901209322105.jpg".split("/")[3][:-4]
    print c
    import datetime
    import time

    print int(time.mktime(datetime.datetime.now().timetuple()))
    all_list = [
        109,
        112,
        115,
        118,
        123,
        125,
        133,
        135,
        138,
        139,
        142,
        144,
        146,
        153,
        159,
        160,
        167,
        170,
        172,
        173,
        202,
        206,
        207,
        208,
        209,
        213,
        218,
        219,
        220,
        221,
        223,
        224
    ]
    today_list = [208, 221, 209, 207, 224, 206, 202, 172, 167, 153, 146, 144, 219, 139, 173, 135, 133, 125, 123, 118,
                  115, 112, 109]
    v = list(map(lambda x: x[0] - x[1], zip(today_list, all_list)))
    print list(set(all_list).difference(set(today_list)))
    doc = {"1": 1, "2": 2}
    if doc:
        print 1
        print len(doc)
    else:
        print 2
    print {}.__class__
    short_name = "上海市普陀区武宁路350号联合大厦Vincent办公室"
    print short_name.partition("区")[2]
    # lst=[]
    # print lst[0]
    a = {u'openid': u'oo4IKxPDtdrC32chYtulN4NuybNM', u'trade_type': u'    JSAPI', u'total_fee': u'1',
         'type': 'wechat_bill', u'return_code': u'SUCCESS', u'nonce_str': u'wf6SFWjzYlgpkVEmiqun7XMBhceJr1ds',
         u'is_subscribe': u'Y', u'fee_type': u'CNY', u'bank_type': u'CFT', u'mch_id': u'1260518601',
         u'out_trade_no': u'wx443951453109125', u'transaction_id': u'1005390778201601182768262114',
         u'time_end': u'20160118173440', u'appid': u'wx53d2501b04d8cbe2', u'cash_fee': u'1', u'result_code': u'SUCCESS'}
    b = {'openid': '', 'trade_type': '', 'type': 'wecha    t_bill', 'total_fee': '',
         'reserve_details': {'4902888234583': {'purchase_num': 1, 'unit_price': 9.89}}, 'fee_type': '',
         'pickup_c    ode': '', 'nonce_str': '', 'return_code': '', 'is_subscribe': '', 'bank_type': '', 'mch_id': '',
         'out_trade_no': '', 'transaction_    id': '', 'time_end': '',
         'coupon_uuid': '6BD4CEFA-0297-452A-B1F8-4490D7815663', 'appid': '', 'reserve_status': False, 'cash_fee': '',
         'result_code': ''}
    for k in a:
        b[k]=a[k]
    print b