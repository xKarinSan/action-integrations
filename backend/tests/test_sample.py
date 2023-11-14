from fastapi.testclient import TestClient
import sys 
import os 
sys.path.append("main")

from app.main import app


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}