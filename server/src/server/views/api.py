# coding: utf-8

from flask import Blueprint


api = Blueprint("demo", __name__)


@api.route("/", methods=["GET", "POST"])
def home():
    return "Hello World!"