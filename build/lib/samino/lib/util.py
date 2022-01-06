from base64 import b64encode, b64decode
from fake_useragent import UserAgent
from hashlib import sha1
from uuid import uuid4
import hmac

api = "https://service.narvii.com/api/v1{}".format


def sh(key: str, data: bytes):
    return hmac.new(bytes.fromhex(b64decode(key).decode()[::-1]), data, sha1)


def c(value: bytes = str(uuid4())[:15].encode()):
    return (
        b64decode("MzI=").decode() +
        value.hex() +
        sh("ZTNkYmYxNzkxOGE1MzRiNzdlMWI4YjczMWVkYWNjYWE2NTFhNGI2Nw==", b64decode(b'Mg==') + value).hexdigest()
    ).upper()


def s(data):
    return b64encode(
        b64decode(b'Mg==') +
        sh("MmU0ZDk2YTY4MjNmOWVjMDFiMzk1NWVlMjQwOWE3MGEzYmU4OWZiZg==", data.encode()).digest()
    ).decode()


def ua():
    return str(UserAgent().chrome)


def uu():
    return str(uuid4())
