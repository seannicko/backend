import logging
import os
from time import time
from typing import Dict, Any

from pymongo.errors import DuplicateKeyError

from src.main.domain.Session import Session
from src.main.domain.methods import make_id, parseAuth
from src.main.service.MongoService import MongoService
from src.main.domain.User import User


class AuthenticationError(Exception):
    code = 401
    message = 'User not authenticated'


class DuplicateUser(Exception):
    code = 409
    message = 'user already exists'


class SessionManager:

    service = MongoService()
    sessions: Dict[str, Session] = {}

    def getSession(self, sessionId, name) -> Any:
        """
        return the session refered to by a request. If the session is no longer authenticated then the
        AuthenticationError is raised.
        this method also handles verifying the current request. To implement, handle the AuthenticationError

        :param sessionId: the session id returned to user when session created
        :param name:
        :return:
        """
        currentTime = time()
        if currentTime - float(sessionId) > int(os.getenv('SESSION_TIMEOUT', 1000)):
            # TODO Sean check me out: timeout of sessions is an environment variable
            logging.info('unauthenticated user request')
            raise AuthenticationError()
        ref = '{}_{}'.format(sessionId, str(name))
        # TODO handle no sessions byb cathcing keyerror on ref
        try:
            return self.sessions[ref]
        except:
            logging.info('unauthenticated user request')
            raise AuthenticationError()

    def startSession(self, name, password):
        """
        create a new session in the sessions dictionary and return the sessionId to the client

        if password is correct raise authentication error

        :param name: plain name string
        :param password: hashed password
        :return:
        """
        user = self.getUser(name)

        if password == user[1]:
            currentSession = Session(str(make_id(name)))
            self.sessions['{}_{}'.format(currentSession.serverTime, str(make_id(name)))] = currentSession
            return str(currentSession.serverTime)
        else:

            raise AuthenticationError()

    def makeUser(self, name, password):
        """
        Create a new user and empty measurement, keyed by the hashed id of plain string name. The name is as it
        appears in the Session object. Measurements for a user are queried using a session object

        If a user is created with a name already in use, a conflict is returned

        :param name:
        :param password:
        :return:
        """
        new_user = User(username=str(make_id(name)), password=password)
        try:
            self.service.users.insert_one(new_user.__dict__)
            self.service.measurement.insert_one({"_id": new_user._id, "measurement":[]})
        except DuplicateKeyError as e:
            raise DuplicateUser()

    def changePassword(self, user, password):
        """
        Change user password
        TODO: accept old password to check
        TODO: forgot password email functionality
        :param user:
        :param password:
        :return:
        """
        self.service.users.find_and_modify({'_id': user}, {'password': password})
        return 'ok'

    def getUser(self, name: str) -> User:
        """
        Get details of a user
        return details of a user

        :param name: the plain name string
        :return:
        """
        user_list = []
        hashedUserName = make_id(name)
        userObject = self.service.users.find_one({'_id': str(hashedUserName)})
        print(userObject)
        user = userObject['_id']
        password = userObject['password']
        user_list.append(user)
        user_list.append(password)
        # TODO switch order of auth objects so that its identifier and item
        return user_list

    def check_User(self, name: str):
        """
        Check DB for user
        """
        user_list = []
        hashedUserName = make_id(name)
        try:
            userObject = self.service.users.find_one({'_id': str(hashedUserName)})
            print(userObject)
            user = userObject['_id']
            user_list.append(user)
        except:
            pass
        if len(user_list) >0:
            return "Valid"
        return "Not Valid"

    def endSession(self, auth):
        """
        delete a session from the list
        :param auth:
        :return:
        """
        auth = parseAuth(auth)
        ref = '{}_{}'.format(auth['sessionId'], auth['username'])
        del self.sessions[ref]
