import asyncio

async def background_task():
    await asyncio.sleep(5)
    print("Task completed using asyncio")

async def main():
    task = asyncio.create_task(background_task())
    print("Main coroutine continues to run...")
    await task

asyncio.run(main())