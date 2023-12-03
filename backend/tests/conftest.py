# ======================== imports ========================
from fastapi.testclient import TestClient
from pymongo import MongoClient
from backend.app.main import app
import pytest
import sys
import os

# ============ add the test_events folder in the directory to the path ============
sys.path.append('./test_events')


# ======================== helper functions ========================
def clean_up(mongo_client):
    mongo_client.drop_database(os.getenv("DATABASE_NAME"))

# ======================== fixtures ========================

# ============ this is the startup and teardown for each test ============
@pytest.fixture(scope="session",autouse=True)
def database_reset():
    mongo_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
    clean_up(mongo_client)
    yield 
    clean_up(mongo_client)
    

# ========== this is to initialise the FastAPI client ==========
@pytest.fixture(scope="session",autouse=True)
def client():
    with TestClient(app) as c:
        yield c
