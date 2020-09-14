# coding: utf-8


from flask import json


def test_hello(client):
    """ test hello route """
    r = client.get("/api/")
    assert 200 == r.status_code


def test_add_task(client):
    """ test add task route """
    data = { "description": "Simple task" }
    r = client.post("/api/add", json=data)
    assert 201 == r.status_code


def test_add_task_no_data(client):
    """ test if 401 is returned if no data provided """
    data = {}
    r = client.post("/api/add", json=data)
    assert 500 == r.status_code


def test_get_task(client):
    """ Test get a task """
    data = { "description": "Simple taks" }
    client.post("/api/add", json=data)

    r = client.get("api/get/1")
    assert 200 == r.status_code


def test_get_fake_test(client):
    """ Test get a fake task """
    r = client.get("api/get/2")
    assert 404 == r.status_code