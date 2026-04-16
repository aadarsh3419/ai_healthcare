from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None
db = None

async def connect_db():
    global client,db

    client = AsyncIOMotorClient(settings.MONGODB_URL)
    db = client[settings.DATABASE_NAME]

    print(f"mongodb connect:{settings.DATABASE_NAME}")

async def disconnect_db():
    global client
    if client:
        client.close()
        print("mongodb disconnect")

def get_db():
    return db