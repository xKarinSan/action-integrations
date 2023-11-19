def EventSchema(event) -> dict:
    return{
        "_id": str(event["_id"]),
        "name": event["name"],
        "event_date": event["event_date"],
    }