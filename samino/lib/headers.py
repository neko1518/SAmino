import json
from .util import c, s, uu, ua

uid = None
sid = None
deviceId = None


class Headers:
    def __init__(self, data=None, lang: str = "ar-SY"):
        if deviceId: self.deviceId = deviceId
        else: self.deviceId = c(uid)

        self.headers = {
            "NDCDEVICEID": self.deviceId,
            "NDCLANG": lang[:lang.index("-")],
            "Accept-Language": lang,
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": ua(),
            "AUID": uu(),
            "SMDEVICEID": uu(),
            "Host": "service.narvii.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        self.web_headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            "user-agent": ua(),
            "x-requested-with": "xmlhttprequest"
        }

        if sid:
            self.headers["NDCAUTH"] = sid
            self.web_headers["cookie"] = sid

        if uid:
            self.uid = uid

        if data:
            self.headers["Content-Length"] = str(len(data))
            if type(data) is not str: data = json.dumps(data)
            self.headers["NDC-MSG-SIG"] = s(data)
