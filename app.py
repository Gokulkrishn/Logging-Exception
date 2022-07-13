from flask import Flask
from ML.logger import logging
from ML.exception import MLException

import sys

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():

    ## Inducing error to test Exception code
    try:
        raise Exception("This is a test exception")
    except Exception as e:
        raise MLException(e,sys) from e
        logging.info(MLException.error_message)
        logging.info('WE are testing logging module')

    return "This is home page of Logging app"


if __name__ == "__main__":
    app.run(debug=True,port=8000)