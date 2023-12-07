from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()
mongodb_client = MongoClient(os.getenv("DATABASE_URL"),tls=True, tlsAllowInvalidCertificates=True)
database = mongodb_client[os.getenv("DATABASE_NAME")]
