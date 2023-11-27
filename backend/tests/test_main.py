import pytest
# from backend.tests.testconfig import api_client
from backend.app.mongoclient import database_client

import os

def clean_up():
    database_name = os.getenv("DATABASE_NAME")
    print("database_name: ",database_name)
    database_client.drop_database(database_name)
    
    # for entity in range(len(entities)-1, -1, -1):
    #     client.delete("/"+entities[entity]+"/deleteall")


# ========================================FastAPI test========================================


@pytest.fixture(scope="module")
def test_fixture():
    clean_up()
    # yield will be ignored in pytest 4.0
    yield "resource"
    clean_up()