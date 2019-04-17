from bson import ObjectId

from src.main.service.MongoService import MongoService
from src.main.domain.Session import Session
from src.main.domain.MeasurementInput import MeasurementInput
import logging as LOG
import json

import pymongo

class MeasurementManager:

    def __init__(self):
        # connect to mongo
        self.service = MongoService()
        pass

    def getMeasurement(self, session: Session) -> MeasurementInput:
        x = self.service.measurement.find_one({"_id": ObjectId(session._id)})
        LOG.info("Updated measurement for user {}".format(session._id))
        if x.acknowledged == None:
            LOG.error("could not get measurement for user {}".format(session._id))
        return x


