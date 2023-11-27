# =========== import fastapi ===============
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# the mongodb functions
from backend.app.mongoclient import *
# from app.mongoclient import *



# =========== import routes ===============
from backend.app.routers.EventRouters import event_router

# =========== initialise app ===============
app = FastAPI()
origins =['http://localhost:8000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    print("hello world")
    # print(os.environ["DATABASE_URL"])
    return {"msg": "Hello World"}





# =============== event routes =================
app.include_router(event_router)

# =============== tutorial test =================
# @app.get("/api/todo")
# async def get_todo():
#     response = await fetch_all_todos()
#     return response

# @app.get("/api/todo/{title}", response_model=Todo)
# async def get_todo_by_title(title):
#     response = await fetch_one_todo(title)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {title}")

# @app.post("/api/todo/", response_model=Todo)
# async def post_todo(todo: Todo):
#     response = await create_todo(todo.dict())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong")

# @app.put("/api/todo/{title}/", response_model=Todo)
# async def put_todo(title: str, desc: str):
#     response = await update_todo(title, desc)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {title}")

# @app.delete("/api/todo/{title}")
# async def delete_todo(title):
#     response = await remove_todo(title)
#     if response:
#         return "Successfully deleted todo"
#     raise HTTPException(404, f"There is no todo with the title {title}")