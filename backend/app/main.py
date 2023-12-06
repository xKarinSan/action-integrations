# ======================== imports ========================
# ====== import fastapi-relevant modules ======
import logging
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
mongodb_client = None
database = None

# ====== init the fastAPI instance & configurations ======
# app = FastAPI(lifespan=lifespan)
app =FastAPI()
origins =['http://localhost:8000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("starting")
    app.mongodb_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
    app.database = app.mongodb_client[os.getenv("DATABASE_NAME")]
    print("started")

@app.on_event("shutdown")
async def shutdown_event():
    print("ending")
    app.mongodb_client.close()
    print("ended")

   


# ======================== adding routes ========================
# ====== healthcheck ======
@app.get("/")
def read_root():
    return {"msg": "Hello World"}

# ====== routes events ======
app.include_router(event_router, tags=['Event'], prefix='/api/event')

print("main.py app")
# ======================== adding lambda handler ========================
handler = Mangum(app)