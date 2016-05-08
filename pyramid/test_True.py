# coding=utf-8
__author__ = 'jim'


def is_box_empty():
    try:
        rtn_msg = {'status': 'True', 'data': 'ok (None)\n'}
        if 'False' in rtn_msg['data']:
            print("F_ex_empty_result:%s" % rtn_msg)
            return {"status": False}
        elif 'True' in rtn_msg['data']:
            print("T_ex_empty_result:%s" % rtn_msg)
            return {"status": True}
    except Exception as E:
        print("is_box_empty error: %s\n" % E.message)
        return {"status": False}


if __name__ == "__main__":
    # status = {"status": False}
    # print is_box_empty()
    # if status['status']:
    #     pass
    # else:
    #     status = 'False'
    # print status
    # data="ok ()\n"
    # data = data.split(",")[2][0:-2].strip()
    print u'\u540c\u4e00\u4e2aout_refund_no\u9000\u6b3e\u91d1\u989d\u8981\u4e00\u81f4'
