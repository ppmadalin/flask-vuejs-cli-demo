# coding: utf-8

from flask import Flask


def create_app():
    """ Application Factory """

    app = Flask(__name__)

    # register blueprints
    from server.views.api import api

    app.register_blueprint(api)

    return app