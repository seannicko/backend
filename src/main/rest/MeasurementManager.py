from bson import ObjectId

from src.main.domain.methods import make_id
from src.main.service.MongoService import MongoService
from src.main.domain.Session import Session
import logging


class MeasurementNotFound(Exception):
    message = 'measurement not found'
    code = 404


class MeasurementManager:

    service = MongoService()

    def updateMeasurement(self, name,  measurement) -> None:
        """
        find a users measurement and add one observation to it based on a session

        :param session:
        :param measurement:
        :return:
        """
        # TODO implement find_and_modify

        x = self.service.measurement.find_one({"_id": str(make_id(name))})
        try:
            x['measurement'].append(measurement)
        except:
            raise MeasurementNotFound()
        y = self.service.measurement.replace_one(filter={"_id": str(make_id(name))}, replacement=x)
        logging.info("Updated measurement for user {}".format(str(make_id(name))))
        if y.acknowledged == None:
            logging.error("could not add measurement for user {}".format(str(make_id(name))))
