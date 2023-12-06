# ======================== imports ========================
from datetime import datetime
from fastapi import APIRouter,HTTPException, Request
from backend.app.models.EventModel import *
from backend.app.database import *
from fastapi.encoders import jsonable_encoder
import logging



# =================== intiialise router ===================
event_router = APIRouter()

# ==================== CRUD operations ====================
# ============= POST =============
# ===== create new event =====
@event_router.post("/api/event",tags=["Events","POST"],name="Create an events")
async def create_event_route(request: Request,new_event: Event):
    # try:
    new_event = jsonable_encoder(new_event)
    print("event",new_event)
    if not new_event:
        raise HTTPException(400, "Event is required")
    if not new_event["name"]:
        raise HTTPException(400, "Event name is required")
    if not new_event["event_date"] or new_event["event_date"] < 0:
        raise HTTPException(400, "Event date is required")
    if new_event["event_date"] < datetime.timestamp(datetime.now()):
        raise HTTPException(400, "Invalid date")
    
    new_event = database["event"].insert_one(new_event)
    created_event = database["event"].find_one({
        "_id": new_event.inserted_id
    })
    if created_event:
        return {'message': 'Event created'}
    raise HTTPException(400, "Something went wrong")
    
    # except Exception as e:
    #     logging.error("[POST /api/event]"+e)
    #     raise HTTPException(400, "Something went wrong")

# ============= GET =============
# ===== get all events =====
@event_router.get("/api/event",tags=["Events","GET"],name="Get all events")
async def get_all_events_route(request: Request):
    try:
        print("database",database)
        # print("database[event]",database["event"])
        # print(database.list_collection_names())
        events = []
        if "event" in database.list_collection_names():  
            for event in await database["event"].find():
                events.append(event)
            print("[get_all_events_route] events",events)
        return {"events": events}
    except  Exception as e: 
        logging.error("[GET /api/event]"+str(e))
        raise HTTPException(400, "Something went wrong")

# ============= UPDATE =============

# ============= DELETE =============