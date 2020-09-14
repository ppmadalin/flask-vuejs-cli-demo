# coding: utf-8

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
  

    