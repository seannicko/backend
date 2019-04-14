import os


class MongoServiceConstants(object):
    def __init__(self):
        self.USERS = os.getenv('USERS', 'users')
        self.port = os.getenv('MONGO_PORT', '27017')
        self.MARKETS = os.getenv('MARKET_DETAILS', 'marketDetails')
        self.DATABASE_NAME = os.getenv('MONGO_DATABASE', 'my_database')
        self.PASSWORD = os.getenv('MONGO_PASS', 'root')
        self.USERNAME = os.getenv('MONGO_USER', 'root')
        self.HOST = '{}:{}'.format(os.getenv('MONGO_HOST', '0.0.0.0'), self.port)
        self.TIMEOUT = os.getenv('MONGO_TIMEOUT', str(10))
        self.MEASUREMENTS = os.getenv('MEASUREMENTS', 'measurements')
