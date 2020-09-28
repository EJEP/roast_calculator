import os
from flask import Flask
from roast_calculator import calculator


def create_app(test_config=None):
    flask_app = Flask(__name__)
    flask_app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        flask_app.config.from_pyfile('config.py', silent=True)
    else:
        flask_app.config.from_mapping(test_config)

    try:
        os.makedirs(flask_app.instance_path)
    except OSError:
        pass

    flask_app.register_blueprint(calculator.bp)

    return flask_app


