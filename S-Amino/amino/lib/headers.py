class Headers:
    def __init__(self, response):
        self.headers = {
            "NDCDEVICEID": "019B6133991CBC2428F822E55AEF0499B3E674928B3268072CC9381881024F07047DCB9A82899C91B8",
            "NDCAUTH": response['sid']
        }
        self.uid = response['auid']