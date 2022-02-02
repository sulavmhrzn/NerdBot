import urllib.parse
from datetime import datetime

import motor.motor_asyncio
from decouple import config


class NoFapWrapper:
    def __init__(self):
        self.username = urllib.parse.quote_plus(config("MONGODB_USERNAME"))
        self.password = urllib.parse.quote_plus(config("MONGODB_PASSWORD"))
        self.conn_str = f"mongodb+srv://{self.username}:{self.password}@cluster0.hiu9p.mongodb.net/DiscordBot?retryWrites=true&w=majority"
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.conn_str)
        self.collection = self.client.DiscordBot.nofaptracker

    async def _user_exist(self, user_id: int) -> bool:
        """Return True if user_id exist in database."""

        user = await self.collection.find_one({"id": user_id})
        return bool(user)

    async def fetch_records(self) -> list[dict]:
        """Returns all records in the database"""

        documents = []

        async for doc in self.collection.find():
            documents.append(doc)
        return documents

    async def fetch_one(self, user_id: int) -> dict:
        """Returns a record from database"""

        doc = await self.collection.find_one({"id": user_id})
        if not doc:
            return {"err": True, "msg": "User does not exist"}

        return {"err": False, "msg": doc}

    async def insert(self, user_id: int, start_date: str = None) -> dict:
        """Insert into database with the given user_id"""

        if not start_date:
            start_date = str(datetime.now().date())

        if await self.collection.find_one({"id": user_id}):
            return {"err": True, "msg": f"User {user_id} already exist."}

        value = {"id": user_id, "start_date": start_date, "days": 0}
        result = await self.collection.insert_one(value)
        return {"err": False, "msg": "User {user_id} inserted successfully."}

    async def update_many(self, day: int = None) -> None:
        """Increments every record with 1."""

        await self.collection.update_many({"id": {"$gt": 1}}, {"$inc": {"days": 1}})

    async def reset_days(self, user_id: int) -> dict:
        """Resets day to 0 for the given user_id"""

        if not await self._user_exist(user_id):
            return {"err": True, "msg": "User {user_id} does not exist."}

        await self.collection.update_one({"id": user_id}, {"$set": {"days": 0}})
        return {"err": False, "msg": "Days reseted successfully for user {user_id}"}
