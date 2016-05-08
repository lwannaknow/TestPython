# coding=utf-8
__author__ = 'Administrator'

import sqlite3
import json

def get_unload_list_bd(cursor):
        try:
            query= """select DISTINCT a.upc,a.slot_id,product_name,b.status from loading a,slot b where
            a.status='out' and a.upc=b.upc;"""
            cursor.execute(query)
            rows = cursor.fetchall()
            if len(rows) == 0:
                return 'None'
            col_name_list = [tuple[0] for tuple in cursor.description]
            unload_list = []
            for row in rows:
                dict_row = dict(zip(col_name_list, row))
                unload_list.append(dict_row)
            return unload_list
        except Exception as E:
            print 1
            return 'None'

if __name__=="__main__":
    con = sqlite3.connect(u"D://我的资料库//works//SVN//trunk//kiosk//var//db//main.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()
    print json.dumps(get_unload_list_bd(cursor))
    print len(get_unload_list_bd(cursor))


