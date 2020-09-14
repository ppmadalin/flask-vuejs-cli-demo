# coding: utf-8

import pathlib
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""


class ProductionConfig(Config):
    DB_USERNAME = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    # mysql://username:password@server/db
    DB_URI = (
        f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DATABASE_NAME}"
    )
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = pathlib.Path(__file__).parent.joinpath("instance/tasks.db")
    DB_URI = f"sqlite:///{DATABASE}"
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
