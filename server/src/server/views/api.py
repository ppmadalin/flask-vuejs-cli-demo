# coding: utf-8

from flask import Blueprint, request, jsonify
from server.model import Task


api = Blueprint("demo", __name__, url_prefix="/api")


@api.route("/")
def home():
    return "Hello World!"


@api.route("/add", methods=["POST"])
def add():
    """ Add new task. """
    data = request.get_json()
    if data.get("description"):
        task = Task()
        task.description = data.get("description")
        task.save()
        return "Task created", 201
    return "No task created", 500


@api.route("/get/<id>", methods=["GET"])
def get(id):
    """ Return task by id. """
    task = Task.query.filter_by(id=id).first()
    if task:
        data = {
            "id": task.id,
            "description": task.description,
            "completed": task.completed,
        }
        return jsonify(data), 200
    return "Task not found", 404