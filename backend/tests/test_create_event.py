from backend.tests.testconfig import api_client
from datetime import datetime

# test_fixture

def test_create_event_success(test_fixture):
    print("test_fixture",test_fixture)
    event_date = datetime.timestamp(datetime(2023, 12, 1))
    response = api_client.post("/api/event", json={"name": "Create new event test","event_date":event_date})
    assert response.status_code == 200
    assert response.json() == {"message": "Event created"}


def test_create_event_unsuccessful_empty_name(test_fixture):
    event_date = int(datetime.timestamp(datetime(2023, 12, 1)))
    response = api_client.post("/api/event", json={"name":"","event_date":event_date})
    assert response.status_code == 400
    assert response.json() == {"detail": "Event name is required"}


def test_create_event_unsuccessful_empty_date(test_fixture):
    # event_date = datetime.datetime(2023, 12, 1)
    response = api_client.post("/api/event", json={"name":"test event 1","event_date":-1})
    assert response.status_code == 400
    assert response.json() == {"detail": "Event date is required"}



def test_create_event_unsuccessful_past_date(test_fixture):
    event_date = datetime.timestamp(datetime(2022, 12, 1))
    response = api_client.post("/api/event", json={"name": "test event","event_date":event_date})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid date"}
