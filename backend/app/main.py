from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# the mongodb functions
from backend.app.mongoclient import *
# from app.mongoclient import *

app = FastAPI()

@app.get("/")
def read_root():
    print("hello world")
    # print(os.environ["DATABASE_URL"])
    return {"msg": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



# handle event on start; connect database


# handle event on end; disconnect database



# =============== tutorial test =================
@app.get("/api/todo")
async def get_todo():
    return 1


@app.get("/api/todo/{id}")
async def get_todo_by_id(id: int):
    return 


@app.post("/api/todo")
async def post_todo(todo):
    return 1


@app.put("/api/todo/{id}")
async def put_todo(id,data):
    return 1


@app.delete("/api/todo/{id}")
async def delete_todo(id):
    return 1