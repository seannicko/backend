import logging
import traceback

from flask import Flask
from flask_cors import CORS

from src.main.rest.MeasurementController import MeasurementController
from src.main.rest.QueryController import QueryController
from src.main.rest.SessionController import SessionController

logging.basicConfig(level=logging.DEBUG)
logging.FileHandler('/var/tmp/myapp.log')

app = Flask(__name__)
cors = CORS(app)
app.config['APPLICATION_ROOT']='/api'

# This is where we add FlaskView object to the Flask app
MeasurementController.register(app)
SessionController.register(app)
QueryController.register(app)


@app.errorhandler(500)
def internal_error(exception):
    print("500 error caught")
    print(traceback.format_exc())
    return traceback.format_exc()


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", debug=True)
