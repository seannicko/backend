import json
from datetime import time


class MeasurementInput:
    def __init__(self, input):
        """
        This function takes a JSON string of the form
        {
            "comment": "free text comment"
            "date": "irrelevent"
            "frequency": 1
            "location": "Left hand"
            "severity": 1
            "specific": "Constipation"
            "time": "Morning"
            "trigger": "Bowel/Bladder"
        }
        And adds it to a users measurement
        """
        input_json = json.loads(input)
        if len(input_json) > 1:
            input_json = input_json[-1]
        else:
            input_json = input_json[0]
        self.comment = input_json['comment']
        self.date = input_json['date']
        self.frequency = input_json['frequency']
        self.location = input_json['location']
        self.severity = input_json['severity']
        self.time = input_json['time']
        self.trigger = input_json['trigger']
        self.specific = input_json['specific']


