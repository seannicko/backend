from bson import ObjectId

from src.main.service.MongoService import MongoService
from src.main.domain.Session import Session
from src.main.domain.MeasurementInput import MeasurementInput
import logging as LOG
import json

import pymongo

class QueryManager:

    def __init__(self):
        # connect to mongo
        self.service = MongoService()
        pass

    def getMeasurement(self, session: Session):
        x = self.service.measurement.find_one({"_id": session._id})
        LOG.info("Got measurement for user {}".format(session._id))
        if x is None:
            LOG.error("No {}".format(session._id))
        return x


