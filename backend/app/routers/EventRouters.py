from datetime import datetime
from fastapi import APIRouter,HTTPException, Request
from backend.app.models.EventModel import *
from fastapi.encoders import jsonable_encoder

event_router = APIRouter()


# ==================== CRUD operations ====================
# ============= POST =============
@event_router.post("/api/event",tags=["Events","POST"],name="Create an events")
def create_event_route(request: Request,event: Event):
    event = jsonable_encoder(event)
    print("event",event)
    if not event:
        raise HTTPException(400, "Event is required")
    if not event["name"]:
        raise HTTPException(400, "Event name is required")
    if not event["event_date"] or event["event_date"] < 0:
        raise HTTPException(400, "Event date is required")
    if event["event_date"] < datetime.timestamp(datetime.now()):
        raise HTTPException(400, "Invalid date")
    
    new_event = request.app.database["event"].insert_one(event)
    created_event = request.app.database["event"].find_one({
        "_id": new_event.inserted_id
    })
    if created_event:
        return {'message': 'Event created'}
    raise HTTPException(400, "Something went wrong")

# ============= GET =============
@event_router.get("/api/event",tags=["Events","GET"],name="Get all events")
async def get_all_events_route(request: Request):
    try:
        events = []
        for event in request.app.database["event"].find():
            events.append(event)

        print("[get_all_events_route] events",events)
        return {"events": events}
    except: 
        raise HTTPException(400, "Something went wrong")

# ============= UPDATE =============

# ============= DELETE =============