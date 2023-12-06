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

# ====== startup/shutdown ======
# DO NOT USE FOR LAMBDA
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # initialise the database
#     app.mongodb_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
#     app.database = app.mongodb_client[os.getenv("DATABASE_NAME")]
#     yield
#     # shut down the database
#     app.mongodb_client.close()


# ====== init the fastAPI instance & configurations ======
# app = FastAPI(lifespan=lifespan)
app = FastAPI()
origins =['http://localhost:8000']
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
app.include_router(event_router)



# ======================== adding lambda handler ========================
handler = Mangum(app)