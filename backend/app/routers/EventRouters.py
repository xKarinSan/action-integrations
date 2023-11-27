from datetime import datetime
from fastapi import APIRouter,HTTPException
from backend.app.models.EventModel import *
event_router = APIRouter()


# ==================== CRUD operations ====================
# ============= POST =============
@event_router.post("/api/event",tags=["Events","POST"],name="Create an events")
async def create_event_route(event: Event):
    event = dict(event)
    if not event:
        raise HTTPException(400, "Event is required")
    if not event["name"]:
        raise HTTPException(400, "Event name is required")
    if not event["event_date"] or event["event_date"] < 0:
        raise HTTPException(400, "Event date is required")
    if event["event_date"] < datetime.timestamp(datetime.now()):
        raise HTTPException(400, "Invalid date")
    
    response = await create_event_mongo(event)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

# ============= GET =============
@event_router.get("/api/event",tags=["Events","GET"],name="Get all events")
def get_all_events_route():
    return {"msg": "Hello World"}

# ============= UPDATE =============

# ============= DELETE =============