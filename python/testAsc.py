# coding=utf-8
__author__ = 'hp'

DB = "/home/f1/kiosk_5/var/db/main.db"
DB_f1_v2 = "/home/f1/kiosk/db/f1_v2.db"

import logging
import dao
import requests
import time
import socket
import datetime
import ConfigParser
import threading
import Queue


LOGGER = logging.getLogger(__name__)
HOST_NAME = socket.gethostname()

queue = Queue.Queue()


class MKC(threading.Thread):
    def __init__(self, fun, **kwargs):
        threading.Thread.__init__(self)
        self.fun = fun
        self.kwargs = kwargs

    def run(self):
        try:
            fun = getattr(self, self.fun)
            fun(**self.kwargs)
        except Exception as E:
            queue.put(E)

    def set_slot_status(self, col, row, status):
        slot_id = col + row
        message = {
            "col": col,
            "row": row,
            "slot_id": slot_id,
            "status": status,
            "is_success": "F",
            "error": ""
        }
        status_list = ['bad', 'empty', 'good']
        my_dao = dao.Dao(DB)
        try:
            if status not in status_list:
                message["error"] = "ILLEGAL_STATUS"
                queue.put(message)
            else:
                if status is 'good':
                    status = 'full'
                result = my_dao.set_slot_status(slot_id, status)
                if result is True:
                    message["is_success"] = "T"
                    queue.put(message)
                else:
                    message["error"] = result
                    queue.put(message)
        except Exception as E:
            queue.put(E)

    def set_module_version(self, module, version):
        try:
            my_dao = dao.Dao(DB)
            msg = {'module': module, 'version': version}
            my_dao.add_queue(msg, "middleware", "set_module_version")
            queue.put(msg)
        except Exception as E:
            queue.put(E)

    def set_alert(self, level, text, attachment_list=[]):
        cp = ConfigParser.ConfigParser()
        cp.read('/home/f1/kiosk_5/mkc/server/recipients.ini')
        email_address = cp.get('Email_list', 'cc').split(',')
        files_array = []
        for i in attachment_list:
            files_array.append(("attachment", open(i)))
        for i in range(4):
            r = requests.post(
                url="https://api.mailgun.net/v3/sandbox6d9cf973329643259d78d1fbb1e280fa.mailgun.org/messages",
                auth=("api", "key-fae43452c4bd562289716e6c3ce821e7"),
                files=files_array,
                data={"from": "MShop <postmaster@sandbox6d9cf973329643259d78d1fbb1e280fa.mailgun.org>",
                      "to": email_address,
                      "subject": "Level: " + str(
                          level) + " Report from " + HOST_NAME + " " + datetime.datetime.now().strftime(
                          "%Y-%m-%d %H:%M:%S"),
                      "text": text,
                      },
            )
            code = r.status_code
            if code == 200:
                queue.put({'status': 'success', 'code': code})
                break
            else:
                time.sleep(0.5)
                LOGGER.error("email sending failed,status code is %s" % (code,))
                queue.put({'status': 'false', 'code': code})


if __name__ == "__main__":
    mkc_api = MKC('set_alert', level='5', text='text for testing', attachment_list=[])
    mkc_api.start()
    async_call(set_alert, print_result, level='5', text='test_testing')
    while True:
        print "time to wait"
        time.sleep(1)
        print "******from Queue %s" %(queue.get())
