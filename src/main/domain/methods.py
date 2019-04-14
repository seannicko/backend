import hashlib
from typing import Dict

from bson import ObjectId


def make_id(string) -> ObjectId:
    id = hashlib.md5(string.encode('utf-8')).hexdigest()
    id = id[:24]
    return ObjectId(id)

def parseSession(authString: str) -> Dict[str, str]:
    """
    take in auth string and return dict of values
    :param authString:
    :return:
    """
    list = authString.split(':')
    out = {}
    out['username'] = list[0]
    out['sessionId'] = list[1]
    return out

def parseAuth(authString: str) -> Dict[str, str]:
    """
    take in auth string and return dict of values
    TODO Sean check me out: standard auth parsing functions
    :param authString:
    :return:
    """
    list = authString.split(':')
    out = {}
    out['username'] = list[0]
    out['password'] = list[1]
    return out
