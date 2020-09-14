# coding: utf-8

import click
from flask.cli import with_appcontext
from server.flask_app import db


@click.command(name="init_db")
@with_appcontext
def init_db():
    db.create_all()
