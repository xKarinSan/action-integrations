# ======================== imports ========================
from pydantic import BaseModel, Field
import uuid;

# ======================== the event model ========================
class Event(BaseModel):
    # the unique ID of the event
    id: str= Field(default_factory=uuid.uuid4, alias="_id")
    name:str
    # just keep the timestamp in ms
    event_date: int
