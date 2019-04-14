from flask_classy import FlaskView, route

from src.main.domain.methods import parseAuth
from src.main.rest.MeasurementManager import MeasurementManager
from src.main.rest.SessionManager import SessionManager, AuthenticationError


class SessionController(FlaskView):

    measurementManager = MeasurementManager()
    sessionManager = SessionManager()

    @route("/startSession/<string:auth>", methods=["PUT"])
    def startSession(self, auth):
        """
        start a session. If the password is incorrect, return 401

        :param auth: a string formatted as <name:password>
        :return: the session id to the user
        TODO Sean check me out: This implements parseAuth
        """
        auth = parseAuth(auth)
        try:
            return self.sessionManager.startSession(auth['username'], auth['password'])
        except AuthenticationError as e:
            return e.message, e.code

    @route("/endSession/<string:auth>", methods =["DELETE"])
    def endSession(self, auth):
        """
        log out of an active session

        :param auth: auth string consisting of session id and username
        :return: confirmation string
        """
        self.sessionManager.endSession(auth)
        return 'ok'

    @route("makeUser/<string:username>/<string:password>")
    def makeUser(self, username, password):
        """
        Create a user and store details in the database

        :param username: plain username
        :param password: hashed password hashed by the front end.
        :return: welcome string
        TODO assert that the username does not already exist
        """
        self.sessionManager.makeUser(username, password)
        return 'welcome {}'.format(username)

