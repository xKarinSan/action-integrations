# ======================== imports ========================
# ====== import fastapi-relevant modules ======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from mangum import Mangum
import os 

# ====== import routes ======
from backend.app.routers.EventRouters import event_router


# ======================== initialisation ========================
load_dotenv()
# ====== init the fastAPI instance & configurations ======
app = FastAPI()
frontend_url = os.getenv("FRONTEND_URL")
print("frontend_url",frontend_url)
origins =[frontend_url]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ======================== adding routes ========================
# ====== healthcheck ======
@app.get("/")
def read_root():
    return {"msg": "Hello World"}
# ====== routes events ======
app.include_router(event_router,tags=["Events"],prefix="/api/event")



# ======================== adding lambda handler ========================
handler = Mangum(app)