import asyncio

loop = asyncio.get_event_loop()

async def my_async_task():
    await asyncio.sleep(4)  # Simulate some asynchronous work
    return "Task Complete"

result = asyncio.create_task(my_async_task())
print(result)
