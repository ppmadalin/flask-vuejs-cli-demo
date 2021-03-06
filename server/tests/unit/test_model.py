# coding: utf-8

from sqlalchemy.orm import query
from server.model import Task


def test_task_definition():
    """ Test if model can save a task """
    task = Task()
    task.description = "Simple task"
    assert "Simple task" == task.description


def test_save_task_to_database(app):
    """ Test if a task can be saved to database. """
    task = Task()
    task.description = "Simple task"
    with app.app_context():
        task.save()
        assert 1 == len(Task.query.all())


def test_get_task_by_id(app):
    """ Test if a task is returned by id. """
    task = Task()
    task.description = "Simple task"
    with app.app_context():
        task.save()
        saved_task = Task.query.filter_by(id=1).first()
        assert 1 == saved_task.id
