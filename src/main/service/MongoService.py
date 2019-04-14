import logging as LOG

import pymongo

from src.main.domain.Session import Session
from src.main.service.MongoServiceConstants import MongoServiceConstants


class MongoService:
    """
    This is the mongo database client. The collection and database it uses are stored in the docker.env file
    To start a docker container do:

        `docker exec -it nostalgic_murdock mongo mongo`

    in a terminal
    """

    def __init__(self):
        max_delay = MongoServiceConstants().TIMEOUT
        username = MongoServiceConstants().USERNAME
        password = MongoServiceConstants().PASSWORD
        host = MongoServiceConstants().HOST
        self.client = pymongo.MongoClient(host=host,
                                          username=username,
                                          password=password,
                                          serverSelectionTimeoutMS=max_delay)
        self.db = self.client[MongoServiceConstants().DATABASE_NAME]
        self.measurement = self.db[MongoServiceConstants().MEASUREMENTS]
        self.users = self.db[MongoServiceConstants().USERS]
