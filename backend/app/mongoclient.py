# from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os 
from backend.app.models.TodoModel import Todo
# from app.models.TodoModel import Todo

# mongodb Driver

from motor import motor_asyncio


load_dotenv()
uri = os.getenv("DATABASE_URL")
client = motor_asyncio.AsyncIOMotorClient(uri)
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True