# coding: utf-8

from flask.globals import current_app
from server.flask_app import db


class Task(db.Model):
    """ Simple task model. """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.description

    def save(self):
        db.session.add(self)
        db.session.commit()
