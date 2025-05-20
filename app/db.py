from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["sentiment_system"]
collection = db["queries"]

def save_query_result(query, df):
    record = {
        "query": query,
        "timestamp": datetime.now(),
        "records": df.to_dict(orient="records")
    }
    collection.insert_one(record)
