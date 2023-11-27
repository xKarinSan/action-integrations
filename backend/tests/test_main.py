import pytest
# from backend.tests.testconfig import api_client
from backend.app.mongoclient import database_client

import os

async def clean_up():
    database_name = os.getenv("DATABASE_NAME")
    await database_client.drop_database(database_name)
    print("Cleaned up")
    return
    # for entity in range(len(entities)-1, -1, -1):
    #     client.delete("/"+entities[entity]+"/deleteall")


# ========================================FastAPI test========================================


@pytest.fixture(autouse=True, scope="session")
async def test_fixture():
    await clean_up()
    # yield will be ignored in pytest 4.0
    yield
    await clean_up()