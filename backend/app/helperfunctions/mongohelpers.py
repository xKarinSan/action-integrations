# ======================== imports ========================
from backend.app.database import *
from fastapi.encoders import jsonable_encoder
import logging

# ======================== bottom level functions ========================
def get_one_item_by_id(collection_name,object_id):
    return database[collection_name].find_one({
        "_id": object_id
     })

def get_all_items(collection_name):
    items = []
    if collection_name in database.list_collection_names():  
        for item in database[collection_name].find():
            items.append(item)
    return items

# ========================== top level functions==========================
def create_new_item(collection_name,collection_object):
    try:
        # collection_object = jsonable_encoder(collection_object)
        new_object = database[collection_name].insert_one(collection_object)
        created_object = get_one_item_by_id(collection_name,new_object.inserted_id)
        if created_object:
            return True
        return False
    
    except Exception as e:
        logging.error("[create_new_item]"+str(e))
        return False
