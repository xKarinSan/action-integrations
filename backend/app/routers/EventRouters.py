# ======================== imports ========================
from datetime import datetime
from backend.app.helperfunctions.mongohelpers import *
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
@event_router.post("",tags=["Events","POST"],name="Create an events")
async def create_event_route(new_event: Event):
    new_event = jsonable_encoder(new_event)
    if not new_event:
        raise HTTPException(400, "Event is required")
    if not new_event["name"]:
        raise HTTPException(400, "Event name is required")
    if not new_event["event_date"] or new_event["event_date"] < 0:
        raise HTTPException(400, "Event date is required")
    if new_event["event_date"] < datetime.timestamp(datetime.now()):
        raise HTTPException(400, "Invalid date")
    
    event_successfully_created = create_new_item("event",new_event)
    if event_successfully_created:
        return {'message': 'Event created'}
    raise HTTPException(400, "Something went wrong")



# ============= GET =============
# ===== get all events =====
@event_router.get("",tags=["Events","GET"],name="Get all events")
async def get_all_events_route():
    try:
        events = []
        return {"events": get_all_items("event")}
    except  Exception as e: 
        logging.error("[GET /api/event]"+str(e))
        raise HTTPException(400, "Something went wrong")

# ============= UPDATE =============

# ============= DELETE =============