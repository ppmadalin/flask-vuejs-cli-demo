# coding: utf-8

import pathlib


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""


class ProductionConfig(Config):
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DATABASE_NAME = ""
    # mysql://username:password@server/db
    DB_URI = (
        f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DATABASE_NAME}"
    )
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MYSQL_ROOT_PASSWORD = ""


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = pathlib.Path(__file__).parent.joinpath("instance/tasks.db")
    DB_URI = f"sqlite:///{DATABASE}"
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
