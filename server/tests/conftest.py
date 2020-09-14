# coding: utf-8

import pytest
import os
from server.flask_app import create_app
from server.flask_app import db


@pytest.fixture
def app():
    app = create_app()

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
