# ======================== test cases ========================
# ============ successfully view date ============
def test_get_all_events_success(client):
    response = client.get("/api/event/")
    assert response.status_code == 200
    assert "events" in response.json()



