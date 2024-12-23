from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings


MONGODB_URL = f'mongodb://{settings.DB_USER}:{settings.DB_PASSWD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?authSource=admin'

client = AsyncIOMotorClient(MONGODB_URL)

