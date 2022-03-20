from base64 import b64encode, b64decode
from hashlib import sha1
from uuid import uuid4
import requests
import platform
import logging
import socket
import uuid
import json
import hmac
import re

api = "https://service.narvii.com/api/v1{}".format
tapjoy = "https://ads.tapdaq.com/v4/analytics/reward"


def c():
    return requests.get(f"https://pysc-overall.herokuapp.com/api/generate-did").text


def s(data):
    return requests.get(f"https://pysc-overall.herokuapp.com/api/generate-sign?data={data}").text


def uu():
    return str(uuid4())
