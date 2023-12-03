from pydantic import BaseModel, Field
import uuid;

class Event(BaseModel):
    id: str= Field(default_factory=uuid.uuid4, alias="_id")
    name:str
    # just keep the timestamp
    event_date: int
