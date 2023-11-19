from fastapi import FastAPI
from pydantic import BaseModel

class Event(BaseModel):
    name:str
    # just keep the timestamp
    event_date: int