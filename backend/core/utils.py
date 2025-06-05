from pymongo import MongoClient
from datetime import datetime
import os
import hashlib
from dotenv import load_dotenv

load_dotenv()

def get_db():
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    return client["data_agent_db"]  # ✅ Your DB name

def save_log(question, answer, filename):
    db = get_db()
    db["agent_age"].insert_one({
        "type": "log",
        "question": question,
        "answer": str(answer),
        "filename": filename,
        "timestamp": datetime.now()
    })

def hash_file_content(data):
    return hashlib.sha256(data).hexdigest()
