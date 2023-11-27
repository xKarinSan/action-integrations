import sys 
import os 
# sys.path.append("config")

from backend.tests.testconfig import api_client
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4



def test_root():
    response = api_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}