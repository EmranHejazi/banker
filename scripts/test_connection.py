import asyncio, asyncpg

async def test():
    conn = await asyncpg.connect(
        user="banker",
        password="password",
        host="localhost",
        port=5432,
        database="banker"
    )
    print("Connected OK")
    await conn.close()

asyncio.run(test())
