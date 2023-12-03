# =========== import fastapi ===============
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient

# the mongodb functions

from dotenv import load_dotenv
import os 

# =========== import routes ===============
from backend.app.routers.EventRouters import event_router

# =========== initialise app ===============
load_dotenv()
uri = os.getenv("DATABASE_URL")

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
    return {"msg": "Hello World"}



@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
    app.database = app.mongodb_client[os.getenv("DATABASE_NAME")]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# =============== event routes =================
app.include_router(event_router)
