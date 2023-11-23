from fastapi import FastAPI
from pydantic import BaseModel
from backend.app.mongoclient import database

event_collection = database.events

class Event(BaseModel):
    name:str
    
    # just keep the timestamp
    event_date: int


# ==================== CRUD operations ====================
# ============= POST =============
async def create_event_mongo(event):
    print("[create_event_mongo] event",event)
    await event_collection.insert_one(event)
    return {"message":"Event created"}
# ============= GET =============

# ============= UPDATE =============

# ============= DELETE =============