from pymongo.mongo_client import MongoClient
from datetime import datetime

url = "mongodb+srv://balgharisaifullah:5456L6ZNiduHtY5X@acounts.hlguw.mongodb.net/?retryWrites=true&w=majority&appName=acounts"
client = MongoClient(url)

db = client["SERP"]

col = db["accounts"]

def add_account(username, password, role) -> None:
    post = {
        "username": username,
        "password": password,
        "role": role,
        "created_at": datetime.now()
    }
    col.insert_one(post)

def verify_account(username, password, role) -> bool:
    query = {
        "username": username,
        "password": password,
        "role": role
    }
    result = col.find_one(query)

    if result:
        return True
    else:
        return False
    
def remove_account(username, password, role) -> bool:
    query = {
        "username": username,
        "password": password,
        "role": role
    }
    result = col.delete_one(query)

    if result.deleted_count == 1:
        return True
    else:
        return False