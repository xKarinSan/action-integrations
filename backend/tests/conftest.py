from fastapi.testclient import TestClient
from backend.app.main import app
import pytest
import sys
from pymongo import MongoClient
import os


sys.path.append('./test_events')
def clean_up(mongo_client):
    mongo_client.drop_database(os.getenv("DATABASE_NAME"))

# ========== this is to reset the database ==========
@pytest.fixture(scope="session",autouse=True)
def database_reset():
    
    mongo_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
    clean_up(mongo_client)
    yield "resource"
    clean_up(mongo_client)
    

# ========== this is to initialise the FastAPI client ==========
@pytest.fixture(scope="session",autouse=True)
def client():
    with TestClient(app) as c:
        yield c
