# ======================== imports ========================
from datetime import datetime

# ======================== test cases ========================

# ============ successfully add date ============
def test_create_event_success(database_reset,client):
    event_date = datetime.timestamp(datetime(2024, 12, 1))
    response = client.post("/api/event", json={"name": "Create new event test","event_date":event_date})
    assert response.status_code == 200
    assert response.json() == {"message": "Event created"}

# ============ unsuccessful (empty event name) ============
def test_create_event_unsuccessful_empty_name(database_reset,client):
    event_date = int(datetime.timestamp(datetime(2024, 12, 1)))
    response = client.post("/api/event", json={"name":"","event_date":event_date})
    assert response.status_code == 400
    assert response.json() == {"detail": "Event name is required"}

# ============ unsuccessful (empty event date) ============
def test_create_event_unsuccessful_empty_date(database_reset,client):
    # event_date = datetime.datetime(2023, 12, 1)
    response = client.post("/api/event", json={"name":"test event 1","event_date":-1})
    assert response.status_code == 400
    assert response.json() == {"detail": "Event date is required"}


# ============ unsuccessful (past event date) ============
def test_create_event_unsuccessful_past_date(database_reset,client):
    event_date = datetime.timestamp(datetime(2022, 12, 1))
    response = client.post("/api/event", json={"name": "test event","event_date":event_date})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid date"}
