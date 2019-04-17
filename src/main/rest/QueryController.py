import json

from flask import request
from flask_classy import FlaskView, route
import logging as LOG
from src.main.domain.MeasurementInput import MeasurementInput
from src.main.domain.Session import Session
from src.main.rest.MeasurementManager import MeasurementManager
from src.main.service.MongoService import MongoService
from src.main.rest.SessionController import SessionController




class QueryController(FlaskView):

    mongoService = MongoService()
    sessionController = SessionController


    @route("/<string:auth>/get_measurement", methods=["GET"])
    def getMeasurement(self, auth):
        split = auth.split(":")
        name = split[0]
        sessionID = split[1]
        currentSession = self.sessionController.getSession(sessionID, name)
        x = self.mongoService.measurement.find_one({"_id": currentSession._id})
        return json.dumps(x)


