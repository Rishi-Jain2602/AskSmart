import pymongo, os
from datetime import datetime
MongoDb_Connection_str = os.environ['MONGODB_STR']

client = pymongo.MongoClient(MongoDb_Connection_str)
db = client['Rag']
conv_collection = db['Conv']

def update_db(user_id,query,response):   
    conversation_entry = {
        "user_id": user_id,
        "query": query,
        "response": response,
        "timestamp": datetime.utcnow().isoformat()
    }

    user_entry = conv_collection.find_one({"user_id": user_id})
    if not user_entry:
        conv_collection.update_one(
            {"user_id": user_id},
            {
                "$set": {"user_id": user_id, "timestamp": datetime.utcnow().isoformat()},
                "$push": {"conversations": conversation_entry}
            },
            upsert=True
        )
    else:
        conv_collection.update_one(
            {"user_id": user_id},
            {"$push": {"conversations": conversation_entry}}
        )
    return None