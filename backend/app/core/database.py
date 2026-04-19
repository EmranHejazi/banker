import asyncpg
from .config import settings

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(settings.DATABASE_URL, min_size=5, max_size=20)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()
            self.pool = None

db = Database()
