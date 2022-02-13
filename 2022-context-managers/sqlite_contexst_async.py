import asyncio 
import logging 


import aiosqlite


async def main():
    logging.basicConfig(level=logging.INFO)
    # async with aiosqlite.connect("application.db") as db:
    #   async with db.execute("SELECT * FROM blogs") as cursor:
    #       logging.info(await cursor.fetchall())
    db = await aiosqlite.connect("application.db")
    cursor = await db.execute("SELECT * FROM blgs")
    logging.info(await cusor.fetchall())

if __name__ == '__main__':
    asyncio.run(main())# python 3.7++