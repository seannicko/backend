import json
from flask import request
from flask_classy import FlaskView, route

from src.main.domain.MeasurementInput import MeasurementInput
from src.main.domain.Session import Session
from src.main.domain.methods import parseSession
from src.main.rest.MeasurementManager import MeasurementManager, MeasurementNotFound
from src.main.rest.SessionManager import SessionManager, AuthenticationError
from src.main.service.MongoService import MongoService


class MeasurementController(FlaskView):

    measurementManager = MeasurementManager()
    mongoService = MongoService()
    sessionManager = SessionManager()

    @route("updateMeasurement/<string:auth>", methods=["PUT"])
    def updateMeasurement(self, auth):
        """
        if Session has expired or was deleted then appropriate response is returned. Otherwise the
        measurement is updated.
        TODO Sean check me out
        Erors in measurement must be handled with an alert and return to home. This is done by conditions of the response
        on the front end

        :param auth:
        :return:
        """
        auth = parseSession(auth)
        try:
            # TODO Sean check me out: implementing authentication
            session = self.sessionManager.getSession(auth['sessionId'], auth['username'])
        except AuthenticationError as e:
            # TODO Sean check me out: dealing with invalid users, we send a status code for the front end to interpret
            return e.message, e.code

        measurementInput = MeasurementInput(request.data)
        try:
            self.measurementManager.updateMeasurement(auth['username'], measurementInput.__dict__)
        except MeasurementNotFound as e:
            return e.message, e.code
        return json.dumps(measurementInput.__dict__)

    @route("/<string:auth>/get_measurement", methods=["GET"])
    def getMeasurement(self, auth):
        user = auth.split(':')[0]
        session = Session(user)
        x = self.mongoService.measurement.find_one({"_id": session._id})
        return json.dumps(x)


