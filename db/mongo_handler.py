from pymongo import MongoClient
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()


class MongoDBHandler:

    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("MONGO_DB_NAME")]
        self.collection = self.db[os.getenv("MONGO_COLLECTION")]

    def get_today_mint_entries(self):
        """Fetch entries from today containing 'mint' in filename (case-insensitive)"""
        today_start = datetime.now(timezone.utc).replace(hour=0,
                                                         minute=0,
                                                         second=0,
                                                         microsecond=0)

        query = {
            "timestamp": {
                "$gte": today_start
            },
            "filename": {
                "$regex": "mint",
                "$options": "i"
            }  # Case-insensitive
        }

        return list(self.collection.find(query))


# Singleton instance
mongo_handler = MongoDBHandler()
