import hashlib
from time import time

from bson import ObjectId


class Session:
    """
    Session objects are retrieved using the sessionManager.getSession method. They are used to
    """

    _id: ObjectId = None
    password: ObjectId = None

    def __init__(self, username):
        self._id = username
        self.serverTime = time()




