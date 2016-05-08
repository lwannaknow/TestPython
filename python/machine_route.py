# coding=utf-8
__author__ = 'jim'

import json

import pymqi

def submit(queue_data):
    queue_dict = json.loads(queue_data)
    machine_id = queue_dict['machine_id']
    message_type = queue_dict['machine_type']
    token = queue_dict['token']
    qmgr = pymqi.connect('qmr', 'CLIENT.QM_ORANGE', 'machine_ip_port')
    que = pymqi.Queue(qmgr, machine_id)
