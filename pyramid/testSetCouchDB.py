# coding=utf-8
import json
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

__author__ = 'jim'

KIOSK_MODEL = {
    "id": "",
    "type": "kiosk",
    "temp": 0,
    "mkc_version": "",
    "mid_version": "",
    "location": "",
    "geo_location": {
        "latitude": 0,
        "longitude": 0
    },
    "status": "offline",
    "last_update": 0
}

kiosk_list = ["M2-B103", "M2-B123"]

result = {}
try:
    with open("./kiosks.json", "r") as f:
        kiosk_info = json.load(f)
        if not kiosk_info:
            LOGGER.warning(".kiosk_list file exist but has no kiosk")
            pass
        else:
            for kiosk_id in kiosk_list:
                kiosk_doc = KIOSK_MODEL.copy()
                kiosk_doc["id"] = "M2-B%s" % kiosk_id
                kiosk_doc["location"] = kiosk_info[kiosk_id]["location"]
                kiosk_doc["geo_location"] = kiosk_info[kiosk_id]["geo_location"]
                result[kiosk_id] = kiosk_doc
                # LOGGER.debug("kiosk %s set. document is %s" % (kiosk_id, kiosk_doc))
except Exception as e:
    LOGGER.error("kiosk_list doesn't exit,%s" % e.message)
print result

for r in range(2):
    print r
