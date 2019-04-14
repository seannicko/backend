import hashlib

import names
from bson import ObjectId

from src.main.domain.Session import Session
from src.main.domain.MeasurementInput import MeasurementInput
from src.main.rest.MeasurementController import MeasurementController
from src.main.service.MongoService import MongoService

mongoService = MongoService()
measurementManager = MeasurementController()

def make_id(string) -> ObjectId:
    id = hashlib.md5(string.encode('utf-8')).hexdigest()
    id = id[:24]
    return ObjectId(id)

def readAndPopulateData():
    with open('./resources/test_data.json') as file:
        
        id = make_id('rory')
        input_file = file.read()
    data = MeasurementInput(input_file, id)
    mongoService.measurement.insert_one({"_id": id, 'measurement': [data.__dict__]})

def updateMeasurement():
    session = Session(make_id(names.get_first_name('male')), 'password')
    with open('./resources/test_data.json') as file:
        input_file = file.read()
    input = MeasurementInput(input_file, session)
    measurementManager.updateMeasurement(session, input)



if __name__ == '__main__':
    readAndPopulateData()
    updateMeasurement()
