from backend.tests.testconfig import api_client
from datetime import datetime

# test_fixture
def test_get_all_events_success():
    response = api_client.get("/api/event")
    assert response.status_code == 200
    assert "events" in response.json()
    # response.json() == {"message": "Event"}
    # check if all events are there


