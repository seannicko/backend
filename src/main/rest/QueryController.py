import json
from flask_classy import FlaskView, route

from src.main.rest.QueryManager import QueryManager
from src.main.rest.SessionManager import SessionManager, AuthenticationError
from src.main.service.MongoService import MongoService


class QueryController(FlaskView):

    mongoService = MongoService()
    sessionManager = SessionManager()
    queryManager = QueryManager()


    @route("/get_measurement/<string:auth>", methods=["GET"])
    def getMeasurement(self, auth):
        split = auth.split(":")
        name = split[0]
        sessionID = split[1]
        try:
            session = self.sessionManager.getSession(sessionID, name)
        except AuthenticationError as e:
            return e

        measurements = self.queryManager.getMeasurement(session)
        return json.dumps(measurements)


# <src.main.domain.Session.Session object at 0x105c25b00>

