import pytest
# from backend.tests.testconfig import api_client
import sys
from pymongo import MongoClient
import os
sys.path.append('./test_events')

def clean_up(mongo_client):
    mongo_client.drop_database(os.getenv("DATABASE_NAME"))

# ========================================FastAPI test========================================
@pytest.fixture(scope="session",autouse=True)
def database_reset():
    mongo_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
    clean_up(mongo_client)
    yield "resource"
    clean_up(mongo_client)
    