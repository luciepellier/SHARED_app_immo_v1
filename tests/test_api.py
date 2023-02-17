from ..api import app # Flask instance of the API
import json
import pytest

def test_get_all_contracts():
    response = app.test_client().get('/contractapi/contracts')
    res = json.loads(response.data.decode('utf-8')).get('Contracts')
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['occupant'] == 'Pablo'
    assert res[1]['occupant'] == 'Maria'
    assert response.status_code == 200
    assert type(res) is list

def test_get_occupant():
    response = app.test_client().get('/occupantapi/occupants')
    res = json.loads(response.data.decode('utf-8')).get('Occupants')
    assert response.status_code == 200
    assert res[0]['id'] == 1
    assert res[0]['firstName'] == 'Laura'
    assert res[0]['lastName'] == 'Rodriguez'

def test_edit_occupant_lastName():
    response = app.test_client().get('/occupantapi/occupants')
    res = json.loads(response.data.decode('utf-8')).get('Occupants')
    assert response.status_code == 200
    assert res[0]['lastName'] == 'Dominguez'