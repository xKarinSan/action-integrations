from backend.tests.testconfig import client
import datetime

def test_create_event_success():
    event_date = datetime.datetime(2023, 12, 1)
    response = client.post("/api/event", json={"name": "test event","event_date":event_date})
    assert response.status_code == 200
    assert response.json() == {"name": "test event"}


def test_create_event_unsuccessful_empty_name():
    event_date = datetime.datetime(2023, 12, 1)
    response = client.post("/api/event", json={"event_date":event_date})
    assert response.status_code == 403
    assert response.json() == {"message": "Event name is required"}


def test_create_event_unsuccessful_empty_date():
    # event_date = datetime.datetime(2023, 12, 1)
    response = client.post("/api/event", json={"name":"test event 1"})
    assert response.status_code == 403
    assert response.json() == {"message": "Event name is required"}



def test_create_event_unsuccessful_past_date():
    event_date = datetime.datetime(2022, 12, 1)
    response = client.post("/api/event", json={"name": "test event","event_date":event_date})
    assert response.status_code == 200
    assert response.json() == {"name": "test event"}
