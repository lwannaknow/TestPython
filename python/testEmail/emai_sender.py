# -*- coding:gbk-*-
__author__ = 'Administrator'

__author__ = 'VincentChen'

import sys
import io

reload(sys)
sys.setdefaultencoding('gbk')
from datetime import datetime

from couchbase.bucket import Bucket
from couchbase.exceptions import NotFoundError
import requests

# DBSession = Bucket('couchbase:///default')
DBSession = 'couchbase:///default'


class CsvReport:
    def __init__(self, report_date):
        self.report_date = report_date
        self.win_file_path = "./rest_report_2015-12-13.csv"
        self.utf_file_path = "./windows_report_2015-12-13.csv"

    def _read_stock_from_db(self, kiosk_id):
        result = []
        kiosk_upcs = DBSession.get("%s::products" % kiosk_id).value
        # print "KIOSK_UPCS: %s" % kiosk_upcs
        for kiosk_upc in kiosk_upcs:
            try:
                product = DBSession.get(kiosk_upc).value
            except NotFoundError, ex:
                continue

            try:
                detailed_product = DBSession.get(product["upc"]).value
                product["name"] = detailed_product["easy_name"]
            except NotFoundError, ex:
                product["name"] = u"未知"
            result.append(product)
        return result

        """
        [{'name': u'\u5229\u5b89\u4e39\u8428\u9648\u917f',
        u'type': u'kiosk_product',
        u'sold': 0,
        u'upc': u'8436011560172',
        u'slots': [u'A4', u'B5'],
        u'total': 4, u'expired': 0},

        {'name': u'\u5229\u5b89\u4e39\u8428\u9648\u917f',
        u'type': u'kiosk_product',
        u'sold': 0,
        u'upc': u'8436011560172',
        u'slots': [u'A4', u'B5'],
        u'total': 4, u'expired': 0}
        """

    def _generate_stock_report_csv(self, kiosk_id):

        content = u"%s当前库存\n" % kiosk_id
        content += u"产品名称,UPC,槽位,总数,过期数\n"

        for rec in self._read_stock_from_db(kiosk_id):
            try:
                content += "%s,'%s',%s,%s,%s\n" % (rec["name"],
                                                   rec["upc"],
                                                   str(rec["slots"]).replace(",", ";"),
                                                   rec["total"],
                                                   rec["expired"])
            except Exception, ex:
                print "[!!!!! ERROR !!!!!]\n" \
                      "Error in adding rec %s: %s\n" \
                      "[!!!!! ERROR !!!!!]" % (rec, ex.message)

            content += "\n"

        return content

    def _read_trx_from_db(self, kiosk_id):
        result = []
        try:
            trx_ids = DBSession.get("transactions::%s::%s" % (kiosk_id, self.report_date)).value
            # print "TRX IDS: %s" % trx_ids

            for trx_id in trx_ids:
                try:
                    trx = DBSession.get(trx_id).value
                except NotFoundError, ex:
                    print "No trx found for trx_id %s" % trx_id

                print "Trx Found: %s" % trx

                if trx.has_key("status"):
                    if str(trx["status"]).upper() == "SUCCESS":
                        shopping_cart = {}
                        try:
                            shopping_cart = DBSession.get(trx["out_trade_no"]).value

                        except NotFoundError, ex:
                            print "[!!!!! ERROR !!!!!]\n" \
                                  "No trx out_trade_no %s found for trx_id %s\n" \
                                  "[!!!!! ERROR !!!!!]" % (trx["out_trade_no"], trx_id)

                        if shopping_cart:
                            trx["payment_method"] = shopping_cart["payment_method"]
                            trx["customer"] = shopping_cart["customer"]

                            try:
                                product = DBSession.get(trx["upc"]).value
                                trx["product_name"] = product["easy_name"]
                            except NotFoundError, ex:
                                trx["product_name"] = u"未知"
                            result.append(trx)
                else:
                    print "[!!!!! ERROR !!!!!]\n" \
                          "Key status missing in trx %s\n" \
                          "[!!!!! ERROR !!!!!]" % trx

        except NotFoundError, ex:
            print "No trx found for %s on %s" % (kiosk_id, self.report_date)
        return result

        """
        [{u'status': u'SUCCESS',
        'customer': u'',
        u'shopping_cart_uuid': u'7a6a2b3e-7d20-11e5-acce-446d57b12157',
        'payment_method': u'wechat',
        u'start_time': u'2015-11-04 20:00:20',
        u'kiosk': u'M2-B142',
        u'upc': u'8436011560171',
        u'transaction_no': u'18fd1f50-d3bf-40aa-baca-bd02a40d4924',
        u'amount': 28.0,
        u'slot_id': u'A3',
        u'end_time': u'2015-11-04 20:20:20',
        u'fetch_status': u'SUCCESS',
        u'out_trade_no': u'1311423132413246',
        u'type': u'transaction',
        u'dispense_status': u'SUCCESS'},
         {u'status': u'SUCCESS', 'customer': u'', u'shopping_cart_uuid': u'7a6a2b3e-7d20-11e5-acce-446d57b12157',
         'payment_method': u'wechat', u'start_time': u'2010-07-22 20:00:20', u'kiosk': u'M2-B142', u'upc': u'8436011560172',
         u'transaction_no': u'18fd1f50-d3bf-40aa-baca-bd02a40d4925', u'amount': 165.0, u'slot_id': u'A4',
         u'end_time': u'2010-07-22 20:20:20', u'fetch_status': u'SUCCESS', u'out_trade_no': u'1311423132413245',
         u'type': u'transaction', u'dispense_status': u'SUCCESS'}]
        """

    def _generate_trx_report_csv(self, kiosk_id):
        content = u"%s 交易记录\n" % kiosk_id
        content += u"商品,UPC,槽位,时间,金额,支付方式,支付用户\n"

        for rec in self._read_trx_from_db(kiosk_id):
            content += "%s,'%s',%s,%s,%s,%s,%s\n" % (rec["product_name"],
                                                     rec["upc"],
                                                     str(rec["slot_id"]).replace(",", ";"),
                                                     rec["end_time"],
                                                     rec["amount"],
                                                     rec["payment_method"],
                                                     rec["customer"])

        content += "\n\n\n"

        return content

    def _save_csv(self, content):
        f = open(self.utf_file_path, "w+")
        f.write(u"你好")
        f.close()
        reload(sys)
        sys.setdefaultencoding('gbk')
        f = open(self.win_file_path, "w+")
        f.write(u"你好")
        f.close()

    def run(self):
        # all_kiosks = DBSession.get("all_kiosk").value

        text_csv = ""
        # for kiosk_id in all_kiosks:
        #     text_csv += self._generate_stock_report_csv(kiosk_id)
        #     text_csv += self._generate_trx_report_csv(kiosk_id)

        self._save_csv(text_csv)


def send_mail(attachment_file_path, report_date, send_to):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6d9cf973329643259d78d1fbb1e280fa.mailgun.org/messages",
        auth=("api", "key-fae43452c4bd562289716e6c3ce821e7"),
        files=[("attachment", open(attachment_file_path[0])),
               ("attachment", open(attachment_file_path[1])),
               ],
        data={"from": u"alert@appartner.cn <postmaster@sandbox6d9cf973329643259d78d1fbb1e280fa.mailgun.org>",
              "to": send_to,
              "subject": u"【自动报表】%s" % report_date,
              "text": u"请查看附件\n\n\n Powered by Appartner Inc"})


if __name__ == "__main__":

    report_date = datetime.now().strftime("%Y-%m-%d")
    if len(sys.argv) > 1:
        report_date = sys.argv[1]

    r = CsvReport(report_date)
    r.run()

    print send_mail([r.utf_file_path, r.win_file_path], report_date, "jim.liu@appartner.cn").content

    # Usage: ./daily_csv_report a@b.com,c@a.com [2016-08-13]
