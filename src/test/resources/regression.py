"""
TODO Seach check me out
Regretion testing module to get test data into database with users.


"""
import json
import random
import string
import names

from src.main.domain.methods import make_id
from src.main.rest.MeasurementManager import MeasurementManager
from src.main.rest.SessionManager import SessionManager

sessionManager = SessionManager()
measurementManager = MeasurementManager()

def randomString(stringLength=12):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def make_user():
    """
    make a single user with a random name and password and return a dict representation to append to a file
    :param out: the list
    :return:
    """
    password = randomString(8)
    name = names.get_first_name().lower()
    out = {'name': name, 'password': password}
    sessionManager.makeUser(name, str(make_id(password)))
    return out


if __name__ == '__main__':
    out = []
    # TODO Sean check me out: test data loader. Make a function to pick random string from list for measurement items
    for i in range(10):
        print(i)
        user = make_user()
        out.append(user)

        sessionId = sessionManager.startSession(user['name'], str(make_id(user['password'])))
        for j in range(4):
            measurement = {
                "comment": "free text comment",
                "date": "27-01-38",
                "frequency": 1,
                "location": "Left hand",
                "severity": 1,
                "specific": "Constipation",
                "time": "Morning",
                "trigger": "Skin"
            }
            session = sessionManager.getSession(sessionId, str(make_id(user['name'])))
            measurementManager.updateMeasurement(user['name'], measurement)

    with open('users.txt', 'w') as file:
        file.writelines(json.dumps(out))
