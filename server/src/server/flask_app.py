# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env="DEV"):
    """ Application Factory """

    app = Flask(__name__)

    # application configuration
    if env == "DEV":
        app.config.from_object("server.config.DevelopmentConfig")
    elif env == "TEST":
        app.config.from_object("server.config.TestingConfig")
    elif env == "PROD":
        app.config.from_object("server.config.ProductionConfig")

    # init apps
    db.init_app(app)

    # register blueprints
    from server.views.api import api

    app.register_blueprint(api)

    return app
